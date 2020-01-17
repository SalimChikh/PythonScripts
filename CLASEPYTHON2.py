##import os
#import pandas as pd
#import numpy as np #numeric python
#import matplotlib.pyplot as plt #para dibujos

#os.chdir('/Users/salim/Desktop/EDEM/Python/Code')
#wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal =',')

#wbr.shape
#wbr.head()
#QC OK 



#x=wbr["cnt"]



#para me pinte donde quiero, en 1000 2000 3000 .... 
#plt.xticks([0, 1000,2000,3000,4000])
#calculame desde 0 hasta 10 000 con saltos de 1000
#ticks=np.arange(0,11000,1000)

#plt.hist(x,edgecolor = 'Black')
#ticks=np.arange(0,10000,1000)
#plt.xticks(ticks)


#histogram figure 1
#plt.hist(x, bins=10, edgecolor ='black')
#plt.xticks(np.arange(0, 10000, step=1000))
#plt.title("Figure1 . ......")
#plt.ylabel("Frecuency")
#plt.xlabel("Number of rented bycicles")


#res = wbr['cnt'].describe()

#res[1]
#print(round(res[1],1))


#store parameters as numbers 

#m=res[1]
#sd = res[2]
#n = res[0]



#Cargar librerías básicas
#Utilizar abreviatura estandar, panda es pd
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Obtener directorio de trabajo
os.getcwd()
#Cambiar directorio de trabajo
os.chdir('/Users/salim/Desktop/EDEM/Python/Code')

#Lectura del fichero, ver antes la configuracion en un fichero plano
wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')


wbr.shape
print(wbr.tail())
#QC OK

x=wbr['cnt']

hp_auto = x

d = hp_auto.describe()
m = hp_auto.mean()
sd = hp_auto.std()
n = hp_auto.count()

#Histograma variable horsepower 
plt.hist(hp_auto, bins=10, edgecolor='black')
plt.title('Figure . Histogram variable cnt')
plt.ylabel('Frecuency')
plt.xlabel('Number of bicycles rented')
plt.xticks(np.arange(0, 10000, step=1000))


# Add reference lines and store their names in label for later legend
plt.axvline(x=m,linewidth=1,linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=m-sd,linewidth=1,linestyle= 'dashed',color="green", label='- 1 S.D.')
plt.axvline(x=m + sd,linewidth=1,linestyle= 'dashed',color="green", label='+ 1 S.D.')
plt. legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))
plt.savefig('Histograma_wbr_0310.jpg')


#Box de numero de registros
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (7700,90, textstr , bbox=props)
plt.savefig('Histograma_wbr_0310.jpg')




#clean up
del(m,n,props,res,sd,textstr,x,ticks)
del(d)
del(hp_auto)


x=wbr['cnt']
plt.boxplot(x)



#Detectar casos atipicos mediante la visualización de un boxplot
plt.boxplot(x, patch_artist=True, vert=False, labels=['# rentals'])
plt.xticks(np.arange(0, 10000, step=1000))




#---------------------SECTION4---------------------

#cuentame cuatas hay de la variable year tengo dias con yr = 0 y dias con yr =1
mytable=pd.crosstab(index=wbr["yr"], columns="count")
print(mytable)
del (mytable)


#separarlo  subset year = 0 creame un data set a partir del data set wbr donde coges todos los casos donde  yr  es igual a 0 

wbr_2011 = wbr[wbr.yr == 0]


wbr_2012 = wbr[wbr.yr == 1]


#exercise, describe bike rentals in the  winter  of 2012  & AND 

wbr_2012_winter = wbr[(wbr.yr ==1) & (wbr.season == 1)]
wbr_2012_winter.shape


plt.hist(wbr_2012_winter.cnt)
wbr_2012_winter.cnt.describe()

#como seleccionar variables

my_vars = ['temp_celsius', 'cnt']

#EXTRAIGO DE WBR MIS VARIABLES y lo guardo en WBR MINIMALS ( para limpiar dataframe)

wbr_minimals=wbr[my_vars]
wbr_minimals.shape
#para generarlo 
wbr_minimals.to_csv('wbr_edem2019.csv')

wbr.to_csv('wbr_edem2019_b.csv', sep=';', decimal=',')

wbr.to_excel("wbr_edem2019_c.xlsx")

# reset -f reset all funciona solo en la consola 


wbr_ue = pd.read_csv("wbr_ue.csv", sep=';', decimal=',')
wbr_ue.describe()
#sacar la media de la temperatura 
wbr_ue.temp_celsius.describe()[1]


plt.hist(wbr_ue.temp_celsius)

#el boxplot nos permite verificar si nuestro dataset esta bien 
plt.boxplot(wbr_ue.temp_celsius)

#vamos a limpiar la variable temperatura creo otra variable _C donde cojo los datos del dataframe original y remplazo los 99 por not a number
wbr_ue['temp_celsius_c']=wbr_ue.temp_celsius.replace(99,np.nan)
wbr_ue.temp_celsius_c.describe()[1]
#borrar los na 
plt.hist(wbr_ue.temp_celsius_c.dropna())
plt.hist(wbr_ue.temp_celsius_c)
plt.boxplot(wbr_ue.temp_celsius_c)

