PrezPoll
==================
PrezPoll is a very simple application that allows you to vote on presidential elections.
The app is based on the flask framework and MongoDB for the backend.

*MongoDB Settings*

Create a DB called `prezpoll`

`use prezpoll`

Create and Election Document in MongoDB

`db.elections.insert({"electionyear" : 2016, "democrat" : "Hillary Clinton", "republican" : "Donald Trump" })`
