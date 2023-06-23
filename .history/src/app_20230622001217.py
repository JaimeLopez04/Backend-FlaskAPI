from flask import Flask 
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/prueba'
mongo = PyMongo(app)

bd = mongo.db.users

if __name__=="__main__":
    app.run(debug=True)