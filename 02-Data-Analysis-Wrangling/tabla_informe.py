#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Informes de Ganancias.
Cruza datos de costos de compra (camion.csv) con precios de venta (precios.csv).
"""

import csv
import os

def leer_camion(nombre_archivo):
    """Lee el inventario del camión y devuelve una lista de diccionarios."""
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            lote = {
                'nombre': fila[0],
                'cajones': int(fila[1]),
                'precio': float(fila[2])
            }
            camion.append(lote)
    return camion

def leer_precios(nombre_archivo):
    """Lee los precios de venta y devuelve un diccionario {producto: precio}."""
    precios = {}
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        for fila in filas:
            try:
                precios[fila[0]] = float(fila[1])
            except (IndexError, ValueError):
                continue # Salta filas vacías o malformadas
    return precios

def imprimir_informe(informe):
    """Imprime una tabla formateada con los resultados del análisis."""
    headers = ('Nombre', 'Cajones', 'Precio Compra', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>15s} {headers[3]:>10s}')
    print(f'{"-"*10} {"-"*10} {"-"*15} {"-"*10}')

    for nombre, cajones, precio, cambio in informe:
        precio_str = f"${precio:.2f}"
        print(f"{nombre:>10s} {cajones:>10d} {precio_str:>15s} {cambio:>10.2f}")

def main():
    # Rutas relativas
    ruta_camion = os.path.join('..', 'Data', 'camion.csv')
    ruta_precios = os.path.join('..', 'Data', 'precios.csv')

    if not os.path.exists(ruta_camion) or not os.path.exists(ruta_precios):
        print("Error: No se encuentran los archivos de datos en la carpeta ../Data/")
        return

    camion = leer_camion(ruta_camion)
    precios = leer_precios(ruta_precios)
    
    informe = []
    for producto in camion:
        nombre = producto['nombre']
        precio_venta = precios.get(nombre, 0)
        cambio = precio_venta - producto['precio']
        informe.append((nombre, producto['cajones'], producto['precio'], cambio))

    imprimir_informe(informe)

if __name__ == "__main__":
    main()
