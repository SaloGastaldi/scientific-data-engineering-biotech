#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:27:02 2021

@author: salo
"""
#Ejercicio 11.14: precio_alquiler ~ superficie
#alquiler.py

import numpy as np
import matplotlib.pyplot as plt

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
g = plt.scatter(x = superficie, y = alquiler)
plt.title('precio_alquiler ~ superficie.')
plt.xlabel('Superficie (metros cuadrados)')
plt.ylabel('Alquiler (miles de pesos)')


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


a, b = ajuste_lineal_simple(superficie, alquiler)

grilla_x = np.linspace(start = 70, stop = 180, num = 1000)
grilla_y = grilla_x*a + b
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())



#Ejemplo: relación cuadrática
np.random.seed(3141) # semilla para fijar la aleatoriedad
N=50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r # relación cuadrática

x = indep_vars
y = dep_vars
plt.scatter(x,y)
plt.title('scatterplot de los datos')
plt.show()

a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = 0, stop = 10, num = 1000)
grilla_y = grilla_x*a + b
g = plt.scatter(x = x , y = y)
plt.title('ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()
errores = y - (x*a + b)
print("ECM", (errores**2).mean())