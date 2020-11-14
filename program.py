from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello 1'

@app.route('/v2')
def v2():
    return 'Hello 2'

@app.route('/Abramov')
def v2():
    return 'Hello from CI with GitHub Actions by Абрамов'
#1