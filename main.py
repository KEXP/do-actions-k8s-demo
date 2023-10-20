import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"Hello again! From {hostname}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
