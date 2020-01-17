# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:08:04 2019
@author: Alberto Sanz
Percentage Comparison
MDA EDEM
"""
#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
#reset -f   

s


#Recoding DV for analysis
res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

### Recode cnt to string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>(m-sd)) & (wbr['cnt']<(m+sd))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>(m+sd)) ,"cnt_str"]= "High rentals"

### Recode cnt to ordinal
my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

#frequencies & barchart
mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize='columns')*100
print(mytable)
print (round(mytable,1))
plt.bar(mytable.index, mytable['count'])

#######################
# Recode  working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No","Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')



#crosstabulation
pd.crosstab(wbr.cnt_cat, wbr.wd_cat)
#normalizamos por columnas tabla de que y como consultarla ? 
pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize ="columns", margins =True)*100

#Normalize para ver la media mas o menos y ver los que estan por encima y por debajo 
my_ct=(pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize ='columns', margins =True)*100).round(1)
my_ct

my_ct = round(my_ct, 1)
my_ct 


#hacemos la prueba de chi2 para ver si las diferencias son significativas

#hacemos un crosstabulation cencillo
ct = pd.crosstab(wbr.cnt_cat, wbr.wd_cat)
ct
#prueba estatistica de chi2 , primer parametro que sale es el chi2  , el segundo es el P value el que nos interesa
stats.chi2_contingency(ct)

#hacer el grafo se usa la 2 tabla, no la que tiene los percentages


#my_ct es el cross tab y kind es el tipo de grafo que creo que me ponga
my_ct.plot(kind ='bar')   #me sale columnas por filas. tengo que cambiar, transformar la matriz (trasponer la matriz)
#me sale columnas por filas. tengo que cambiar, transformar la matriz (trasponer la matriz)
my_ct2=my_ct.transpose()
my_ct2.plot(kind='bar', edgecolor ='Black')


my_ct2.plot(kind='bar', edgecolor ='Black', colormap ='Paired')

my_ct2.plot(kind='bar', edgecolor ='Black', colormap ='Blues')

my_ct2.plot(kind='bar', edgecolor ='Black', colormap ='winter')
props = dict(boxstyle = 'round', facecolor = 'white', lw=0.5)
plt.text(-0.3, 70, 'Chi2: 498300\n''n:731' '\n' 'Pval.:0.083', bbox=props)
plt.xlabel("Working Day")
plt.title ('Figure 7. Percentage of Rental level, by Working Day. ''\n')
plt.xticks(rotation = 360)
plt.ylim(0,100)
plt.savefig('cross_tab_plot2.eps')





















#crosstabulation
o = pd.crosstab(wbr.cnt_cat, wbr.weathersit)
#normalizamos por columnas tabla de que y como consultarla ? 
o = pd.crosstab(wbr.cnt_cat, wbr.weathersit, normalize ="columns", margins =True)*100


o =(pd.crosstab(wbr.cnt_cat, wbr.weathersit, normalize ='columns', margins =True)*100).round(1)
o

o = round(my_ct, 1)
o 


#hacemos la prueba de chi2 para ver si las diferencias son significativas

#hacemos un crosstabulation cencillo
cto = pd.crosstab(wbr.cnt_cat, wbr.weathersit, normalize='columns',margins=True)*100
cto
#prueba estatistica de chi2 , primer parametro que sale es el ...  , el segundo es el P value el que nos interesa
stats.chi2_contingency(cto)

#hacer el grafo se usa la 2 tabla, no la que tiene los percentages


cto.plot(kind ='bar')   #me sale columnas por filas. tengo que cambiar, transformar la matriz (trasponer la matriz)
#me sale columnas por filas. tengo que cambiar, transformar la matriz (trasponer la matriz)
cto.T.plot(kind='bar', edgecolor ='Black')


cto.T.plot(kind='bar', edgecolor ='Black', colormap ='Paired')

props = dict(boxstyle = 'round', facecolor = 'white', lw=0.5)
plt.text(-0.8, 70, 'Chi2: 68\n''n:731' '\n' 'Pval.:0.0000', bbox=props)
plt.xlabel("Working Day")
plt.title ('Figure 7. Percentage of Rental level, by  Day. ''\n')
plt.xticks((0,1,2), ("Sunny","Cloudy","Rainy"), rotation =360)
plt.ylim(0,100)








