#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:56:15 2021

@author: salo
"""

#### Ejercicio 4.18: Lectura de todos los árboles

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/05_Arboles2_LC.md#ejercicio-418-lectura-de-todos-los-%C3%A1rboles

# Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 3.18, 
# escribí otra leer_arboles(nombre_archivo) que lea el archivo indicado y devuelva una lista 
# de diccionarios con la información de todos los árboles en el archivo. La función debe 
# devolver una lista conteniendo un diccionario por cada árbol con todos los datos.
# 
# Vamos a llamar arboleda a esta lista.

import csv
from pprint import pprint

def leer_parque(nombre_archivo, parque):
    archivo = open(nombre_archivo, "r", encoding="UTF-8")
    csv_file = csv.reader(archivo)
    informacion_parque = []
    headers = next(csv_file)
    for item in csv_file:
        if(parque in item):
            informacion_parque.append(dict(zip(headers, item)))
    return informacion_parque


def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
        csv_file = csv.reader(archivo)
        headers = next(csv_file)
        lista_arboles = [{header: value for header, value in zip(headers, fila)} for fila in csv_file]
    return lista_arboles    

# Alternativa mas sencilla aprovechando DictReader de la libreria csv:
# 
# def leer_arboles(nombre_archivo):
#     with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
#         csv_file = csv.DictReader(archivo)
#         lista_arboles = list(csv_file)
#     return lista_arboles

parque = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
"""
##########


#### Ejercicio 4.19: Lista de altos de Jacarandá

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/05_Arboles2_LC.md#ejercicio-419-lista-de-altos-de-jacarand%C3%A1

# Usando comprensión de listas y la variable arboleda podés por # ejemplo armar la lista de la 
# altura de los árboles.
# 
# H=[float(arbol['altura_tot']) for arbol in arboleda]
# 
# Usá los filtros (recordá la Sección 4.3) para armar la lista de alturas de los Jacarandás 
# solamente.

lista_alturas_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]

#########


#### Ejercicio 4.20: Lista de altos y diámetros de Jacarandá

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/05_Arboles2_LC.md#ejercicio-420-lista-de-altos-y-di%C3%A1metros-de-jacarand%C3%A1

# En el ejercicio anterior usaste una sola linea para seleccionar las alturas de los Jacarandás 
# en parques porteños. Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de 
# longitud 2) conteniendo no solo el alto sino también el diámetro de cada Jacarandá en la lista.
# 
# Esperamos que obtengas una lista similar a esta:
# 
# [(5.0, 10.0),
#  (5.0, 10.0),
#  ...
#  (12.0, 25.0),
#  ...
#  (7.0, 97.0), 
#  (8.0, 28.0), 
#  (2.0, 30.0), 
#  (3.0, 10.0), 
#  (17.0, 40.0)]

lista_tuplas_alturas_y_diametro_jacaranda = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
"""

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies,arboleda):
    '''Version mas legible, creando un record en cada paso del bucle for, y usando metodo 
    ".update() para actualizar el diccionario"'''
    dicc_medidas = {}
    for especie in especies:
        record = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol["nombre_com"] == especie}]
        dicc_medidas.update(record)
    return dicc_medidas
"""
def medidas_de_especies2(especies,arboleda):
    '''Otra forma de crear el registro'''
  dicc_medidas={}  
  for especie in especies:
    registro=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
    dicc_medidas[especie]=registro
  return dicc_medidas

def medidas_de_especies3(especies,arboleda):
    '''Simil Oneliner, sin creacion de registro, pero aun con un for que recorre cada especie'''
    dicc_medidas = {}
    for especie in especies:
        dicc_medidas = {dicc_medidas[especie]: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol["nombre_com"] == especie]}
    return dicc_medidas

def medidas_de_especies4(especies,arboleda):
    '''Oneliner completo'''
    dicc_medidas = {dicc_medidas[especie]: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda for especie in especies if arbol["nombre_com"] == especie]}
    return dicc_medidas

"""
medidas = medidas_de_especies(especies, arboleda)

#medidas2 = medidas_de_especies2(especies, arboleda)

#medidas3 = medidas_de_especies3(especies, arboleda)

#medidas4 = medidas_de_especies4(especies, arboleda)
pprint(medidas)
#pprint(medidas2)
#pprint(medidas3)
#pprint(medidas4)
