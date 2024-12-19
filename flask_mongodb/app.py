import json

from flask import Flask, Response
from pymongo import MongoClient
from bson import json_util

from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)




app = Flask(__name__, static_folder='static', template_folder='templates')
client = MongoClient('mongo', 27017)
db = client['flask_mongodb']
collection = db['users']


@app.route('/add/<name>/<age>')
def add(name=None, age=18):
    result = collection.insert_one({'name': 1})

    otv = JSONEncoder().encode(result.inserted_id)
    return {'j': otv}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
