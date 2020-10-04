from flask import Flask, request
from flask import Response
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.json_util import dumps, loads

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://172.16.238.10:27017/notes"
mongo = PyMongo(app)

@app.route('/nnotes', methods=['GET'])
def getNnotes():
    nnotes = mongo.db.notes.count({})
    return Response(response = "{ \"elements\": "+dumps(nnotes)+" }", status=200, mimetype="application/json")

@app.route('/notes', methods=['GET'])
def getNotes():
    fnotes = mongo.db.notes.find({})
    return Response(response = dumps(fnotes), status=200, mimetype="application/json")

@app.route('/notes', methods=['POST'])
def postNote():
    mongo.db.notes.insert_one(loads(request.data))
    return Response(response = "{\"res\":\"true\"}", status=200, mimetype="application/json")

@app.route('/notes', methods=['DELETE'])
def deleteNotes():
    mongo.db.notes.remove({})
    return Response(response = "{\"res\":\"true\"}", status=200, mimetype="application/json")
    
@app.route('/cpuusage', methods=['GET'])
def getCpuUsage():
    f = open("/elements/procs/cpu-module", "r")
    return Response(response = f.read(), status=200, mimetype="application/json")
    
@app.route('/ramusage', methods=['GET'])
def getRamUsage():
    f = open("/elements/procs/ram-module", "r")
    return Response(response = f.read(), status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port = 4000)
