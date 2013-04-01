PrezPoll on OpenShift
==================
PrezPoll is a very simple application that allows you to vote on presidential elections.
The app is based on the flask framework and MongoDB for the backend.


This git repository helps you get up and running quickly w/ a Flask installation
on OpenShift.


Running on OpenShift
----------------------------

Create an account at http://openshift.redhat.com/

Create a python-2.6 application

    rhc app create -a prezpoll -t python-2.6

Add this upstream flask repo

    cd prezpoll
    git remote add upstream -m master git@github.com:ariv3ra/prezpoll.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://flask-$yournamespace.rhcloud.com

