#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:34:48 2019

@author: salim
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #para dibujos

#-------------------------- 1- Connectarse al repertorio----------------------------------------------------

# Change working directory --> Cambiar de directorio de trabajo 
os.chdir('/Users/salim/Desktop/EDEM/Python/TRABAJO')


#----------------------------leer el fichero ------------------------------
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


os.chdir('/Users/salim/Desktop/EDEM/Python/Code')


wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')


wbr.shape
wbr.head()
#QC OK

res = turismo_bueno['temperatura'].describe()
print(res)


# store parameters as numbers 

m=res[1]
sd = res[2]
n = res[0]


#histogram ver4

x =turismo_bueno['poblacion']

plt.hist(x, bins=10, edgecolor='black')
plt.title('Figure . Histogram variable poblacion')
plt.ylabel('Frecuency')
plt.xlabel('Number of bicycles rented')
plt.xticks(np.arange(0, 10000, step=1000))


# Add reference lines and store their names in label for later legend
plt.axvline(x=m,linewidth=1,linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=m-sd,linewidth=1,linestyle= 'dashed',color="green", label='- 1 S.D.')
plt.axvline(x=m + sd,linewidth=1,linestyle= 'dashed',color="green", label='+ 1 S.D.')
plt. legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))



#--------------------------- Ejercicio2-------------------------

mpg=df_auto.loc[:, "mpg"]


mpg.describe()
#CAMBIAR de objetos a numerical. 
mpg2= mpg.apply(pd.to_numeric)
mpg2.describe()

#TUNEAR y dibujar


z = mpg2.describe()
me = mpg2.mean()
sde = mpg2.std()
ne = mpg2.count()


#Histograma variable horsepower 
plt.hist(mpg2, bins=10, edgecolor='black')
plt.title('Figure1 . Histogram variable mpg ')
plt.ylabel('Frecuency')
plt.xlabel('mpg')

#Box de numero de registros
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(ne)
plt.text (40,50, textstr , bbox=props)

# Add reference lines and store their names in label for later legend
plt.axvline(x=me,linewidth=1,linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=me-sde,linewidth=1,linestyle= 'dashed',color="pink", label='- 1 S.D.')
plt.axvline(x=me + sde,linewidth=1,linestyle= 'dashed',color="pink", label='+ 1 S.D.')
plt.legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))
plt.savefig('Histograma_MPG.jpg')

#-----------------------Ejercicio3--------------------------------


origin2 = pd.crosstab(index=df_auto["origin"], columns="count")
print(origin2)

#Percentage
#sumo todos los numeros que estan en mi tabla %
n = origin2.sum()


origin3 = (origin2/n)*100
print(origin3)
del (origin2)


#TUNEAR EL DIBUJO PONIENDO ETIQUETAS DE CAMPOS
x1 = [1]
y1 = origin3.loc[1]
x2 = [2]
y2 = origin3.loc[2]
x3 = [3]
y3 = origin3.loc[3]
#Configurar las características del gráfico
plt.bar(x1, y1, label = '62,56%', width = 0.5, color = 'lightblue')
plt.bar(x2, y2, label = '17,58%', width = 0.5, color = 'orange')
plt.bar(x3, y3, label = '19,84%', width = 0.5, color = 'green')
ax = plt.axes()
ax.text( 0.85, 30,'62.56%')
ax.text( 1.85, 8,'17.58%')
ax.text( 2.85, 10,'19.84%')
plt.xticks(origin3.index, objects) #poner objetos en cada tipo
plt.title("Figura . Origen de coches en porcentaje") #Titulo
plt.xlabel("Origen del coche")   # Establece el título del eje x
plt.ylabel("Porcentaje")   # Establece el título del eje yçplt.legend()
plt.legend()
plt.savefig('origen_auto.jpg')



