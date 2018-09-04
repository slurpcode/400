"""A very simple Flask Hello World app for you to get started with..."""
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    """Homepage with the GitHub Leaderboard."""
    arr = []
    with open(site_path + 'data/task.csv') as fname:
        for line in fname:
            arr.append(line.rstrip().split(','))
    return render_template('home.html', info=arr, year=datetime.today().year)


@app.errorhandler(404)
def page_not_found(error):
    """Jedi style 404 Not Found page."""
    return render_template('page_not_found.html'), 404


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    """Hello world Flask style."""
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    site_path = './'
    app.run(port=8081, debug=True)
else:
    site_path = '/home/Beast/mysite/'
