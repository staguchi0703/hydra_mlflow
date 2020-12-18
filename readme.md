# memo

## Hydra

* pythonファイルの書き方
    * hydraから読み込んだ値を使う場合は、関数に`@hydra.main(config_path='./conf/config.yaml')`とconfigファイルの場所を指示する。
* 実行時引数
    * `python xxxx.py`に続いて
    * `-m model=lightlbg,nn`と書く
    * ここでmodelがconf内のmodelディレクトリ
    * その中のlighbgmとnnのyamlを見に行っている
    * model=以下を,で繋ぐときに**半角スペースを入れない！**

## Mlflow

* mlflowで管理するpythonファイルをつくる
* 上記pythonファイルを実行する
* mlrunsに結果が保存される
* `mlflow ui -h 0.0.0.0:5000`でtracking serverを起動する
    * mlrunsのソースを指定する場合は、`--backend-store-uri ./src`と指定する
* ホストの[ローカルホスト](http://localhost:5000)から接続する