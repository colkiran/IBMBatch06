
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

@app.route("/<usrname>")
def user(usrname):
    return f"<h2> Greetings {usrname}, Welcome to the event.....</h2>"

if __name__ == '__main__':
    app.run(debug=True)
