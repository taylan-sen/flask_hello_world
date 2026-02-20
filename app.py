"""Flask hello world application — runs locally or on a server."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


if __name__ == "__main__":
    # 0.0.0.0 allows connections from other machines (e.g. when deployed on a server)
    app.run(host="0.0.0.0", port=5000)
