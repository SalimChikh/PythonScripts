#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:37:18 2019

@author: Salim Chikh
Clase 1 sesion 2
Reading external data ("washington bike")
"""
#load basic libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #para dibujos

#Simplificar el nombre de DataFrame

wbr=rentals_weather_11_12
del (rentals_weather_11_12)


#CREAR PORCENTAGE
#CREAR UNA TABLA , QUE QUIERO ANALIZAR ? COLUMNA WEATHERSIT COMO TIENE QUE LLAMARSE LA COLUMNA -> COUNT
mytable = pd.crosstab(index=wbr["weathersit"], columns="count")
print(mytable)

#Percentage
#sumo todos los numeros que estan en mi tabla %
n = mytable.sum()
n

mytable2 = (mytable/n)*100
print(mytable2)
del (mytable)


#representar en tabla pintar barplot --> Grafico de barras
plt.bar(mytable2.index, mytable2['count'])

#TUNEAR EL DIBUJO PONIENDO ETIQUETAS DE CAMPOS
#BARCHART decir como llamar y en que campo 
objects = ('Sunny', 'Cloudy', 'Rainy')
plt.bar(mytable2.index, mytable2['count'])
plt.xticks(mytable2.index, objects)
plt.show()

#BARCHART2 
#AQUI LE DECIMOS CUAL SE TENDRÁ QUE COGER COMO INDICE
plt.bar(mytable2.index, mytable2["count"], edgecolor="black")
objects= ("Sunny", "Cloudy", "Rainy")
plt.xticks(mytable2.index, objects)
plt.ylabel ("Percentage")
plt.xlabel ("Different weather situations")
plt.title ("Figure 1. Percentage of weather conditions")

#plt.text(2.5,50, "n=731") #2.50 y 50 son las coordenadas donde quieres ubicar

#plt.show() for separating the charts, if not will delete the previous one and replace

######Extra tip: Adding legend of n (replacing plt.text)
props=dict(boxstyle="round", facecolor="white", lw=0.5)
textstr="$\mathrm{n}=%.0f$"%(n)
plt.text (3,60, textstr, bbox=props)


#guardar imagen 
plt.savefig('bar_centro.eps')
plt.savefig('bar_centro.jpg')



#OTRO BARRAS
x=wbr['cnt']
# plot
plt.hist(x, edgecolor='black')

#saltos de 1000 para ordenar abajo 
plt.xticks(np.arange(0, 10000, step=1000))
plt.xticks(ticks)
plt.title('Figure 1.Daily Bicycle rentals in washington DC' '\n' 'by Capital bikesha)
plt.ylabel('Frecuency')
plt.xlabel('Number of rented bicycles')

#ADD DESCRIPTIVE  guardandolo en una variable para poder despues acceder en ello

res = wbr['cnt'].describe()

res[1]
#para redondear con un decimal
print(round (res[1,1]))

m = res[1]
sd = res [2]
n res[0]


plt.hist(x, bin=10, edgecolor ='black')
plt.xticks(np.arange(0,))



#BORRAR LINEAS QUE TIENEN ? DENTRO DEL FICHERO df_auto y el nombre de la columna horsepower


df_auto2 = df_auto.loc[df_auto['horsepower'] != '?']
