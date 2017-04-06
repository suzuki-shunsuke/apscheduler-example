# Python でスケジューリングのサンプル

* APSchedulerを使う
  * http://apscheduler.readthedocs.io/en/3.3.1/userguide.html
  * [.travis.ymlを見る限り3系もサポートしている](https://github.com/agronholm/apscheduler/blob/master/.travis.yml)
  * http://qiita.com/yushin/items/a026626dbb291dd43dd8o
  * [詳細なドキュメントはGitHubのリポジトリにある](https://github.com/agronholm/apscheduler/tree/master/docs)

以下のようなポイントを満たすサンプルを書いてみた

* 一定時間ごとにジョブを実行
* ジョブの多重起動は禁止
* ジョブのエラーハンドリング
* ジョブの失敗時にスケジューリング自体を停止する

## Requirements

* Python 3

## Setup

```
$ pip install -r requirements.txt
```

## 実行

```
python main.py
```
