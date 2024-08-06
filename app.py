from flask import Flask ,Response ,request,redirect,url_for,render_template ,jsonify
from pymongo import MongoClient
import json
from bson.objectid import ObjectId   # we can use the object id as text 


app = Flask(__name__)    #creating wsgi application "web standared gataway interface"

@app.route("/")             # decorator 
def welcome():
    return render_template('main.html')


if __name__ == "__main__" :   
    app.run(port=5550,debug=True)  