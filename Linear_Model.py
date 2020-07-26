# -*- coding: utf-8 -*-
"""
@author: Hariom Chaturvedi (@hariomch)
"""

def model(readings):
    import pandas as pd
    import numpy as np

    data = pd.read_excel('ActData1.xlsx')

    x= data[['Temp','Rh','Soil_Moist']] 
    y= data[['Water_content']]
    
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=101)
    
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    
    model.fit(x_train,y_train)
    
    predictions = model.predict(x_test)
    model.predict([readings])
