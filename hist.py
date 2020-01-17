#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:41:00 2019

"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #para dibujos

#-------------------------- 1- Connectarse al repertorio----------------------------------------------------

# Change working directory --> Cambiar de directorio de trabajo 
os.chdir('/Users/salim/Desktop/EDEM/Python/hackaton')



turismo = pd.read_csv ('load_csv_limpio.csv', sep=';', decimal=',')

turismo_bueno = turismo[turismo.municipio > '0']




turismo.shape
turismo.head()
#QC OK

res = turismo_bueno['temperatura'].describe()

print(res)

#TUNEAR y dibujar


z = res.describe()
me = res.mean()
sde = res.std()
ne = res.count()


#Histograma variable horsepower 
plt.hist(res, bins=10, edgecolor='black')
plt.title('Figure1 . Histogram variable temperatura ')
plt.ylabel('Frecuency')
plt.xlabel('temperatura')

#Box de numero de registros
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(ne)
plt.text (40,50, textstr , bbox=props)

# Add reference lines and store their names in label for later legend
plt.axvline(x=me,linewidth=1,linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=me-sde,linewidth=1,linestyle= 'dashed',color="pink", label='- 1 S.D.')
plt.axvline(x=me + sde,linewidth=1,linestyle= 'dashed',color="pink", label='+ 1 S.D.')
plt.legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))






essaie_tempe=turismo_bueno.loc[:, "temperatura"]


essaie_tempe.describe()

#TUNEAR y dibujar


z = essaie_tempe.describe()
me = essaie_tempe.mean()
sde = essaie_tempe.std()
ne = essaie_tempe.count()


#Histograma variable horsepower 
plt.hist(essaie_tempe, bins=10, edgecolor='black')
plt.title('Figure1 . Histogram variable temperatura ')
plt.ylabel('Frecuency')
plt.xlabel('temperatura')

#Box de numero de registros
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(ne)
plt.text (40,50, textstr , bbox=props)

# Add reference lines and store their names in label for later legend
plt.axvline(x=me,linewidth=1,linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=me-sde,linewidth=1,linestyle= 'dashed',color="pink", label='- 1 S.D.')
plt.axvline(x=me + sde,linewidth=1,linestyle= 'dashed',color="pink", label='+ 1 S.D.')
plt.legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))