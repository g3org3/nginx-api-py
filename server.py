from flask import Flask
from flask import request
import subprocess
from flask import jsonify

def shell(line):
  try:
    output = subprocess.check_output(line.split(' '))
    return output.strip()
  except:
    return "false"

def isNginxAvailable():
  return shell("which nginx") is not "false"
def isDefaultPathAvailable():
  return shell("ls -la /etc/nginx/sites-available/default") is not "false"

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/hostname")
def hostname():
  return shell("hostname")

@app.route("/nginx")
def nginx_test():
  res = { "status": 404, "message": "nginx was not found" }
  if not isNginxAvailable(): return jsonify(res), 404
  res['status'] = 200
  res['message'] = "yes!"
  return jsonify(res)

@app.route("/nginx/start", methods=['POST'])
def nginx_start():
  res = { "status": 404, "message": "nginx was not found" }
  if not isNginxAvailable(): return jsonify(res), 404
  shell("nginx")
  res['status'] = 200
  res['message'] = "yes!"
  return jsonify(res)

@app.route("/nginx/stop", methods=['POST'])
def nginx_stop():
  res = { "status": 404, "message": "nginx was not found" }
  if not isNginxAvailable(): return jsonify(res), 404
  shell("nginx -s stop")
  res['status'] = 200
  res['message'] = "yes!"
  return jsonify(res)

@app.route("/nginx/reload", methods=['POST'])
def nginx_reload():
  res = { "status": 404, "message": "nginx was not found" }
  if not isNginxAvailable(): return jsonify(res), 404
  shell("nginx -s reload")
  res['status'] = 200
  res['message'] = "yes!"
  return jsonify(res)

@app.route("/nginx/conf", methods=['POST'])
def nginx_conf_create():
  res = { "status": 404, "message": "nginx was not found" }
  if not isNginxAvailable(): return jsonify(res), 404
  if not isDefaultPathAvailable(): return jsonify(res), 404
  conf = request.get_json()['conf']
  f = open("/etc/nginx/sites-available/default", "w")
  f.write(conf)
  f.close()
  return "true"

@app.route("/nginx/conf")
def nginx_conf():
  res = { "status": 404, "message": "nginx was not found" }
  if not isNginxAvailable(): return jsonify(res), 404
  conf = shell('cat /etc/nginx/sites-available/default')
  return conf

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9493)