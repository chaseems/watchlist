from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to My Watchlist! This is a Hello World app~"

@app.route('/user/<name>')
def test(name):
    return '<h1>This is a %s page.</h1><img src="http://helloflask.com/totoro.gif">' % name

@app.route('/test')
def test_url_for():
    # pls use command line window to watch URL
    print(url_for('hello'))
    print(url_for('user_page',name='chen'))
    print(url_for('user_page',name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test page'