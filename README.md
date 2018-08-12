```sh
#!/bin/bash
wget https://raw.githubusercontent.com/g3org3/nginx-api-py/master/user_data.sh
bash user_data.sh
```

```sh
#!/bin/bash
set -e
apt update
apt install -y nginx docker.io python3 python3-pip python3-venv
ln -s /usr/bin/python3 /usr/bin/python
ln -s /usr/bin/pip3 /usr/bin/pip

mkdir /root/apps
cd /root/apps
git clone https://github.com/g3org3/nginx-api-py.git
cd nginx-api-py
bash run.sh > /root/apps/nginx-api-py.log & echo $! > /root/apps/nginx-api-py.pid
```

```sh
#!/bin/bash
set -e
apt update
apt install -y docker.io
docker run -d --name nginx -p 80:80 -p 443:443 -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy
```