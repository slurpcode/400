from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    user_search = 'https://api.github.com/search/users?q=followers:1..10000000&per_page=100'
    user_searches = []
    for i in range(1, 5):
        user_searches.append('%s%s%s' % (user_search, '&page=', i))
    loads = []
    info = []

    for api_search in user_searches:
        page = requests.get(api_search)
        loads.append(json.loads(page.content))
    for i, each_json in enumerate(loads):
        for j, person in enumerate(each_json['items'], 1):
            # print(person)     #k = i * 100 + j
            info.append([person['login'], person['html_url']])
    return render_template('home.html', info=info)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(port=8081, debug=True)
