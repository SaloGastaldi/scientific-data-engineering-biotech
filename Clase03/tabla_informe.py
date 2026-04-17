#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:14:37 2021

@author: salo
"""
#Ejercicio 3.13: Recolectar datos
#tabla_informe.py, es el 2.18 modificado. 
#Agregue una funcion hacer_informe y saqué la parte donde hacía el calculo del costo del camion, de la recaudacion por venta y de las ganancias
import csv
def leer_camion(nombre_archivo):
     camion = []
     diccionario_camion = {}
     with open(nombre_archivo, 'rt') as f:
         rows = csv.reader(f)
         headers = next(rows)
         for row in rows:
             diccionario_camion[headers[0]] = row[0]
             diccionario_camion[headers[1]] = int(row[1])
             diccionario_camion[headers[2]] = float(row[2])
             camion.append(diccionario_camion)
             diccionario_camion = {}
     return camion

def leer_precios(nombre_archivo): 
    diccionario_precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                diccionario_precios[row[0]] = float(row[1])
            except:
                pass
    return diccionario_precios

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
 
camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
#for r in informe:
#    print(r)


#Ejercicio 3.15: Agregar encabezados
headers = ('Nombre' , 'Cajones', 'Precio', 'Cambio')

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'---------- ---------- ---------- ----------')
#Ejercicio 3.16: Un desafio de formato
#Comentario: Ahora si está colocado bien el signo '$'
#Ejercicio 3.14: Imprimir una tabla con formato
#Opcion 1
for nombre, cajones, precio, cambio in informe:
    print(f"{nombre:>10s} {cajones:>10d} {f'${precio:.2f}':>10} {cambio:>10.2f}")
#Opcion 2
#for r in informe:
#    print('%10s %10d %10.2f %10.2f' % r)

