#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:49:44 2021

@author: salo
"""
import datetime

fecha_y_hora = datetime.datetime.now()
print(fecha_y_hora)
repr(fecha_y_hora)
#%%
datetime.datetime(2020,9,21)
datetime.datetime(2020,9,21,12,30)
print(datetime.datetime(2020,9,21,12,30,45,10))

#%% Relación con strings

#imprimir como quiera
datetime.datetime.now().strftime('Son las %H horas, %M mintos, %S segundos')

#leer con formato
cadena_con_fecha= '21 September, 2021'
object_fecha = datetime.datetime.strptime(cadena_con_fecha, '%d %B, %Y')
print('objeto_fecha =', object_fecha)

#leer con formato
cadena_con_fecha= '2020 # 09 # 30'
object_fecha = datetime.datetime.strptime(cadena_con_fecha, '%Y # %m # %d')
print('objeto_fecha =', object_fecha)

#%%
#Atributos de la clase datetime
fecha_y_hora.year
fecha_y_hora.month
fecha_y_hora.day
'''
La clase datetime es algo que tiene un dato(año, mes, dia, cantidad de horas, cantidad de minutos, cantidad de segundos).
Pero además tiene metodos de funciones asociadas: 
Por ejemplo esta primera tiene "fecha_y_hora". 
"year" "month" "day", es un atributo que tiene la clase.
'''
# métodos de la clase datetime
#(año, semana, dia)
fecha_y_hora.isocalendar()
'''
isocalendar es una funcion que a partir de los atributos que tiene el objeto, calcula año, semana(18), dia de la semana(3=miercoles)
'''
#el número de segundos transcurridos desde el primero de enero de 1970 hasta hoy, es un numero gigante!
fecha_y_hora.timestamp()  

#%%

#Time deltas
parcial_inicio = datetime.datetime(2020,9,16,14)
parcial_fin = datetime.datetime(2020,9,16,15,30)

duracion = parcial_fin - parcial_inicio
print(duracion)
repr(duracion)
'''
la representacion es algo que si lo evalúo me devuelve un objeto. (0 minutos, 5400 segundos)
'''
duracion.total_seconds()
#%%
import os
for root, dirs, files in os.walk("ordenar"):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))  
      
#%%    
########################
# PARTE 3 ### Pandas ###
########################
import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

#Caminatas al azar
import numpy as np
idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()
s2.plot()
#Media movil para suavizar los datos
w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()
s3.plot()
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()


#Ejemplo: 12 personas caminando 8 horas
horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()
#suavizamos los datos, usando min_periods para no perder los datos de los extremos
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()
df_walk_suav.to_csv('caminata_apostolica.csv')
