# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:00:29 2019

@author: alber
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# New libraries
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import scipy.stats as stats  # For statistical inference 
import seaborn as sns  

os.getcwd()
os.chdir('C:/Users/alber/Desktop/Master_Data_Analytics/Asignaturas/Fundamentos/Python/code_and_data/data')


#BASIC LOOP

 for i in range(0,11,1): #desde 0 hasta 10 (python empieza en 0)
    print("i:",i)
    
#BASIC LOOP II
    
for i in [1,2,3,4]: #la iteración considera todos los valores de i (de la lista)
    print("i:",i)

#BASIC LOOP III
for i in ["red","blue","yellow"]:#break --> puede romper un BUCLE
    print(i)
    
#BASIC LOOP IV
    
for i in range (10,-1,-1):#descenso de 10 a 0 de 1 en 1
    print("i:",i)  
    
for i in range (50,-1,-5): #descenso de 50 a 0 de 5 en 5
    print("i:",i)  
    
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
x =wbr['cnt']
plt.hist(x, bins=10, edgecolor='black')
plt.title('Figure . Histogram variable cnt')
plt.ylabel('Frecuency')
plt.xlabel('Number of bicycles rented')

#PLOTEAR 50 HISTOGRAMAS CAMBIANDO el numero de bins y mostrando el numero de barras

for i in range (1,51,1):

    x =wbr['cnt']
    plt.hist(x, bins=i, edgecolor='black')
    plt.show()
    print(i)

for i in range (50,101,1): #ploteamos de 50 bins a 100

    x =wbr['cnt']
    plt.hist(x, bins=i, edgecolor='black')
    plt.show()
    print(i)

#TAREA PARA CASA
wbr.iloc[6:17] #explorar iloc --> plotear scatters de todas las variables cuantitativas contra la variable dependiente (cnt) -->primero habra que hacer un subset de solo las variables cuantitativas y ya crear el bucle
 
#Mostrar las notas y a que corresponden
 
for i in range (0,11,1):
    if i < 5:
        grade="Fail"
    else:
        grade="Pass"
    print(" My grade is ", i,":", grade)
    
    
#Lo mismo ahora solo con IFS sin el ELSE
    
for i in range (0,11,1):
    
    if i < 5:
        grade="Fail"
        
    if i>= 5:
        grade="Pass"
    print(" My grade is ", i,":", grade)


#dividir en diferentes notas
    
for i in range (0,11,1):
    
    if i < 5:
        grade="Fail"
        
    if 5 <= i < 7:
        grade="Pass"
        
    if 7 < i < 10:
        grade="Excellent"
    print(" My grade is ", i,":", grade)

#si pones el print al principio solo imprimiria el ultimo caso al pasar por todo el bucle sin printear nada
print(" My grade is ", i,":", grade)
for i in range (0,11,1):
    
    if i < 5:
        grade="Fail"
        
    if i>= 5:
        grade="Pass"

#funcion que suma los dos numeros que metas

def plus(a,b): #Aqui se define la funcion
    print("lets add these two numbers...")
    return a + b

plus(5,4) #aplica la funcion

addition= plus(5,4) #aqui en este caso ha guardado la accion (el output) en una variable (addition)

print("they add up to...",addition)

 #el orden de los productos afecta el resultado final depende de la funcion
 
def dividir(a,b): #Aqui se define la funcion
    print("lets add these two numbers...")
    return a / b

dividir(10,5)
dividir(5,10)

dividir(b=5,a=10) #al etiquetar los argumentos al realizar la funcion los hace en el orden alfabetico de la etiqueta (esto ha sido etiquetar los parametros)

dividir(10)#falta darle un argumento 
#pero si por defecto consideramos que b =2 si que podemos dividir por un numero
#definimos parametros por DEFECTO
def dividir(a,b=2): #Aqui se define la funcion
    print("lets add these two numbers...")
    return a / b

dividir(10)
dividir(8)
dividir(8,3)

