### Hands on

apiディレクトリには消費税を計算するFlaskで作成されたpythonファイルが存在します。

このPythonファイルを含む、Dockerイメージを作成してみてください。

Pyhonの実行環境
- ubuntu（任意）
- Python3
- PythonLibralyのｆlask

DockerImageの作り方

Dockerfileがあるディレクトリで以下のコマンドで実行
taxapiが作成するイメージ名
```
inuga@inuga-VirtualBox:~/apitest$ sudo docker build -t taxapi .

```

作成したイメージの実行
```
inuga@inuga-VirtualBox:~/apitest$ sudo docker run -p 80:5000 taxapi 
```

実行状況の確認
```
inuga@inuga-VirtualBox:~/apitest$ sudo docker ps
```

疎通確認
```
inuga@inuga-VirtualBox:~/apitest$ curl http://172.17.0.1/health-check
```
