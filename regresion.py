#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:32:52 2019

@author: salim
"""

#a + b*X
# intercept cuando estoy a 0 cuanto vendo 
#R^2 significa si tiene impacto o no (que percentaje de mis vientas depende de la otra variable)





#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 

# Change working directory
os.chdir('/Users/salim/Desktop/EDEM/Python/Code')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK

#REGRESSION
from statsmodels.formula.api import ols
model1=ols('cnt ~temp_celsius', data=wbr).fit()
model1.summary2()

#No. Observations: Número de casos
#R-squared: Precisión del modelo va de 0 a 1 / Cuanto más alto mejor
#Coef: Intercepet punto de partida / temp_celsius coeficiente (numéro de bicis que vendo cuando todas las otras variables son 0)
#P>|t|: P value
#Por cada incremento de 1 de temp celsius se produce un incremento de ventas de b (tempcelsius.coef)

model2=ols('cnt ~windspeed_kh', data=wbr).fit()
model2.summary2()



#fit calculame la pendiente 
modell = ols('cnt ~ temp_celsius', data=wbr).fit()
modell.summary2()


#Modelo de regresion con 2 

model2 =ols('cnt ~ temp_celsius + windspeed_kh', data=wbr).fit()
print(model2.summary2())


#coger otra variable humedad
wbr.hum.hist()

#Modelo 3 humeadad

model3 =ols('cnt ~ temp_celsius + windspeed_kh + hum', data=wbr).fit()
print(model3.summary2())


#modelo 4
model4 =ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday', data=wbr).fit()
print(model4.summary2())


# coef intercept numéro de bicis que vendo cuando todas las otras variables son 0)
# coef temp_celsius por cada incremento de 1 temp_celius aumentan mis ventas 161.
# Coef working day en los no working day 4009 pero si quito los otros vendo 125 mas. 

#!pip install stargazer
from stargazer.stargazer import Stargazer
#genera codigo HTML
Stargazer([model1,model2,model3,model4]).render_html()


# Cuando hay una relacion que sube y baja hay que calcular el ^2 y restarlo .
# cuando una variable nominal tiene mas de 2 categorias tenemos que hacer 

wbr["S1"] = 0 
wbr["S2"] = 0 
wbr["S3"] = 0 
wbr["S4"] = 0 

wbr.loc[  (wbr['season'] == 1),  "S1"] = 1
wbr.loc[  (wbr['season'] == 2),  "S2"] = 1
wbr.loc[  (wbr['season'] == 3),  "S3"] = 1
wbr.loc[  (wbr['season'] == 4),  "S4"] = 1

#Cuando hacemos dummys siempre tenemos que dejar una variable fuera que actua como referencia de las demas(la mas frecuente)

model5 =ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday  + S2 + S3 + S4', data=wbr).fit()
print(model5.summary2())


model6 =ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday  + C(season)', data=wbr).fit()
print(model6.summary2())
