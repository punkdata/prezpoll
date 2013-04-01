import os
import datetime
from flask import Flask
from flask import render_template
from flask import flash, redirect, url_for, request, make_response
from flask.ext.pymongo import PyMongo

#Create an instance of flask
app = Flask(__name__)

#Build the variables that use the assigned environment variables
HOST = os.environ['OPENSHIFT_MONGODB_DB_HOST']
PORT = int(os.environ['OPENSHIFT_MONGODB_DB_PORT'])
DB_USER = os.environ['OPENSHIFT_MONGODB_DB_USERNAME']
DB_PWD = os.environ['OPENSHIFT_MONGODB_DB_PASSWORD']
DB_NAME = 'prezpoll' #data base name

app.config['MDB_HOST'] = HOST
app.config['MDB_PORT'] = PORT
app.config['MDB_USERNAME'] = DB_USER
app.config['MDB_PASSWORD'] = DB_PWD
app.config['MDB_DBNAME'] = DB_NAME

mdb = PyMongo(app, config_prefix='MDB') #Create instance of PyMongo object

#This function capitalizes names separated with spaces
@app.template_filter("caps")
def capWords(s):
    final = []
    v = s.split()
    if v:
        f = v[0].capitalize()
        l = v[1].capitalize()
        
        return  f + " " + l
    else:
        return s.capitalize()

@app.route("/")
@app.route("/index")
def index():
    elections = mdb.db.elections.find({"electionyear":2012})
    title = "U.S. Prez Pol 2012 - Who are you voting for this Election?"
    #Check if user has already voted
    voted = None
    cook = request.cookies.get('vote') #Check for a cookie
    if cook:
        voted = True
        return render_template("results.html", voted = voted)
    else:
        voted = False
        resp = make_response(render_template("index.html", title = title, elections = elections))
        resp.set_cookie('vote', 'voted', None, datetime.datetime(2012, 11, 8))
        
    return resp

#route to post data that is associated in the role collection
@app.route("/vote", methods=["GET","POST"])
def vote():    
    v = request.form['vote'] #Get the data from the post
    sel = {"pick":v,"timestamp":datetime.datetime.utcnow()}#Build the document to be saved
    #insert into the mongodb
    mdb.db.vote.insert(sel)
    
    return redirect("/results")

@app.route("/results", methods=["GET","POST"])
def results():
    dem = mdb.db.vote.find({"pick":"obama"}).count()
    rep = mdb.db.vote.find({"pick":"romney"}).count()
    lead = None
    color = None
    
    #Check who is in the lead
    if dem > rep:
        lead = "Barack Obama is currently in the lead."
        color = "blue"
    elif dem < rep:
        lead = "Mitt Romney is currently in the lead."
        color = "red"
    else:
    #There is a tie
        lead = "The Candidates are currently tied."
        color = "black"
        
    return render_template("results.html", dem = dem, rep = rep, lead = lead, color = color)
    
if __name__ == "__main__":
    app.run(debug = "True")
    
