#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:47:44 2021

@author: salo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Imaginate una fila con varios fósforos uno al lado del otro.
Los fósforos pueden estar en tres estados: nuevos, prendidos
fuego o ya gastados (carbonizados).
​
Representaremos esta situación con una lista L con un elemento por fósforo,
que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado).
El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósforo
nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.
​
Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y
devuelva un vector en el que los 1's se propagaron a sus vecinos con 0.
Guardalo en un archivo propaga.py.
"""
​
def propagar_v1(lis):
    for i, f in enumerate(lis):
        if i - 1 >= 0:
            if f==0 and lis[i-1]==1:
                lis[i] = 1
​
    return lis
​
​
def propagar_v2(lis):
    for i, f in enumerate(lis):
        if i - 1 >= 0:
            if f==0 and lis[i-1]==1:
                lis[i] = 1
        if i + 1 < len(lis):
            if f==0 and lis[i+1]==1:
                lis[i] = 1
    return lis
​
def propagar_v3(lis):
    hice_cambio = True
    while hice_cambio:
        hice_cambio = False
        for i, f in enumerate(lis):
            if i - 1 >= 0:
                if f==0 and lis[i-1]==1:
                    lis[i] = 1
                    hice_cambio = True
​
            if i + 1 < len(lis):
                if f==0 and lis[i+1]==1:
                    lis[i] = 1
                    hice_cambio = True
    return lis
​
def propagar_v4(lis):
    for i in range(len(lis)):
        if i - 1 >= 0:
            if lis[i]==0 and lis[i-1]==1:
                lis[i] = 1
​
    for i in range(len(lis)-1,-1,-1):
        if i + 1 < len(lis):
            if lis[i]==0 and lis[i+1]==1:
                lis[i] = 1
​
    return lis
​
lista_1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 1, 0, 0]
lista_3 = [ 1, 0, 0, 0, 0, -1]
lista_4 = [ 0, 0, 0, 0, 0, -1]
lista_5 = [ 0, 0, 0, 0, 0, 1]
lista_6 = []