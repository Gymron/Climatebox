import Actions
from flask import Blueprint, request, redirect, url_for

views = Blueprint('views', __name__)
actions = Actions.Actions()


@views.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    wtemp = request.form['wtemp']
    temp = request.form['temp']
    humidity = request.form['humidity']
    actions.setTemp(float(temp))
    actions.setWTemp(float(wtemp))
    actions.setHumidity(float(humidity))
    actions.getValuesAndParseData()
    return redirect('/')


@views.route('/')
def home():
    acthum = actions.stf.gethummitity()
    acttemp = actions.stf.gettemp()
    actwtemp = actions.stf.getWtemp()
    retstr = "<h1>Dashboard</h1><form action='/submit_form' method='POST'>"
    retstr = retstr + str(acthum) + " Humidity " + str(acttemp) + " Temperature " + str(actwtemp) + " Water Temperature "
    retstr = retstr + "<input type='text' name='wtemp'><input type='text' name='temp'>"
    retstr = retstr + "<input type='text' name='humidity'><input type='submit' value='Go'></form>"
    return retstr