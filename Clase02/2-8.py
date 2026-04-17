#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:36:25 2021

@author: salo
"""

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad