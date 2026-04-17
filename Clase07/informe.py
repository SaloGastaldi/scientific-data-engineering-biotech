#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:14:37 2021

@author: salo
"""
#Ejercicio 6.11: Usemos tu módulo
#tabla_informe.py (ejerccio 3.16) modificado 
#Clase 7: ejercicio informe_funciones(clase 6) copiado en informe.py
#Ejercicio 7.2: Función main ()
#Ejercicio 7.3: Hacer un script
#Ejercicio 7.5: Arreglamos las funciones existentes
import fileparse 
import sys

def leer_camion(nombre_archivo_camion):
    with open(nombre_archivo_camion, 'rt') as file:
        camion = fileparse.parse_csv(file, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        return camion

def leer_precios(nombre_archivo_precios):
    with open(nombre_archivo_precios, 'rt') as file:
        lista_precios = fileparse.parse_csv(file, types = [str, float], has_headers = False)
        precios = dict(lista_precios)
        return precios


def hacer_informe(camion, precios):
    informe = []
    for producto in camion:
        nombre = producto['nombre']
        cajones = producto['cajones']
        precio = producto['precio']
        precio_venta = precios[nombre]
        cambio = precio_venta - precio
        tupla_productos = (nombre, cajones, precio, cambio)
        informe.append(tupla_productos)
    return informe

def imprimir_informe(informe):
    headers = ('Nombre' , 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        try:
            print(f"{nombre:>10s} {cajones:>10d} {f'${precio:.2f}':>10} {cambio:>10.2f}")
        except:
            pass
        
#Ejercicio 6.5: Crear una funcion de alto nivel para la ejecucuin del programa.
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    return imprimir_informe(informe)

#Ejercicio 7.2: Función main()
def main(argv):
    if len(argv) != 3:
        print(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    else:
        camion = argv[1]
        precios = argv[2]
        return informe_camion(camion, precios)
#Ejercico 7.3: Hacer un script 
if __name__ == '__main__':
    main(sys.argv)
   
