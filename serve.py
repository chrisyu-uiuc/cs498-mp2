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
    subprocess.Popen(["python", "stress_cpu.py"])
    return "";

@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        return json
    else:
        return 'Content-Type not supported!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)


