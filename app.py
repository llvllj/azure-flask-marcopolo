from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/marco/<polo>")
def marco(polo):
    return "%s" % polo
