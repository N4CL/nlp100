# coding: utf-8

from flask import Flask
from app.controller import service

app = Flask(__name__)
app.register_blueprint(service.app)

if __name__ == '__main__':
    SERVER_IP = "0.0.0.0"
    app.run(host=SERVER_IP, debug=True)
