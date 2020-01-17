#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:08:53 2019

@author: Salim Chikh
Clase 1 sesion 2
Reading external data ("washington bike")
"""
#load basic libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #para dibujos



#-------------------------- 1- Connectarse al repertorio----------------------------------------------------

# Change working directory --> Cambiar de directorio de trabajo 
os.chdir('/Users/salim/Desktop/EDEM/Python/Code')
os.getcwd() #despues de cambiar de directorio verificamos si se ha hecho bien

#------------------------- 2- Importar Fichero a leer----------------------------------------------------------------
#leeeme el fichero ..... que esta separado por ; donde las decimales son , en el working directory
rentals_2011 = pd.read_csv ("washington_bike_rentals_2011.csv", sep=';', decimal =',')


#------------------------ 3- Effectuar el CONTROL DE CALIDAD --------------------------------------------------------------

#para verificar las dimenciones (en funcion de lo que lleva el interior de nuestro fichero es un control de calidad)
rentals_2011.shape 

#Que me muestre la cabezera del fichero  // nombre del fichero. head()
rentals_2011.head()
#Que me muestre el final del fichero  // nombre del fichero. tail()
rentals_2011.tail()
#QC ---> OK

#------------------------4 - Analizar el DataFrame-------------------------------------------------------------------

#--------------------------------Teoria IMPORTANTE---------------------------------------------
#para describir una variable nominal % y graficos de barras
#Para describir variables ordinal como nominales, 
#Para describir variables cuantitativas (media y desviación tipica,histograma)
# la logica que hay que seguir -> que tipo de variables es ? cuantitativa ... entonces media, desviacion tipica)


#Seleccionar la variable que queremos mostrar en una variable, 
#loc -> localizame, : para seleccionar todos los casos de la columna "cnt" 
x=rentals_2011.loc[:, "cnt"]

#Plot dibujar
plt.hist(x)
#Media mean, y descripción std
x.describe()




#Load data from Excel para ver la diferencia con el CSV y la diferencia es el formato de los campos en este caso ha sido fecha
rentals_2011b = pd.read_excel ("washington_bike_rentals_2011.xlsx")
y = rentals_2011b
y.shape
y.head ()
del (y)
del (x)
del (rentals_2011b)


#-------------------LEER UN FICHERO DE TIEMPO PARA DESPUES CRUZARLO-------------------------
#-----------------------leer el fichero-------------------------------------------------
weather_2011 = pd.read_csv ("weather_washington_2011.csv", sep= ';', decimal=',')

#------------------------Control de calidad otra vez--------------------------------------
weather_2011.shape
weather_2011.head ()

#dtypes nos dice el tipo de datos
weather_2011.dtypes

#despues de elegir cual es la variable a usar en este caso ha sido temperatura porque es cuantitativo 

x=weather_2011.loc[:, "temp_celsius"]
plt.hist(x, edgecolor ='black')
x.describe()
plt.show()
del (x)



#------------------------------------------Vamos a juntar los 2 DataSet------------------------------
#--------Hay que ver si tenemos el mismo numéro de Dias para poder coincidir dos dataset hay que tener una variable en commun----------------------------------
#EL NUEVO DATA SET ES EL MERGE ENTRE EL PRIMERO Y EL SEGUNDO JUNTADOS POR LA COLUMNA DIA
rentals_weather_2011 =pd.merge(weather_2011, rentals_2011, on="day")

#--------------------------------------------controle de calidad-------------------------------------------
rentals_weather_2011.shape
rentals_weather_2011.head()

#--------------como el campo fecha existe 2 veces nos creo un fichero con columna day_X y day_y hay que borrar uno-----------


#PARA BORRAR UNA VARIABLE HAY QUE USAR EL COMANDO DROP 

rentals_weather_2011 = rentals_weather_2011.drop(columns=['dteday_y'])

#Despues cambiamos el nombre de la columna que queda 
rentals_weather_2011 = rentals_weather_2011.rename (columns={"dteday_x": "dteday"})

#dibujar x y scatterplot 
plt.scatter(rentals_weather_2011.temp_celsius, rentals_weather_2011.cnt)


#---------------------otro fichero de 2012---------------------------

rentals_weather_2012 = pd.read_csv ("rentals_weather_2012.csv", sep= ';', decimal=',')

#controle de calidad
rentals_weather_2012.shape
rentals_weather_2012.head ()

# para comparar entre dos ficheros antes de trabajar con ellos 

rentals_weather_2011.shape == rentals_weather_2012.shape

print("Equal dimensions ?:" , rentals_weather_2011.shape == rentals_weather_2012.shape)

#JUNTAR LOS DOS FICHEROS
rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012)

#controle quality
print (rentals_weather_11_12.shape)
print (rentals_weather_11_12.head())
print (rentals_weather_11_12.tail())

#nos damos cuenta de que el indice se repite no sabe que es unico
#Decir cual es el campo que no se tiene que repetir
rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012,ignore_index=True)
#Volver a verificar 
print (rentals_weather_11_12.shape)
print (rentals_weather_11_12.head())
print (rentals_weather_11_12.tail())

#VAMOS A VOLVER A RESTAURAR EL ORDEN ORIGINAL DEL FICHERO siguiendo el orden del fichero 2011

rentals_weather_11_12 = rentals_weather_11_12[rentals_weather_2011.columns]

#LO PRIMERO QUE TENEMOS QUE HACER ES 1- CARGAR LOS FICHEROS 
#-2 ES MIRAR CUALES SON LAS VARIABLES COMO EL INDEX QUE TIENE QUE SER UNICOS 
#-3 MIRAR SI HAY CAMPOS DUPLICADOS (RENOMBRAR Y BORARAR)
#-4 REORDENAR LOS CAMPOS 

