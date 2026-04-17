#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:55:16 2021

@author: salo
"""
#Ejercicio 3.18: Lectura de los Arboles de un parque
import csv
from collections import Counter

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
parque_los_andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
parque_centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

#Ejercicio 3.19: Determinar las especies en un parque

def especies(lista_arboles):
    especies = []
    for arbol in lista_arboles:
        especies.append(arbol['nombre_com'])
    unicos_especies = set(especies)
    return(unicos_especies)
print(f'Especies Parque General Paz \n {especies(parque_general_paz)} \n')
print(f'Especies Parque Los Andes \n {especies(parque_los_andes)} \n')
print(f'Especies Parque Centenario \n {especies(parque_centenario)}')
print(f'\n\n')

#Ejercicio 3.20: Contar ejemplares por especie

def contar_ejemplares(lista_arboles):
    ejemplares = Counter()
    for arbol in lista_arboles:
        ejemplares[arbol['nombre_com']] += 1
    return ejemplares.most_common(5)
print(f'Parque General Paz - Cantidad de ejemplares de las 5 especies más comunes: \n {contar_ejemplares(parque_general_paz)}')
print(f'Parque Los Andes - Cantidad de ejemplares de las 5 especies más comunes: \n {contar_ejemplares(parque_los_andes)}')
print(f'Parque Centenario - Cantidad de ejemplares de las 5 especies más comunes: \n {contar_ejemplares(parque_centenario)}')
print(f'\n\n')

#Ejercicio 3.21: Alturas de una especie en una lista
    
def obtener_alturas(lista_arboles, especie):
    lista_alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista_alturas.append(float(arbol['altura_tot']))
    return lista_alturas

alturas_general_paz = obtener_alturas(parque_general_paz, 'Jacarandá')
altura_max_general_paz = max(alturas_general_paz)
altura_promedio_general_paz = (sum(alturas_general_paz) / len(alturas_general_paz))
print(f'General Paz | Altura máxima Jacarandá: {altura_max_general_paz} | Altura promedio Jacarandá: {altura_promedio_general_paz}')
alturas_los_andes = obtener_alturas(parque_los_andes, 'Jacarandá')
altura_max_los_andes = max(alturas_los_andes)
altura_promedio_los_andes = (sum(alturas_los_andes) / (len(alturas_los_andes)))
print(f'Los Andes | Altura máxima Jacarandá: {altura_max_los_andes} | Altura promedio Jacarandá: {altura_promedio_los_andes:.2f}')
alturas_centenario = obtener_alturas(parque_centenario, 'Jacarandá')
altura_max_centenario = max(alturas_centenario)
altura_promedio_centenario = (sum(alturas_centenario) / (len(alturas_centenario)))
print(f'Centenario | Altura máxima Jacarandá: {altura_max_centenario} | Altura promedio Jacarandá: {altura_promedio_centenario:.2f}')
print(f'\n\n')

#Ejercicio 3.22: Inclinaciones por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    lista_inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista_inclinaciones.append(float(arbol['inclinacio']))
    return lista_inclinaciones

inclinacion_general_paz = obtener_inclinaciones(parque_general_paz, 'Falso Guayabo (Guayaba del Brasil)')
print(f'Inclinaciones del Falso Guayabo en Barrio General Paz: \n{inclinacion_general_paz}' )
inclinacion_los_andes = obtener_inclinaciones(parque_los_andes, 'Falso Guayabo (Guayaba del Brasil)')
print(f'Inclinaciones del Falso Guayabo en Barrio Los Andes: \n{inclinacion_los_andes}')
inclinacion_centenario = obtener_inclinaciones(parque_centenario, 'Falso Guayabo (Guayaba del Brasil)')   
print(f'Inclinaciones del Falso Guayabo en Barrio Centenario: \n{inclinacion_centenario}')  

   