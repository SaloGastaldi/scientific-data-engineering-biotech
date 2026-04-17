#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:05:27 2021

@author: salo
"""
#Ejercicio 6.17: Complejidad de incrementar()
#incrementar.py
#hasta listar_secuencia(20) lo hace en un tiempo razonable, ya mas tarda mucho
def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


def listar_secuencias(n):
    lista = [0]*n
    final = [1]*n
    print(lista)
    while lista != final:
        incrementada = incrementar(lista)
        print(incrementada)



