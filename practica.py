#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:37:48 2019

@author: salim
@Practica 
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #para dibujos

#-------------------------- 1- Connectarse al repertorio----------------------------------------------------

# Change working directory --> Cambiar de directorio de trabajo 
os.chdir('/Users/salim/Desktop/EDEM/Python/Code')


#----------------------------leer el fichero de 2011------------------------------
rentals_2011 = pd.read_csv ("washington_bike_rentals_2011.csv", sep=';', decimal =',')

#-------------------------------Controle de calidad--------------------------------

#para verificar las dimenciones (en funcion de lo que lleva el interior de nuestro fichero es un control de calidad)
rentals_2011.shape 

#Que me muestre la cabezera del fichero  // nombre del fichero. head()
rentals_2011.head()
#Que me muestre el final del fichero  // nombre del fichero. tail()
rentals_2011.tail()
#QC ---> OK

x=rentals_2011.loc[:, "workingday"]


x.describe()

#Plot dibujar
plt.hist(x)
# Hay que ver el tipo de variable, es nominal entonces porcentage.

#Media mean, y descripción std
#Percentage

#CREAR PORCENTAGE
#CREAR UNA TABLA , QUE QUIERO ANALIZAR ? COLUMNA WEATHERSIT COMO TIENE QUE LLAMARSE LA COLUMNA -> COUNT
mytable = pd.crosstab(index=rentals_2011["workingday"], columns="number_of_days_off_on")
#sumo todos los numeros que estan en mi tabla %
n = mytable.sum()
mytable2 = (mytable/n)*100


mytable2.describe()

#representar en tabla pintar barplot --> Grafico de barras // aqui porqué ? 
plt.bar(mytable2.index, mytable2['number_of_days_off_on'], color ='Red')

#TUNEAR EL DIBUJO PONIENDO ETIQUETAS DE CAMPOS
#BARCHART decir como llamar y en que campo 
#objects = ('DayOff', 'WorkingDay')
#AQUI LE DECIMOS CUAL SE TENDRÁ QUE COGER COMO INDICE
plt.bar(mytable2.index, mytable2['number_of_days_off_on'])
plt.xticks(mytable2.index, objects)
plt.show()
plt.bar(mytable2.index, mytable2["number_of_days_off_on"], edgecolor="black")


objects= ('DAY OFF','WorkingDay')
plt.xticks(mytable2.index, objects)
plt.ylabel ("Percentage")
#plt.xlabel ("Figure 1. Percentage of DAY OFF/ON")
plt.title ("Figure 1. Percentage of DAY OFF/ON")





z=rentals_2011['cnt']
# plot
plt.hist(z, edgecolor='black')

#saltos de 1000 para ordenar abajo 
plt.xticks(np.arange(0, 10000, step=1000))
plt.xticks(ticks)
#plt.title('Figure 1.Daily Bicycle rentals in washington DC ' '\n' 'by Capital bikeshar')
plt.ylabel('Frecuency')
plt.xlabel('Number of rented bicycles')

#ADD DESCRIPTIVE  guardandolo en una variable para poder despues acceder en ello



plt.hist(x, bin=10, edgecolor ='black')
plt.xticks(np.arange(0,))

rentals_weather_2012 = pd.read_csv ('rentals_weather_2012.csv', sep=';', decimal=',')

weather_2011 = pd.read_csv ('weather_washington_2011.csv', sep=';', decimal=',')

rentals_weather_2011 = pd.merge(weather_2011, rentals_2011, on='day')
rentals_weather_2011 = rentals_weather_2011.drop(columns=['dteday_y'])


rentals_weather_2011.to_csv('rentals_weather_2011.csv')

rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012, ignore_index=True)

rentals_weather_11_12.to_csv('rentals_weather_11_12.csv')
