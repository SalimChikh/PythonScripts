# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

3
3+2

a = 3
print (a)

b=2
print (b)
c=a+b
print (c)
#del es para borrar del DELETE
del (a)
del (b,c)


a="Good Morning"
b= "Vientam"


print (a)
print (b)
c=a+b
print (c)
d=a+" "+b


#reset ALL. carefull. This is as "magic" comand it runs only on the console es para borrar todo
#%reset -f

#load basic libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #para dibujos

#Create a dataframe for the class
name = ["Miguel", "Marta", "Pau", "Alberto", "Diego", "Jose"]
age=[44,32,22,25,27,34]
gender=["male", "female","male","male","male","male"]
nat=["ES","ES","ES","ES","ES","ES"]

print (name, age, gender, nat)

#Construir el DataFrame
class_2019 = pd.DataFrame({'name': name, 'age': age, 'gender': gender, 'nat': nat})

#Clean up 
del (age,gender,name,nat)

