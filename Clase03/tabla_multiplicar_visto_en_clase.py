#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:22:56 2021

@author: salo
"""
"""
def tabla():
    for x in range (5):
        valor = 0
        print()
        for y in range (5):
#            print ('x:' ,x, 'y:', y, 'val:',valor)
            print(f'{valor:>5}', end='')
            valor = valor + x

tabla()
"""
#Acá podemos setear el N nosotres
def tabla(N):
    for x in range(N):
        valor = 0
        print()
        for y in range(N):
            print(f'{valor:>5}', end='')
            valor = valor + x

tabla(6)