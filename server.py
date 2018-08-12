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
  return compose(shell)("hostname")

@app.route("/nginx")
def nginx_test():
  res = { "status": 404, "message": "nginx was not found" }
  if not isNginxAvailable(): return json.dumps(res)
  res['status'] = 200
  res['message'] = "yes!"
  return json.dumps(res)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9493)