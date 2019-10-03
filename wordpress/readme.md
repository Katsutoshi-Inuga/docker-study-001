### wordpress起動について

今回はwordpressの起動にdocker-composeを使います。

コンテナ一つだけの起動や、特に起動時パラメーターが不要な場合は、以下のようなDocker runコマンドで実行してます。
（後述の自分で作ったDockerImageを自分で試すときとか）

```　一番かんたんな起動方法はdocker run
docker run hello-world
```

wordpressはmysql（DB）が裏にいることが前提で、DBもコンテナとして起動します。

Container間の起動順序やパラメータをまとめたものが、
docker-coposeファイルで、これを使用することにより、運用負荷を低減することができます

### 実行方法
