from flask import Flask, render_template, request, redirect, session, flash, url_for
from classes import User, Gain, Outgoing
from datetime import datetime
import locale
import currency
from babel.dates import format_date, format_datetime, format_time

locale.setlocale(locale.LC_ALL, '')

app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'ayron'

#data
user1 = User('Ayron',15,'M','123')
user_data = [user1]
gain_data = []
gain = Gain('Ayron', 'Venda', 'Venda de um Carro', 'variable', 25000, '2024-12-26')
gain2 = Gain('Ayron', 'Venda', 'Venda de uma Moto', 'variable', 3000, '2025-12-27')
gain3 = Gain('Ayron', 'Venda', 'Venda de uma imovel', 'variable', 300000, '2024-11-27')
gain4 = Gain('Ayron', 'Venda', 'Venda de um apartamento', 'variable', 900000, '2024-12-30')
gain5 = Gain('Ayron', 'Venda', 'Venda de um Computador', 'variable', 4000, '2024-12-30')

gain_data.append(gain)
gain_data.append(gain2)
gain_data.append(gain3)
gain_data.append(gain4)
gain_data.append(gain5)

@app.route('/')
def index():
    return render_template('index.html', user_data=user_data, rota="index")

@app.route('/gain')
def gain():
    gains = {}
    
    for gain in gain_data:
        year = datetime.strptime(gain.date, '%Y-%m-%d').year
        gains[year] = {}

    for year in gains:
        months = {}

        for gain in gain_data:
            gain_year = datetime.strptime(gain.date, '%Y-%m-%d').year 
            month = datetime.strptime(gain.date, '%Y-%m-%d').month                    
            
            if gain_year == year:
                months[month] = []
            
        for gain in gain_data:
            gain_month = datetime.strptime(gain.date, '%Y-%m-%d').month                    
            gain_year = datetime.strptime(gain.date, '%Y-%m-%d').year  

            for month in months.keys():
                if gain_month == month and gain_year == year:
                    months[month].append(gain)
        
        gains[year] = months

    return render_template('gain.html', user_data=user_data, gain_data=gains, other=gain_data, rota="gain")

@app.context_processor
def utility_processor():
    def get_date_format( Format , date):
        if Format == "M":
            if date == 1:
                return "Janeiro"
            elif date == 2:
                return "Fevereiro"
            elif date == 3:
                return "Março"
            elif date == 4:
                return "Abril"
            elif date == 5:
                return "Maio"
            elif date == 6:
                return "Junho"
            elif date == 7:
                return "Julho"
            elif date == 8:
                return "Agosto"
            elif date == 9:
                return "Setembro"
            elif date == 10:
                return "Outubro"
            elif date == 11:
                return "Novembro"
            elif date == 12:
                return "Dezembro"
        elif Format == "D/M/Y":
            return format_date(date, locale='de_DE')           
    return dict(get_date_format=get_date_format)

@app.context_processor
def utility_processor():
    def get_currency_format(amount):
        return currency.pretty(amount, 'BRL')
    return dict(get_currency_format=get_currency_format)

@app.route('/gain/new', methods=['GET', 'POST'])
def new_gain():
    if request.method == 'POST':
        name        = request.form.get('gainName')
        desc        = request.form.get('gainDesc')        
        date        = date(datetime.strptime(request.form.get('gainDate')).year, (datetime.strptime(request.form.get('gainDate')).month, (datetime.strptime(request.form.get('gainDate')).day ))
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

