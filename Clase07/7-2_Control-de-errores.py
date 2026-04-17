#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:01:52 2021

@author: salo
"""
#7.2 Control de errores

def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hola', 'mundo')    # 'Holamundo'
add('3', '4')           # '34'
add(3, '4')