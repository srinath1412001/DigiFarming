# -*- coding: utf-8 -*-
"""
@author: Hariom Chaturvedi (@hariomch)
"""

from flask import Flask
from flask import request
from flask import redirect,url_for
from Linear_Model import model

#def model(readings):
#    import pandas as pd
#    import numpy as np
#
#    data = pd.read_excel('ActData1.xlsx')
#
#    x= data[['Temp','Rh','Soil_Moist']] 
#    y= data[['Water_content']]
#    
#    from sklearn.model_selection import train_test_split
#    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=101)
#    
#    from sklearn.linear_model import LinearRegression
#    model = LinearRegression()
#    model.fit(x_train,y_train)
#    
#    #predictions = model.predict(x_test)
#    model.predict([readings])

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
