from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Hello Internet"

@app.route('about')
def about():
    return 'This is the about page!'

@app.route('/movies')
def movies():
    return 'There is only one movie playing at the moment and it is called "An introduction to Flask"'