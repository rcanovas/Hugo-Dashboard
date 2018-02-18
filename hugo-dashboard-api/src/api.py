from flask import Flask, request, jsonify, make_response
import methods as m
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hugo Dashboard API'


@app.route('/content/<section>/<page>', methods=['GET'])
def get_content(section, page):
    response = m.get_contents(section, page)
    return make_response(jsonify(response), response['status'])


@app.route('/content/<section>/<page>', methods=['PUT'])
def put_content(section, page):
    # TODO what is content? how do we extract it?
    payload = request.get_json()
    print(json.dumps(payload))
    md_content = payload.get('markdown_contents')
    toml_content = payload.get('toml_fields')
    response = m.set_contents(section, page, md_content, toml_content)
    return make_response(jsonify(response), response['status'])


@app.route('/content/<section>/<page>', methods=['POST'])
def post_content(section, page):
    payload = request.get_json()
    print(json.dumps(payload))
    md_content = payload.get('markdown_contents')
    toml_content = payload.get('toml_fields')
    response = m.new_content(section, page, md_content, toml_content)
    return make_response(jsonify(response), response['status'])


@app.route('/content/<section>/<page>', methods=['DELETE'])
def delete_content(section, page):
    response = m.remove_content(section, page)
    return make_response(jsonify(response), response['status'])


if __name__ == '__main__':
    app.run()
