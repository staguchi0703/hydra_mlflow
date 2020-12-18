# memo

## TODO

* `main.py` と推論モジュールを分離する
  * 推論モジュールにhydraからパラメータを渡す感じ
  * 推論モジュールもアルゴリズムごとに分けておく
* configファイルを使いやすい書式にする
  * 方法を考える
  * modelでアルゴルズムを大きく分ける
  * model配下の個別のyamlはもう少し具体的な名前だったり、使いそうな条件を色々詰め込んでおくほうが使いやすそう
* Mlflowサーバコンテナと機械学習コンテナに分けて運用する
  * Mlflowサーバは結果の記録と可視化専門にする
  * 機械学習コンテナはGPUやDLなどの発展的な手段を動かせるようにする
* Oputunaなどのパラメータ最適化ツールの使いこなしを練習する
* 自前の機械学習コードを走らせる

## 使い方
* 完成したら一番楽な使い方を記録しておく

## Hydra

* pythonファイルの書き方
    * hydraから読み込んだ値を使う場合は、関数に`@hydra.main(config_path='./conf/config.yaml')`とconfigファイルの場所を指示する。
* 実行時引数
    * `python xxxx.py`に続いて
    * `-m model=lightlbg,nn`と書く
    * ここでmodelがconf内のmodelディレクトリ
    * その中のlighbgmとnnのyamlを見に行っている
    * model=以下を,で繋ぐときに**半角スペースを入れない！**
* グリッドサーチ
    `python xxx.py -m param1=1,2,3 param2=1,2,3,4`これでparam1×param2のグリッドサーチができる
* hydraをデコレータとして使うと、CWDがhydraのoutputディレクトリとなる。Mlflowのパス指定がおかしくなるので注意

## Mlflow

* mlflowで管理するpythonファイルをつくる
* 上記pythonファイルを実行する
* mlrunsに結果が保存される
* `mlflow ui -h 0.0.0.0:5000`でtracking serverを起動する
    * mlrunsのソースを指定する場合は、`--backend-store-uri ./src`と指定する
* ホストの[ローカルホスト](http://localhost:5000)から接続する
* HydraがCWDを変えてしまうので、メイン関数の頭でCWDをプロジェクトのルートに変更しないとMlflowへの結果の書き込みがバグる