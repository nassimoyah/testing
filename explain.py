####################### creating urls and returning string ##########################

import os
from flask import Flask, Response, request, jsonify, make_response
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)    #creating wsgi application "web standared gataway interface"

@app.route("/")             # decorator 
def welcome():
    return "<h1> hello </h1> <h3> hello </h3> "

@app.route("/success/<score>")             # decorator 
def welcome2(score):
    return "hello you won " + score

if __name__ == "__main__" :  # 
    app.run(port=5550,debug=True)  


    ##################################  rendering ############################

    import os
from flask import Flask, Response, request, jsonify, make_response,redirect,url_for 
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)    #creating wsgi application "web standared gataway interface"

@app.route("/fail/<score>")             # decorator 
def fail(score):
    return "<h1> you failed </h1> " + str(score) 

@app.route("/success/<score>")             # decorator 
def success(score):
    return "<h1> you have succeeded </h1> " + str(score) 
@app.route("/result/<mark>")             # decorator 
def result(mark):
    result=""
    if int(mark) >= 50 : 
        result = "success"
        print(result)
    else : 
        result = "fail" 
        print(result)
    return redirect(url_for(result,score=str(mark))) 



if __name__ == "__main__" :   
    app.run(port=5550,debug=True)  