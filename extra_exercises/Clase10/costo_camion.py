#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:46:14 2021

@author: salo
"""
#Ejercicio 10.2: Iteración sobre objetos
# costo_camion.py

import informe

def costo_camion(filename):
    '''
    Calcula el costo total (cajones * precio) de un camión
    '''
    camion = informe.leer_camion(filename)
    return camion.precio_total()

def main(args):
    if len(args) != 2:
        raise SystemExit('Usoe: %s archivo_camion' % args[0])
    filename = args[1]
    print('Costo total:', costo_camion(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
