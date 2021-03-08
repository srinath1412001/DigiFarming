# -*- coding: utf-8 -*-
"""
@author: Hariom Chaturvedi (@hariomch)
"""

from flask import Flask
from flask import request
from flask import redirect,url_for
from Linear_Model import model

app = Flask(__name__)

@app.route('/success')
def success(temperature,humidity,moisture):
      model([temperature,humidity,moisture])
               
           
@app.route('/test', methods = ['POST','GET'])
def test():
    if request.method=='POST':
        Temp = request.form['temprature_from_web']
        Rh = request.form['rh']
        Soil_moist = request.form['soil_moist']
        Area = request.form['area']
        return redirect(url_for('success',temperature=Temp,humidity = Rh,moiture=Soil_moist))
    
    else:
        Temp = request.args.get('temprature_from_web')
        Rh = request.args.get('rh')
        Soil_moist = request.args.get('soil_moist')
        Area = request.args.get('area')
        return redirect(url_for('success',temperature=Temp,humidity = Rh,moiture=Soil_moist))
    
@app.route('/')
def hello():
    return 'Hello'
    
if __name__ =='__main__':
    app.run(debug = False)
