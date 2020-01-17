#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:06:11 2019

@author: salim
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


xg_data = pd.read_csv ("https://raw.githubusercontent.com/twhelan22/python-for-fantasy-football/master/1%20-%20Introduction/epl_xg.csv", sep=',', decimal ='.')
del(xG_data)
xY_data=xG_data
#crear una nueva columna goal difference = goals - goals contra (against)
xg_data['GD'] = xg_data['G'] - xg_data['GA']
#Crear una nueva columna goal difference expected 
xg_data['xGD'] = xg_data['xG'] - xg_data['xGA']
#Crear otra 
xg_data['NPxGD'] = xg_data['NPxG'] - xg_data['NPxGA']
xg_data
#leer las columnas 
print(list(xg_data))

#estamos guardando todas las columnas en una variable para despues recorrelos
cols = ['G', 'GA', 'xG', 'xGA', 'NPxG', 'NPxGA', 'GD', 'xGD', 'NPxGD']
#Le esta diciendo para todas las columnas creame una columna que se llame la columna con pg %s por ser un string, hacer cada columna dividido por partido 
for col in cols:
    xg_data['%s_pg' % col] = xg_data[col]/xg_data['Games']
xg_data


# leer otro fichero (el de jornada)
fixtures = pd.read_csv('https://raw.githubusercontent.com/twhelan22/python-for-fantasy-football/master/2%20-%20Matchup%20Adjustment/epl_fixtures.csv')
fixtures
#Cambiar el nombre de una columna 
fixtures = fixtures.replace('Wolves', 'Wolverhampton Wanderers')
fixtures

#creamos otro fichero sobre el cual nos quedamos con las 3 columnas que nos interesa
xg_data_pg = xg_data[['Team', 'xG_pg', 'xGA_pg']]


#merge de dos ficheros donde le decimos cual se pone por la izquierda y cual por la derecha de la primera columna
#left_on te permite ponerlo primero por la izquierda y lo coge de referencia para aplicar sus caracteristicas 
fixtures = pd.merge(fixtures, xg_data_pg, left_on='Home_Team', right_on='Team')
fixtures


fixtures = pd.merge(fixtures, xg_data_pg, left_on='Away_Team', right_on='Team')
fixtures

fixtures = fixtures.drop(['Team_x', 'Team_y'], axis=1)
fixtures





