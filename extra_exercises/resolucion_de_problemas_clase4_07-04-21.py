#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:17:34 2021

@author: salo
"""
"""
#Forma de hacer el invlista.py
def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida = [e] + invertida
    return invertida

lista = [1, 2, 3, 4, 5]
lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

print(invertir_lista(lista))
print(invertir_lista(lista2))
"""
"""
#Forma de hacer el propaga.py
lista_1 = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
lista_2 = [0, 0, 0, 1, 0, 0]
lista_3 = [1,0,0,0,0,-1]
lista_4 = [0,0,0,0]

def propaga(lis):
    for i,f in enumerate(lis): #nos da la posicion "i" y un volor del fosforo "f" 
        if i - 1 >= 0:
            if f==0 and lis[i-1]==1:
                lis[i] = 1
                
    for i in range(len(lis)-1, -1, -1):
        if i + 1 < len(lis):
            if f==0 and lis[i+1] ==1:
                lis[i] = 1
            
    return lis

print(propaga(lista_1)) #No funciona con este primero!
print(propaga(lista_2))
print(propaga(lista_3))
print(propaga(lista_4))

#Forma de hacer arboles.py
#4.21

import csv
from pprint import pprint

def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        arboles = [{encabezado: valor for encabezado, valor in zip(encabezados, fila)} for fila in filas]
    return arboles

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')


def medidas_de_especies(especies, arboleda):
    d = {}
    for especie in especies:
        d[especie] = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
        return d

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
print(medidas)
"""

