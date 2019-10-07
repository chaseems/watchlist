from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Wellcome to My Watchlist! This is a Hello World app~"