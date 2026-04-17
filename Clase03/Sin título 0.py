#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:22:56 2021

@author: salo
"""

def tabla():
    for x in range (5):
        valor = 0
        for y in range (5):
            valor = valor + x
            print (valor)
tabla()