from flask import Flask, request
import methods as m

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hugo Dashboard API'


@app.route('/content/<section>/<page>')
def content(section, page):
    if request.method == 'GET':
        return m.get_contents(section, page)
    else:
        return {}


if __name__ == '__main__':
    app.run()
