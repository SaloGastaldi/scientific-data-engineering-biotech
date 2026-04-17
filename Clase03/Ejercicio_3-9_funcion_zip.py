#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:45:14 2021

@author: salo
"""
import csv
f = open('../Data/camion.csv')
filas = csv.reader(f)
encabezados = next(filas)
fila = next(filas)
print(fila)