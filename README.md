```sh
#!/bin/bash
apt update
apt install -y nginx python3 python3-pip python3-venv
alias python=python3

mkdir /root/apps
cd /root/apps
git clone https://github.com/g3org3/nginx-api-py.git
cd nginx-api-py
bash run.sh
```