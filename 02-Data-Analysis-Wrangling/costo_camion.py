#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cálculo de costos de logística a partir de archivos CSV.
Este script demuestra el manejo de archivos, parsing de datos y 
robustez frente a datos faltantes.
"""

import csv
import os

def costo_camion(nombre_archivo):
    """
    Calcula el costo total (cajones * precio) de un archivo CSV dado.
    Ignora filas con datos faltantes o inválidos.
    """
    costo_total = 0.0
    
    # Usamos 'with' para asegurar que el archivo se cierre automáticamente
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as f:
            filas = csv.reader(f)
            encabezados = next(filas) # Saltamos los encabezados
            
            for n_fila, fila in enumerate(filas, start=1):
                try:
                    ncajones = int(fila[1])
                    precio = float(fila[2])
                    costo_total += ncajones * precio
                except ValueError:
                    # Informamos si hay un error en los datos pero seguimos procesando
                    print(f"Aviso: Fila {n_fila} omitida por datos inválidos en {nombre_archivo}")
                    
        return costo_total

    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
        return None

def main():
    # Definimos la ruta de forma relativa para que funcione en cualquier compu
    ruta_data = os.path.join('..', 'Data', 'camion.csv')
    
    costo = costo_camion(ruta_data)
    
    if costo is not None:
        print(f'Costo total del camión: ${costo:,.2f}')

if __name__ == "__main__":
    main()
