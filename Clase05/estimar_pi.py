#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:45:57 2021

@author: salo
"""
#Ejercicio 5.4: Calcular pi
#estimar_pi.py
"""
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

N = 100000
M = 0
for i in range(N):
    x,y = generar_punto()
    if x**2 + y**2 < 1:
        M += 1
print(f'pi ~ {4*M/N:.5f}')
"""
#%%
import matplotlib.pyplot as plt

N= 1000
M=0
Xi = []
Yi = []
Xo = []
Yo = []

for i in range(N):
    x,y = generar_punto()
    if x**2 + y**2 < 1:
        Xi.append(x)
        Yi.append(y)
        M+=1
    else:
        Xo.append(x)
        Yo.append(y)
        
plt.clf()
plt.scatter(Xi, Yi, s=1)
plt.scatter(Xo, Yo, s=1)
plt.show()