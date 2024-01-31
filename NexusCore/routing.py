from flask import Flask, request
from bson import json_util
from flask_cors import CORS, cross_origin
from NexusCore import NexusCore

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
global nexuscore
nexuscore = NexusCore()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<category>", methods=['GET'])
def get_category_docs(category):
    count = request.args.get('count') if request.args.get('count') else 100
    docs = nexuscore.get_category_docs(category, count)
    res = []
    for doc in docs:
        print(doc)
        res.append(json_util.dumps(doc))
    # def sort_objects_by_timestamp(objects):
    #     # Sort the list of objects by timestamp in descending order (most recent first)
    #     sorted_objects = sorted(objects, key=lambda x: x['published'], reverse=True)
    #     return sorted_objects
    # res = sort_objects_by_timestamp(res)
    return {'data': res}

@app.route("/<category>", methods=['POST'])
def post_category_doc(category):
    document = request.args.get('document') if request.args.get('count') else {}
    if document == {} or type(document) == type([]):
        return {"status": 400, "msg": "No document in args or document is an array"}
    id = nexuscore.mongodb.insert_document(
        nexuscore.db_name,
        category,
        document
    )
    return {
            "status": 200, 
            "msg": "Docuemnt successfully inserted in to db",
            "id": id
        }


