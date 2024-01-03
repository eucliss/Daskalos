from flask import Flask, request
from bson import json_util
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<category>", methods=['GET'])
def get_category_docs(category):
    count = request.args.get('count') if request.args.get('count') else 100
    from NexusCore import NexusCore
    nexuscore = NexusCore()
    docs = nexuscore.get_category_docs(category, count)
    res = []
    for doc in docs:
        res.append(json_util.dumps(doc))
    print(res)
    return {'data': res}
