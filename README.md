# docker-studty-001

## Docker勉強会用資料

### Docker環境の構築(事前準備)　勉強会当日までなんとかDockerの動く環境を作ってください

以下の①～④のどれか

#### ①docker on WSL（非推奨）

今動いているWindowsに直にLinuxを入れるパターン

https://qiita.com/koinori/items/78a946fc74452af9afba#ubuntu-1604-lts--docker-17033

サンプルコードぐらいは動くが逆にそれ以外はなにも動かない

#### ②docker on Linux on VirtualBox（ローカルPCでちゃんとしたLinuxの環境作りたい人向け）

今動いているWindowsに一度VirtualBoxを入れてその中でLinux　Dockerとつかっていきたい人向け

https://qiita.com/idani/items/fb7681d79eeb48c05144

#### ③docker on Linux on EC2（クラウドでちゃんとしたLinuxの環境作りたい人向け）

個人のEC2でLinux立ち上げてそこでDocker動かす

https://qiita.com/yumatsud/items/33bc22f7d8f640a286f4

#### ④Docker for windows（まぁまぁ大変）

Windows10 Proでしか動かないので、要確認

https://qiita.com/manamiTakada/items/c1394e5e3358802a9446

https://ops.jig-saw.com/techblog/docker-for-windows-install/


#### ①~④の確認方法

docker run hello-worldが動けばDockerの実行環境はできてます

```
root@Cho17-0073:~# docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
1b930d010525: Pull complete                                                                                             Digest: sha256:b8ba256769a0ac28dd126d584e0a2011cd2877f3f76e093a7ae560f2a5301c00
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

root@Cho17-0073:~#
```
