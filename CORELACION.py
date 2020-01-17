#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:23:33 2019
Mean comparison
@author: salim
"""

#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 


os.chdir('/Users/salim/Desktop/EDEM/Python/Code')
#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK

#histogram ver4

x =wbr['cnt']


x =wbr.temp_celsius # select the variables  cuando sube la temperatura entonces temperatura x 
y=wbr.cnt #select the variables la consecuencia siempre 

#tenemos nuestro primero scat
plt.scatter (wbr.temp_celsius, wbr.cnt)
plt.xlabel('Temperature')
plt.ylabel('Daily Rentals')

#Correlation 
#importamos personr from stats 
from scipy.stats.stats import pearsonr 
# coeficiente de corelacion y p value.
res = pearsonr(x,y)

print (res)

r = res[0]
p_val = res[1]
#cuantas veces esta repitido (longitude de ...)
n = len (wbr.cnt)


print ('r:', round(r,3) ,'P.Val:', round(p_val,3), 'n:', n)
# hay una relacion fuerte porque 0.6 y muy significativa porque p value 0.0 

#attribucion doble r1 coge x y coge p_val1
r1, p_val1 = pearsonr(x,y)
print (r1,p_val1)


#graf
#talla del grafo
plt.figure (figsize=(5,5))
#tabla que sale dentro del grafo 
plt.scatter(x,y, s=30, facecolors='none', edgecolors= 'c0')

#plt.xticks(np.arrange(0, 11, step =1))
plt.yticks(np.arange(0, 10000, step =1000))
plt.title ('Figure 9. Daily bicycle rentals, by temperature.''\n')
plt.xlabel('Temperature Centigrades')
plt.ylabel('Daily Rentals')

props = dict (boxstyle= 'round', facecolor ='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3, 7500, textstr , bbox=props)
plt.show()

#cambia el color en funcion del campo yr
plt.scatter ('temp_celsius', 'cnt',data=wbr,c=wbr.yr)
#sceaborn
sns.scatterplot(x = 'windspeed_kh', y = 'cnt',  data =wbr)

#subset  para hacerlo por cada año 

wbr_2011 = wbr[wbr.yr == 0] 
wbr_2012 = wbr[wbr.yr == 1] 


#calcular por 2011
x_2011=wbr_2011.temp_celsius.round(1) # select the variables  cuando sube la temperatura entonces temperatura x 
y_2011=wbr_2011.cnt

res_2011 = pearsonr(x_2011,y_2011)

print (res_2011)

r_2011 = res_2011[0]
p_val_2011 = res_2011[1]


#calcular por 2012
x_2012=wbr_2012.temp_celsius.round(1) # select the variables  cuando sube la temperatura entonces temperatura x 
y_2012=wbr_2012.cnt

res_2012 = pearsonr(x_2012,y_2012)

print (res_2012)

r_2012 = res_2012[0]
p_val_2012 = res_2012[1]

#DIBUJO


#graf
#talla del grafo
plt.figure (figsize=(7,7))
#tabla que sale dentro del grafo 
plt.scatter(x_2011,y_2011, s=30, facecolors='none', edgecolors= 'c0')
plt.scatter(x_2012,y_2012, s=50, facecolors='none', edgecolors= 'C0')
#plt.xticks(np.arrange(0, 11, step =1))
plt.yticks(np.arange(0, 10000, step =1000))
plt.title ('Figure 10. Daily bicycle rentals, by temperature.''\n')
plt.xlabel('Temperature Centigrades')
plt.ylabel('Daily Rentals')

props = dict (boxstyle= 'round', facecolor ='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r_2011, p_val_2011, n/2)
textstr2 = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r_2012, p_val_2012, n/2)
plt.text (3, 7500, textstr , bbox=props)
plt.text (30, 10, textstr2 , bbox=props)
plt.show()