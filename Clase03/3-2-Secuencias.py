#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:21:01 2021

@author: salo
"""
"""
a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
del a[2:4]
print(a)
"""
#%%
"""
s = [1, 2, 3, 4]
print(sum(s))
print(min(s))
print(max(s))
t = ['Helllo', 'World']
print(max(t))
"""
#%%
"""
s = [1, 4, 9, 16]
for i in s:
    print(i)
    
"""
#%%
"""
for i in range(100):
    print(i)
"""
"""
for j in range(10,20):
    print(j)
"""
"""
for k in range(10,50,2):
    print(k)
"""    
#%% Tuplas y ciclos for
"""
points = [
    (1,4),(10, 40),(23, 14),(5, 6),(7,8)
]
for x, y in points:
    print(x,y)
"""
#%% La funcion zip()
"""
columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1]
pares = zip(columnas, valores)
for columna, valor in pares:
    print(columna, valor)

d = dict(zip(columnas, valores))
print(d)
"""     
#%% Ejercicio 3.6: Contar
"""
for n in range(10):
    print(n, end=' ')
"""
"""
for n in range(10,0,-1):
    print(n, end=' ')
"""
"""
for n in range(0,10,2):
    print(n, end=' ')
"""
#%% Ejercicio 3.7: Más operaciones con secuencias
"""

data = [4, 9, 1, 25, 16, 100, 49]
print(min(data))
print(max(data))
print(sum(data))
"""
"""
for x in data:
    print(x)
"""
"""
for n, x in enumerate(data):
    print(n, x)
"""
"""
for n in range(len(data)):
    print(data[n])
"""
#%% Ejercicio 3.8: Un ejemplo práctico de enumetare()
"""
Está hecho en costo_camio.py
"""
#%% Ejercicio 3.9: La función zip()
"""
import csv
f = open('../Data/camion.csv')
filas = csv.reader(f)
encabezados = next(filas)
fila = next(filas)
list(zip(encabezados, fila))
record = dict(zip(encabezados, fila))
print(record)
La parte del ejercicio que hay que modificar costo_camion.py, está hecha en ese archivo directamente!!!
"""
#%% Ejercicio 3.10: Invertir un diccionario
"""
Lo hice en una terminal directamente!
"""