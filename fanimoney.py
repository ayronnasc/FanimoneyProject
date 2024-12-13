from flask import Flask, render_template


app = Flask(__name__, instance_relative_config=True)

#data

@app.route('/')
def index():
    return render_template('index.html')
