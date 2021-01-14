import datetime
from flask import Flask
from flask import request

__author__ = "Gal Netanel"

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return "Hello world "

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80, debug=True)

