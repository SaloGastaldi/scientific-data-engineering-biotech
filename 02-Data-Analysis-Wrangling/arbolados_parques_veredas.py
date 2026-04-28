#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:12:57 2021

@author: salo
"""
"""
#Incorporando el Arbolado lineal
#Ejercicio 8.7: Lectura y selección
import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
#seleccionamos columnas
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]
#10 especies mas frecuentes con sus respectivas cantidades
cant_ejemplares = df_lineal['nombre_cientifico'].value_counts()
cant_ejemplares.head(10)
#Seleccionamos especies
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

#Ejercicio 8.8: Boxplots
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')
#Ejemplo de pairplot
import seaborn as sns
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')

"""
#Ejercicio 8.9: Comparando especies en parques y en veredas
import pandas as pd
import os
#árboles en parques
directorio_parques = '../Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
fname_parques = os.path.join(directorio_parques,archivo_parques)
df_parques = pd.read_csv(fname_parques)
##Hacemos copia del archivo original con las filas correspondientes a las tipas y las columans de diametros y alturas
cols_parques = ['nombre_cie', 'diametro', 'altura_tot']
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parques].copy()
##Añadimos columna 'ambiente' que contiene la palabra 'parque' en todas las filas 
lista_parque = ['parque' for i in range(4031)]
df_tipas_parques['ambiente'] = lista_parque

#árboles en veredas
directorio_veredas = '../Data'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_veredas = os.path.join(directorio_veredas,archivo_veredas)
df_veredas = pd.read_csv(fname_veredas)
##Hacemos copia del archivo original con las filas correspondientes a las tipas y las columans de diametros y alturas
cols_veredas = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_veredas].copy()
##Renombramos columnas diametro y altura para que queden iguales en los dos dataframes
df_tipas_veredas = df_tipas_veredas.rename(columns={'diametro_altura_pecho': 'diametro', 'altura_arbol': 'altura_tot'})
##Añadimos columna 'ambiente' que contiene la palabra 'vereda' en todas las filas
lista_vereda = ['vereda' for i in range(9330)]
df_tipas_veredas['ambiente'] = lista_vereda



#Juntamos ambos datasets
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura_tot', by = 'ambiente')

# Pregunta 7
'''
¿Qué tendrías que cambiar para repetir el análisis para otras especies? 
Habría que cambiar el nombre de la especie cuando hacemos la seleccion de filas
y columnas a la hora de hacer la copia del dataframe.
¿Convendría definir una función?
Crear una funcion que vaya llamando tomando de a uno los nombres de las 
especies. Estas podrian darse en forma de lista como le dimos las columnas.
'''