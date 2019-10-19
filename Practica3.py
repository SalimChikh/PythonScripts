#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:20:33 2019

@author: salim
"""


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Obtener directorio de trabajo
os.getcwd()
#Cambiar directorio de trabajo
os.chdir('/Users/salim/Desktop/EDEM/Python/Code')

#leer el dataset

dataset = pd.read_csv ("abny_pep2019.csv")
#quitar valores 

dataset1 = dataset.loc[dataset['price'] > 0]

#contar cuanto hay de cada
df_room = pd.crosstab(index=dataset1['room_type'], columns='count')

Entire = dataset1.loc[dataset1['room_type'] == 'Entire home/apt']
Entire_precio = Entire.price
a1 = Entire_precio.mean()


Shared =dataset1.loc[dataset1['room_type'] == 'Shared room']
Shared_precio = Shared.price
a2 = Shared_precio.mean()


Private = dataset1.loc[dataset1['room_type'] != 'Entire home/apt']
Private = Private.loc[Private['room_type'] != 'Shared room']
Private_precio = Private.price
a3 = Private_precio.mean()

mean = [a1, a2, a3]
#construir un data frame con mean = el vector de medias que hemos guardado antes
mean_room = pd.DataFrame({'mean':mean})
#cambiar el nombre de cada index 
mean_barrios_name = mean_room.rename(index={0: 'Entire home/apt',1: 'Private room',2: 'Shared room'})
plt.bar(mean_barrios_name.index, mean_barrios_name['mean'])
#etiquetas y guardado de grafico
plt.title("Figura 3. Average Price by room type") #Titulo
plt.xlabel("Room type")   # Establece el título del eje x
plt.ylabel("Price (US Dollar)")   # Establece el título del eje yçplt.legend()
plt.savefig('punto2.jpg')