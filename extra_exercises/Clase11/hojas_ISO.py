#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 10:26:40 2021

@author: salo
"""
#Ejercicio 11.13: Hojas ISO y recursión
#hojas_ISO.py

def hoja_A(N):
    if N >= 0:
        if N == 0:
            ancho = 841
            largo = 1189
        if N > 0:
            ancho = max(hoja_A(N-1)) // 2
            largo = min(hoja_A(N-1))
    
    return ancho, largo
    