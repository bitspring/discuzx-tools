#This dockerfile uses the ubuntu image
#VERSION 2-EDITION 1
#Author: wujuguang
#Command format: Instruction[arguments/command]	..
#Base image to use,	this must be set as	the	first line
# FROM ubuntu:14.04
# 国内加速
FROM daocloud.io/ubuntu:14.04

# Maintainer: docker_user <docker_user at email.com> (@docker_user)
MAINTAINER wujuguang wujuguang@126.com

# Commands to update the image
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty main universe" >> /etc/apt/sources.list
RUN apt-get update && apt-get upgrade
RUN apt-get install -y coreutils

# Pip安装Python包的依赖项
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y libxslt1-dev
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN apt-get install -y vim
RUN apt-get clean && apt-get autoclean
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/kylin/Luntan/service-quant
ADD ./requirements.txt /home/kylin
ADD ./scripts/install-avbin-linux-x86-64-v10 /home/kylin

# 安装mp3支持包
RUN sh /home/kylin/install-avbin-linux-x86-64-v10
RUN pip install -r /home/kylin/requirements.txt

WORKDIR /home/kylin
