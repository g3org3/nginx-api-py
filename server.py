from flask import Flask
import subprocess
import functools
import json

def compose(*functions):
  def compose2(f, g):
    return lambda x: f(g(x))
  return functools.reduce(compose2, functions, lambda x: x)

def shell(line):
  try:
    output = subprocess.check_output(line.split(' '))
    return output.strip()
  except:
    return "false"

def isNginxAvailable():
  return shell("which nginx") is not "false"

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
  if not isNginxAvailable(): return json.dumps(res), 404
  res['status'] = 200
  res['message'] = "yes!"
  return json.dumps(res)

@app.route("/nginx/conf")
def nginx_conf():
  res = { "status": 404, "message": "nginx was not found" }
  if not isNginxAvailable(): return json.dumps(res), 404
  conf = shell('cat /etc/nginx/sites-available/default')
  return conf

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9493)