from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello API week hackers!!</p>"

if __name__ == "__main__":
    app.run(debug=True)