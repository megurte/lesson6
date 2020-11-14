from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from CI with GitHub Actions by Абрамов'

@app.route('/Abramov')
def v2():
    return 'Hello from CI with GitHub Actions by Абрамов'
#1