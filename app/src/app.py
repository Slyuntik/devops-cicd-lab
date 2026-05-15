import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "service": "devops-cicd-demo",
        "version": "1.0.0",
        "hostname": socket.gethostname()
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/greeting')
def greeting():
    flag = os.getenv('FEATURE_NEW_GREETING', 'false').lower() == 'true'
    if flag:
        return jsonify({"message": "Hello from new feature!"})
    return jsonify({"message": "Hello, world!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)