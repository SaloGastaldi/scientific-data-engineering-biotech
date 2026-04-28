#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:51:04 2021

@author: salo
"""
"""
# 6.2 Scripting
#Definir nombres
def cuadrado (x):
    return x*x

a = 42 
b = a + 2  # Requiere que 'a' haya sido definida antes.

z = cuadrado (b)  #Requiere que 'cuadrado' y 'b' estén definidos.
print(z)

#Definir funciones
import csv
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios

precios = ('../Data/precios.csv')
print(leer_precios(precios))
"""
#%% 
#Ejercicio 6.3 Funciones
def bar(intems):
    items = [4, 5, 6]
    return items
    
b = [1, 2, 3]
bar(b)
print(b)
print(bar(b))