from flask import Flask, render_template, request, redirect, session, flash, url_for
from classes.class_user import User
from classes.class_gain import Gain
from classes.class_outgoing import Outgoing

app = Flask(__name__, instance_relative_config=True)

#data
user1 = User('Ayron',15,'M','123')
gain1 = Gain('Ayron', 'salario', 'fixo', 1000, '12/12/24')
outgoing1 = Outgoing('Ayron', 'Conta de Luz', 'fixo', 0, 200, '12/07/24')
user_data = [user1,gain1,outgoing1]

@app.route('/')
def index():
    return render_template('index.html', user_data=user_data, rota="index")

@app.route('/gain')
def gain():
    return render_template('gain.html', user_data=user_data, rota="gain")
