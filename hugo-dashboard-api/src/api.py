from flask import Flask, request, jsonify
import methods as m
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hugo Dashboard API'


@app.route('/content/<section>/<page>', methods=['GET'])
def get_content(section, page):
    return jsonify(m.get_contents(section, page))


@app.route('/content/<section>/<page>', methods=['PUT'])
def put_content(section, page):
    # TODO what is content? how do we extract it?
    payload = request.get_json()
    print(json.dumps(payload))
    md_content = payload.get('markdown_contents')
    toml_content = payload.get('toml_fields')
    return jsonify(m.set_contents(section, page, md_content, toml_content))


if __name__ == '__main__':
    app.run()
