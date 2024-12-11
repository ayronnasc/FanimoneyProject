import classes
from flask import Flask, render_template, request, redirect, session, flash, url_for
from FanimoneyProject.classes import User

app = Flask(__name__, instance_relative_config=True)

#data
User = User('Ayron Nasc',15,'M','123')

@app.route('/')
def index():
    return render_template('index.html')
