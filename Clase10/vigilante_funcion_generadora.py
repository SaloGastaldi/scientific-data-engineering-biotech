#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:11:14 2021

@author: salo
"""
#Ejercicio 10.7: Cambios de precio de un camión
# vigilante.py
import os
import time

def vigilar(nombre_archivo):
    f = open(nombre_archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        else:
            yield line

if __name__ == '__main__':
    import informe

    camion = informe.leer_camion ('../Data/camion.csv')
    
    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        
        
        if nombre in camion:
            print(f'{nombre}, {precio}, {volumen}')
            