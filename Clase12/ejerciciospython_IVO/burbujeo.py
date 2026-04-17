#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:40:34 2020

@author: ivan
"""

def ord_burbujeo(lista):
    n = len(lista)
    for i in range(n): 
        ordenado = True
        for j in range(n-i-1): 
            if lista[j] > lista[j+1]: 
                lista[j], lista[j+1] = lista[j+1], lista[j]
                ordenado = False
        if ordenado:
            break
    return lista

#El algoritmo tiene complejidad cuadrática. 