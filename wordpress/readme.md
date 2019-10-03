### wordpress起動について

今回はwordpressの起動にdocker-composeを使います。

コンテナ一つだけの起動や、特に起動時パラメーターが不要な場合は、以下のようなDocker runコマンドで実行してます。
（後述の自分で作ったDockerImageを自分で試すときとか）

### docker composeを使用しない場合の起動方法
```
inuga@inuga-VirtualBox:~/docker-study-001/wordpress$ sudo docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=test-pw -d mysql:5.7
44234d3b2c2496cadd541733dfb5ecfaaa44c42dcc1258797e0750f90dcb41d3
inuga@inuga-VirtualBox:~/docker-study-001/wordpress$ sudo docker run --name test-wordpress --link test-mysql:mysql -d -p 8080:80 wordpress
```

wordpressはmysql（DB）が裏にいることが前提で、DBもコンテナとして起動します。

Container間の起動順序やパラメータをまとめたものが、
docker-coposeファイルで、これを使用することにより、運用負荷を低減することができます

### docker composeを使用する場合の起動方法
```
inuga@inuga-VirtualBox:~/docker-study-001/wordpress$ sudo docker-compose up
```
