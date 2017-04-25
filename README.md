# movies_spider
基于Python的Scrapy，针对BT天堂bttt.la的爬虫

1、Docker for Scrapy环境搭建
docker pull hub.c.163.com/public/centos:7.0
docker run --name scrapy -it hub.c.163.com/public/centos:7.0 /bin/bash

yum -y install epel-release
yum -y install python-pip
pip install --upgrade pip
yum -y install gcc gcc-c++ kernel-devel
yum -y install python-devel.x86_64
yum -y install openssl-devel
pip install Scrapy

2、执行
查看容器scrapy是否运行
docker ps -a
如果没有运行，手动启动
docker start scrapy
登陆容器scrapy
docker exec -it scrapy /bin/bash

3、创建Scrapy工程实例
进入工作目录，创建工程实例
scrapy startproject movies_spiders

4、添加爬虫
touch bttt.py