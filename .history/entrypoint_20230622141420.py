 
from flask import Flask, request
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/SpotItunes'
mongo = PyMongo(app)


db = mongo.db.users
@app.route('/')
def index():
    return '<h1>holaaa<h1>'


@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert({
        'name' : request.json['name'],
        'email' : request.json['email'],
        'password' : request.json['password']
    })
    print (str(ObjectId(id)))
    return 'received'

if __name__=="__main__":
    app.run(debug=True)