#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:16:25 2019

@author: salim
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:23:42 2019

@author: salim
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


os.chdir('/Users/salim/Desktop/EDEM/Python/Code')


wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')


wbr.shape
wbr.head()
#QC OK

res = wbr['cnt'].describe()
print(res)


# store parameters as numbers 

m=res[1]
sd = res[2]
n = res[0]


#histogram ver4

x =wbr['cnt']

plt.hist(x, bins=10, edgecolor='black')
plt.title('Figure . Histogram variable cnt')
plt.ylabel('Frecuency')
plt.xlabel('Number of bicycles rented')
plt.xticks(np.arange(0, 10000, step=1000))


# Add reference lines and store their names in label for later legend
plt.axvline(x=m,linewidth=1,linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=m-sd,linewidth=1,linestyle= 'dashed',color="green", label='- 1 S.D.')
plt.axvline(x=m + sd,linewidth=1,linestyle= 'dashed',color="green", label='+ 1 S.D.')
plt. legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))





#round es para redondear a solo 1 digito y definimos cuales son los puntos de cortes media - deviacion tipica
print ('Low limit : ', round (m-sd,1))
print ('Mean', m)
print ('Upper limit : ', round (m+sd,1))
# los guardo en variables 
pc1 = round (m-sd,1)
pc2 = round (m+sd,1)

#Crear nueva fila cnt_cat dentro del dataset donde todos los casos son low rentals 
 #wbr["cnt_cat"] = "low rentals"
 
# .loc es las filas si no ponemos .loc va a las columnas => en la columna cnt_cat para todas las filas pon low rentals 
 # wbr.loc[:,"cnt_cat"] = "low rentals"


#en las filas cnt del wbr que estan por debajo del ... escribe low rentals en la columna cnt_cat2
#definir los campos RECODIFICACION
wbr.loc[wbr['cnt'] < pc1 ,"cnt_cat2"] = "1: low rentals"
wbr.loc[(wbr['cnt']> pc1) & (wbr['cnt']< pc2) ,"cnt_cat2"] = "2: Average"
wbr.loc[wbr['cnt'] > pc2 ,"cnt_cat2"] = "3: High rentals"


#controle de calidad
wbr.loc[wbr['cnt'] < pc1 ,"cnt_cat3"] = 1
wbr.loc[(wbr['cnt']> pc1) & (wbr['cnt']< pc2) ,"cnt_cat3"] = 2
wbr.loc[wbr['cnt'] > pc2 ,"cnt_cat3"] = 3

plt.scatter(wbr.cnt, wbr.cnt_cat3)



#contar cuanto hay de cada  // frequency 
Mytable = pd.crosstab (index=wbr["cnt_cat2"], columns="count")
print(Mytable)

#total
n = Mytable.sum()
n
#porcentaje 
mytable2 = (Mytable/n)*100
print(mytable2)
#dibujar
plt.bar(mytable2.index, mytable2['count'], color='blue')



#recodificar en 4 categorias iguales
wbr['cnt'].describe()

q1 = res[4]
q2 = res [5]
q3 = res [6]

wbr.loc[wbr['cnt'] <= q1 ,"cnt_cat4"] = "Low Rentals"
wbr.loc[(wbr['cnt']>= q1) & (wbr['cnt']<= q2) ,"cnt_cat4"] = "Average Low"
wbr.loc[(wbr['cnt']>= q2) & (wbr['cnt']<= q3) ,"cnt_cat4"] = "Average High"
wbr.loc[wbr['cnt'] >= q3 ,"cnt_cat4"] = "High Rentals"

#controle quality


plt.scatter(wbr.cnt, wbr.cnt_cat4)
#contar cuanto hay de cada  // frequency 
Mytable5 = pd.crosstab (index=wbr["cnt_cat4"], columns="count")
print(Mytable5)

#total
n = Mytable5.sum()
n
#porcentaje 
mytable6 = (Mytable5/n)*100
#dibujar
plt.bar(mytable6.index, mytable6['count'], color='red')

#CATEGORICAL CON OTRAS 

