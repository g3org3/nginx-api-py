#!/bin/bash
set -e
apt update
apt install -y nginx docker.io python3 python3-pip python3-venv
ln -s /usr/bin/python3 /usr/bin/python
ln -s /usr/bin/pip3 /usr/bin/pip

sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

curl https://zeit.co/custom_error > /usr/share/nginx/html/custom_error.html
cat /usr/share/nginx/html/custom_error.html > /usr/share/nginx/html/404.html
cat /usr/share/nginx/html/custom_error.html | sed s.404.502.g > /usr/share/nginx/html/50x.html

mkdir /root/apps
cd /root/apps
git clone https://github.com/g3org3/nginx-api-py.git
cd nginx-api-py
bash run.sh > /root/apps/nginx-api-py.log & echo $! > /root/apps/nginx-api-py.pid
