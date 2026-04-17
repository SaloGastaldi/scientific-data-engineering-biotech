#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:24:39 2021

@author: salo
"""
#Ejercicio 6.6: Parsear un archivo CSV
#Ejercicio 6.7:Selector de Columnas
#Ejercicio 6.8: Conversión de tipo
#Ejercicio 6.9: Trabajando sin encabezados 
#Ejercicios clase 7
#Ejercicio 7.4: De archivos a "objetos cual archivos"
#fileparse.py


def parse_csv(filas, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    
    # Una inconsistencia
    import csv
    if has_headers == False and select != None:
        raise RuntimeError("Para seleccionar, necesito encabezados.") 
    rows = csv.reader(filas)    
    #Si el archivo no tiene encabezados
    if has_headers == False:
        encabezados = []
        contador = 0
        registros = []
        for fila in rows:
            contador += 1
            if not fila:
                continue
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Fila {contador}: No pude convertir {fila}.')
                        print(f'Fila {contador}: Motivo:', e)
                # Devuelve lista de tuplas
                registro = tuple(fila)     #sin poner fila[0] y fila[1] queda más general, puede que el archivo tenga mas de dos columnas con valores
                registros.append(registro)
            
                
    else:
        # Lee los encabezados del archivo
        encabezados = next(rows)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
                
        contador = 0
        registros = []
        for fila in rows:
                contador += 1
                if not fila:    # Saltear filas vacías
                    continue

                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    try:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Fila {contador}: No pude convertir {fila}.')
                            print(f'Fila {contador}: Motivo:', e)
                # Armar diccionario    
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
    return registros