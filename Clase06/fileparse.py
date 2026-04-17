#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:38:46 2021

@author: salo
"""
#Ejercicio 6.6: Parsear un archivo CSV
#Ejercicio 6.7:Selector de Columnas
#Ejercicio 6.8: Conversión de tipo
#Ejercicio 6.9: Trabajando sin encabezados 
#fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    #Si el archivo no tiene encabezados
    if has_headers == False:
        with open(nombre_archivo) as f:
            filas = csv.reader(f)
            registros = []
            for fila in filas:
                if not fila:
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Devuelve lista de tuplas
                registro = (fila[0], fila[1])
                registros.append(registro)
            
                
    else:            
        with open(nombre_archivo) as f:
            filas = csv.reader(f)
            # Lee los encabezados del archivo
            encabezados = next(filas)
            

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Armar diccionario    
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
    return registros
