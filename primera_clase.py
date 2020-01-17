# -*- coding: utf-8 -*-
"""
@Author: Salim Chikh
14/09/2019
First class 
"""

3
3+2

a = 3
print (a)

b=2
print (b)
c=a+b
print (c)
#del --> es para borrar del DELETE
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

#Get working directory --> para ver donde estoy trabajando 
os.getcwd()

# Change working directory --> Cambiar de directorio de trabajo 
os.chdir('/Users/salim/Desktop/EDEM/Python/Code')
os.getcwd() #despues de cambiar de directorio verificamos si se ha hecho bien

# Save dataframe to Excel 
class_2019.to_excel("class2019.xlsx") #que dataFrame quieres guardar a que formato y como
class_2019.to_csv("class2019.csv")

print(class_2019.age)

class_2019.age.describe() #dame las estatisticas descriptivas, todas

plt.hist(class_2019.age) #dibujo un histograma de edad de mi DataFrame

%reset -f
