#!flask/bin/python
from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return socket.gethostname()  #"Hello, World!"

@app.route('/', methods=['POST'])
def indexPost():
    subprocess.Popen(["python", "./stress_cpu.py"])
    return "";

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)


