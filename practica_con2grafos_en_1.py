#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:56:48 2019

@author: salim
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/salim/Desktop/EDEM/Python/Code')

a11 = pd.read_csv ('rentals_weather_2011.csv', sep=',', decimal='.')

a12 = pd.read_csv ('rentals_weather_2012.csv', sep=';', decimal=',')

a11 = a11.drop(columns=['Unnamed: 0'])

a11 = a11.rename(columns={'dteday_x':'dteday'})


a12.day = a12.day - 365

a12.drop(a12.tail(1).index,inplace=True) # drop last n rows (borrar ultima linea)

y12 = a12[['day', 'cnt']]
y11 = a11[['day', 'cnt']]

y12 = y12.rename(columns={'cnt':'cnt_12'})
y11 = y11.rename(columns={'cnt':'cnt_11'})

y112 = pd.merge(y11, y12, on='day')

#Representar dos años en una gráfica
plt.scatter(y112.day,y112.cnt_11)
plt.scatter(y112.day,y112.cnt_12)
plt.title("Figura . Rented Bicycles Comparation 11-12") #Titulo
plt.xlabel("Nr. of Day")   # Establece el título del eje x
plt.ylabel("Nr. of Rented Bicycles")   # Establece el título del eje y
plt.scatter(y112.day,y112.cnt_11,linewidths=1,label = 'Sales 2011',color ="Green")
plt.scatter(y112.day,y112.cnt_12,linewidths=1,label = 'Sales 2012', Color ="Blue")
plt.legend()
plt.savefig('Sales_11_12.jpg')
