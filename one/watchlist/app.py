from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/dome')
def index():
    return "hello word"


@app.route('/user/<name>')
def user(name):
    return "hello %s" %name