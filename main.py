#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
APSchedulerのサンプル

* 1秒ごとにジョブを実行
* ジョブの実行には2秒かかる
* 最初のジョブでは1とlast_time.txtに書き込む
* ジョブごとに書き込む数字をインクリメントする
* 5と書き込もうした時点でジョブでエラーを起こす
* エラーが起こったらerror.logに"5でエラーが起こりました"と書き込み、スケジューラを停止する
"""

from functools import partial
import os
import time

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR


class JobError(Exception):
    def __init__(self, s):
        self.s = s


def tick():
    time.sleep(2)
    try:
        with open("last_time.txt") as r:
            s = int(r.read().strip())
    except IOError:
        s = 0
    s += 1
    if s == 5:
        raise JobError(s)
    with open("last_time.txt", "w") as w:
        w.write(str(s))


def err_listener(scheduler, event):
    if event.exception:
        with open("error.log", "a") as a:
            a.write("{}でエラーが起こりました\n".format(event.exception.s))
        scheduler.shutdown(wait=False)


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, "interval", seconds=1)
    scheduler.add_listener(partial(err_listener, scheduler), EVENT_JOB_ERROR)
    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
