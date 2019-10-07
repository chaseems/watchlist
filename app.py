from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to My Watchlist! This is a Hello World app~"

@app.route('/test')
def test():
    return "This is a test page."