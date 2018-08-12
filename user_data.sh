#!/bin/bash
set -e
apt update
apt install -y nginx python3 python3-pip python3-venv
ln -s /usr/bin/python3 /usr/bin/python
ln -s /usr/bin/pip3 /usr/bin/pip

mkdir /root/apps
cd /root/apps
git clone https://github.com/g3org3/nginx-api-py.git
cd nginx-api-py
bash run.sh > /root/apps/nginx-api-py.log & echo $! > /root/apps/nginx-api-py.pid