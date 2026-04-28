# -*- coding: utf-8 -*-
"""
ticker.py

Una funcion lee un archivo csv. Ppuedo elegir columnas
y contiene funciones generadoras que convierten el tipo de 
datos a diccionarios

@author: sil_d
"""

from vigilante import vigilar
import csv
from formato_tabla import crear_formateador
import informe
#%%
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
#%%        
def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]
#%%
def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
#%%        
def filtrar_datos(filas, nombres):
    '''
    deja pasar únicamente aquellos lotes incluidos en el camión
    '''
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila
#%%
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows= elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])    
    return rows
#%%
def imprimir(data, formateador):
    '''
    accede a los valores del diccionario a partir de las claves
    e imprime de acuerdo al formato.
    '''
    formateador.encabezado(['nombre', 'precio', 'volumen'])
    for fila in data:
        datos= [fila['nombre'], str(fila['precio']), str(fila['volumen'])]
        formateador.fila(datos)
#%%        
def ticker(camion_file, log_file, fmt):
    camion = informe.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file)) 
    rows = filtrar_datos(rows,camion) 
    formateador = crear_formateador(fmt) 
    imprimir(rows, formateador)
    
#%%       
if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
        
#%%
'''
import informe
camion = informe.leer_camion('../Data/camion.csv')
filas = parsear_datos(vigilar('../Data/mercadolog.csv'))
filas = filtrar_datos(filas, camion)
for fila in filas:
    print(fila)
'''
#%%
from ticker import ticker
ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')
ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')
#%%