#!/usr/bin/env python3
import csv
from pprint import pprint
from collections import Counter
 
def leer_parque(nombre_archivo, parque):
     archivo = open(nombre_archivo, "r", encoding="UTF-8")
     csv_file = csv.reader(archivo)
     informacion_parque = []
     headers = next(csv_file)
     for item in csv_file:
         if(parque in item):
             informacion_parque.append(dict(zip(headers, item)))
     return informacion_parque
 
def especies(lista_arboles):
     dicc_numero_especies = {}
     for arbol in lista_arboles:
         if arbol["nombre_com"] not in dicc_numero_especies.keys():
             dicc_numero_especies[arbol["nombre_com"]] = 1
         else:
             dicc_numero_especies[arbol["nombre_com"]] += 1
     return dicc_numero_especies
 

arboles_general_paz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
especies_general_paz = Counter(especies(arboles_general_paz))
pprint(especies_general_paz)