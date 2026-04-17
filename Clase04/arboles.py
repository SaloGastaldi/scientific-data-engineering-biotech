#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:05:01 2021

@author: salo
"""
#Ejercicio 4.18: Lectura de todos los árboles
#arboles.py
import csv
from pprint import pprint
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

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#pprint(arboleda)
"""
#Ejercicio 4.19: Lista de altos de JAcarandá
H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
pprint(H)  

#Ejercicio 4.20: Lista de altos y diámetros de Jacarandá
HD=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
pprint(HD)
"""
#Ejercicio 4.21: Diccionario con medidas 
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
"""
def medidas_de_especies(especies,arboleda):
    diccionario_medidas = {}
    for especie in especies:
        record = {especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]}
        diccionario_medidas.update(record)
    return diccionario_medidas

medidas = medidas_de_especies(especies, arboleda)
pprint(medidas)
#Otra opcion para hacerlo. No estoy segura que esté bien, porque no se puede ver al cantidad que hay en cada especie!
"""
def medidas_de_especies(especies, arboleda):
    d= [{arbol['nombre_com'] : (float(arbol['altura_tot']),float(arbol['diametro'])) }for arbol in arboleda if arbol['nombre_com'] in especies]
    return d
medidas = medidas_de_especies(especies, arboleda)
pprint(medidas)