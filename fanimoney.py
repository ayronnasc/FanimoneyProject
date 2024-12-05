from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def index():
    return 'Hello World Fanimoney'

