#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General Purpose CSV Parser.
A flexible tool for parsing CSV files with support for type conversion, 
column selection, and headerless files.
"""

import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.
    
    Args:
        nombre_archivo: Ruta al archivo.
        select: Lista opcional de nombres de columnas a seleccionar.
        types: Lista opcional de funciones de conversión (ej: [str, int, float]).
        has_headers: Booleano que indica si el archivo tiene encabezados.
    """
    registros = []
    
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        
        if has_headers:
            encabezados = next(filas)
            if select:
                # Mapeamos los índices de las columnas seleccionadas
                indices = [encabezados.index(col) for col in select]
                encabezados = select
            else:
                indices = []
        else:
            indices = []
            encabezados = None

        for n_fila, fila in enumerate(filas, start=1):
            if not fila:  # Saltear filas vacías
                continue
            
            # Filtrar columnas si se especificó 'select'
            if indices:
                fila = [fila[i] for i in indices]
            
            # Aplicar conversiones de tipo si se especificó 'types'
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila)]
                except ValueError as e:
                    print(f"Fila {n_fila}: No se pudo convertir {fila}. Error: {e}")
                    continue

            # Armar el registro (Diccionario si hay encabezados, Tupla si no)
            if encabezados:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(fila)
                
            registros.append(registro)
            
    return registros

if __name__ == "__main__":
    # Ejemplo de uso técnico (Testing)
    # data = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
    # print(data)
    pass
