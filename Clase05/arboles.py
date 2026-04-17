#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:05:01 2021

@author: salo
"""
#Ejercicio 4.18: Lectura de todos los árboles
#arboles.py
import csv
#from pprint import pprint
"""
def leer_parque(nombre_archivo, parque):
    arboles = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            if record['espacio_ve'] == parque:
                arboles.append(record)
    return arboles

parque_general_paz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
"""
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        arboles = [{encabezado: valor for encabezado, valor in zip(encabezados, fila)} for fila in filas]
    return arboles

"""
#Ejercicio 4.19: Lista de altos de JAcarandá
H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
pprint(H)  

#Ejercicio 4.20: Lista de altos y diámetros de Jacarandá
HD=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
pprint(HD)

#Ejercicio 4.21: Diccionario con medidas 
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
def medidas_de_especies(especies, arboleda):
    diccionario_medidas = {}
    for especie in especies:
        diccionario_medidas[especie] = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
    return diccionario_medidas

#medidas = medidas_de_especies(especies, arboleda)
#print(medidas)

# extra
def medidas_de_especies(especies, arboleda):
    d = {especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return d
medidas_extra = medidas_de_especies(especies, arboleda)
print(medidas_extra)

#Ejercicio 5.24: Histograma de altos de Jacarandás
import os
import matplotlib.pyplot as plt
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
altos = H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.hist(altos,bins=15)
"""
#Ejercicio 5.25: Scatterplot (diametro vs alto) de Jacarandás

import numpy as np
import matplotlib.pyplot as plt
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
HD=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

h = np.array(HD)[:,0]
d = np.array(HD)[:,1]
print(h)
N = len(HD)
colors = np.random.rand(N)

plt.scatter(d, h, c = colors, alpha = 0.3, s=50)


plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
plt.show()

#Ejercicio 5.26: Scatterplot para diferentes especies
import os
import numpy as np
import matplotlib.pyplot as plt

def medidas_de_especies(especies, arboleda):
    diccionario_medidas = {}
    for especie in especies:
        diccionario_medidas[especie] = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
    return diccionario_medidas

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)


#Eucalipto
h0 = np.array(medidas[especies[0]])[:,0]
d0 = np.array(medidas[especies[0]])[:,1]

N = len(medidas)
colors = np.random.rand(N)
plt.scatter(d0, h0, c = colors, alpha = 0.3, s=50)
plt.xlim(0,30) 
plt.ylim(0,100)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Eucalipto")
plt.show()

#Palo borracho rosado
h1 = np.array(medidas[especies[1]])[:,0]
d1 = np.array(medidas[especies[1]])[:,1]

N = len(medidas)
colors = np.random.rand(N)
plt.scatter(d1, h1, c = colors, alpha = 0.3, s=50)
plt.xlim(0,30) 
plt.ylim(0,100)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Palo borracho rosado")
plt.show()

#Jacaranda
h2 = np.array(medidas[especies[2]])[:,0]
d2 = np.array(medidas[especies[2]])[:,1]

N = len(medidas)
colors = np.random.rand(N)
plt.scatter(d2, h2, c = colors, alpha = 0.3, s=50)
plt.xlim(0,30) 
plt.ylim(0,100)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandá")
plt.show()
