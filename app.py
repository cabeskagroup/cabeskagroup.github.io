
from flask import Flask,jsonify,request, render_template, request, flash, redirect, url_for, session
import time

import os
from config import *
import pymongo
import json

from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage


app = Flask(__name__)

app.secret_key = 'sbatrow'


############## WEB SITE START#####################

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():

    return render_template("login.html")

@app.route('/about', methods=['POST', 'GET'])
def about():

    return render_template("about.html")

@app.route('/contact', methods=['POST', 'GET'])
def contact():

    return render_template("contact.html")

@app.route('/projects', methods=['POST', 'GET'])
def projects():

    return render_template("projects.html")

@app.route('/shop', methods=['POST', 'GET'])
def shop():

    return render_template("marketplace.html")

@app.route('/news', methods=['POST', 'GET'])
def news():

    return render_template("news.html")

@app.route('/gallery', methods=['POST', 'GET'])
def contact():

    return render_template("gallery.html")

@app.route('/union', methods=['POST', 'GET'])
def contact():

    return render_template("union.html")

@app.route('/admissions', methods=['POST', 'GET'])
def contact():

    return render_template("admissions.html")



if __name__ == '__main__':


    
    app.run(host='', port=5000, debug=True)