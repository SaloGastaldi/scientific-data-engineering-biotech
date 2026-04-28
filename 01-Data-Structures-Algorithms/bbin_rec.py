#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:53:34 2021

@author: salo
"""
#Ejercicio 11.11: Búsqueda binaria
#bbin_rec.py

def bbinaria_rec(lista, e):
    
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e 
    else:
        medio = len(lista)//2
        if (lista[medio] == e):
            res = True
        else:
            if lista[medio] < e:
                return bbinaria_rec(lista[medio+1:], e)
            else:
                return bbinaria_rec(lista[:medio], e)
    return res
       
#lo probé con
#lista = [2, 4, 6, 8, 10]