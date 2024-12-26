from flask import Flask, render_template, request, redirect, session, flash, url_for
from classes import User, Gain, Outgoing

app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'ayron'

#data
user1 = User('Ayron',15,'M','123')
user_data = [user1]
gain_data = []

@app.route('/')
def index():
    return render_template('index.html', user_data=user_data, rota="index")

@app.route('/gain')
def gain():
    return render_template('gain.html', user_data=user_data, gain_data=gain_data, rota="gain")

@app.route('/gain/new', methods=['GET', 'POST'])
def new_gain():
    if request.method == 'POST':
        name        = request.form.get('gainName')
        desc        = request.form.get('gainDesc')        
        date        = request.form.get('gainDate')
        value       = request.form.get('gainValue')
        gain_type   = request.form.get('gainType')

        #Verifying data
        for data in [name, desc, date, value, gain_type]:
            if not data:
                flash('Todos os campos são obrigatórios!', 'danger')
                return redirect(url_for('new_gain'))
        
        #turn data in object format
        gain = Gain(user1.name, name, desc, gain_type, value, date)
        gain_data.append(gain)

        flash('Ganho cadastrado com sucesso!', 'success')
        return redirect(url_for('gain'))

    return render_template('new_gain.html', user_data=user_data, rota="gain") 

@app.route('/outgoing')
def outgoing():
    return render_template('outgoing.html', user_data=user_data, rota="outgoing")

@app.route('/investment')
def investment():
    return render_template('investment.html', user_data=user_data, rota="investment")

@app.route('/config')
def config():
    return render_template('config.html', user_data=user_data, rota='config')

@app.route('/switch_theme')
def switch_theme():
    return render_template('index.html', user_data=user_data, rota='switch_theme')

@app.route('/profile')
def profile():
    return render_template('profile.html', user_data=user_data, rota='profile')

