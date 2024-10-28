先下载安装docker 有客户端 也可使用命令行

sudo apt-get install docker

记得换源！ 

在GUI里面改成这个

{

  "debug": true,

  "experimental": false,

  "registry-mirrors": [

​    "https://docker.mirrors.ustc.edu.cn",

​    "https://hub-mirror.c.163.com"

  ]

}

然后往docker内拉取20.04版本内核的ubuntu

docker pull ubuntu:20.04

创建一个名为ubuntu-test的容器

docker run -itd --name apaam ubuntu:20.04

进入容器，进入命令行开始操作。进入容器内的ubuntu的命令行

docker exec -it apaam /bin/bash

升级 apt-get

Apt-get update

apt-get upgrade

安装sudo

apt-get install sudo

安装vim

sudo apt-get install vim 

安装 zip

sudu apt-get install zip

安装netdem环境

sudo apt **install** build-essential

sudo apt-**get** **install** -y autoconf-archive automake cmake texinfo

sudo apt-**get** **install** openmpi-**bin** libopenmpi-dev libboost-**all**-dev

安装lzip环境

Sudo apt-get install lzip

移动 gmp

docker cp /Volumes/apaam-lch/gmp-6.2.1.tar.lz ea0b057da580:/usr/local/gmp-6.2.1.tar.lz

解压gmp

lzip -d gmp-6.2.1.tar.lz

tar -xvf gmp-6.2.1.tar

安装 

cd gmp-6.2.1

./configure --enable-cxx

make

sudo make install

安装解压

sudo apt-get install zip

docker cp /Volumes/apaam-lch/gh_2.20.2_linux_arm64.deb ea0b057da580:/usr/local/gh_2.20.2_linux_arm64.deb





拷贝整体文件夹后解压







将文件从宿主机传入docker内（在宿主机的终端！）

docker cp /Volumes/apaam-lch/apaam-lch-test.zip 

90c4d02a0095:/usr/local/apaam-lch-test.zip





docker container ls -l

docker commit -m "apaam_test" -a "lichh53" apaam thapaam:1.0

docker save -o /Users/lch/Documents/thapaam.tar thapaam:1.0









x