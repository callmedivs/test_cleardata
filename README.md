# test_cleardata
Test for ClearData
This goal of this project is to create a simple RESTFul API structure to pass an input_str as an input and return true is it contains all the alphabets and return false if it does'nt.

The REST API runs as a Flask app

# Requirements:

Python3
Flask

# Installation 
For local depolyment only

To Install flask , assuming you have python3 installed already

pip3 install Flask

create a folder app-checker
mkdir app-checker
cd app-checker

then use git clone to get the repo
git@github.com:callmedivs/test_cleardata.git

Then run the Flask application

FLASK_APP=checker.py flask run

Alternativetly you can also use virtualenv to do the installations
Find more info on http://flask.pocoo.org/docs/1.0/installation/#

# Testing

Now using POSTMAN or your browser, you can test the application

Ex:
http://localhost:5000/test/?input_str=2343543  Expected o/p: False
http://localhost:5000/test/3543abcdefghijklmnopqrstuvwxy   Expected o/p: False

http://localhost:5000/test/3543abcdefghijklmnopqrstuvwxyz  Expected o/p: True 


