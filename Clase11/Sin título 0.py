#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:27:39 2021

@author: salo
"""
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
xc = x**2
ap, bp = ajuste_lineal_simple(xc, y)
grilla_y_p = (grilla_x**2)*ap + bp
plt.scatter(x,y)
plt.plot(grilla_x, grilla_y, c = 'green')
plt.plot(grilla_x, grilla_y_p, c = 'red')
plt.title('ajuste lineal con x^2')
plt.show()

yhat = (x**2)*ap + bp       # valores estimados
residuos = y - yhat         # diferencia entre el valor original y el estimado
ecm = (residuos**2).mean()  # error cuadrático medio
print("ECM:", ecm)


import pandas as pd
from sklearn import linear_model

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4]) # mismos datos x, y
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
datosxy = pd.DataFrame({'x': x, 'y': y}) # paso los datos a un dataframe

ajus = linear_model.LinearRegression() # llamo al modelo de regresión lineal
ajus.fit(datosxy[['x']], datosxy['y']) # ajusto el modelo

grilla_x = np.linspace(start = 0, stop = 70, num = 1000)
grilla_y = ajus.predict(grilla_x.reshape(-1,1))

datosxy.plot.scatter('x','y')
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

#Regresión Lineal Múltiple
#Ejemplo: superficie y antigüedad
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = [50.0, 5.0, 25.0, 70.0]

data_deptos = pd.DataFrame({'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})

X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)

ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)

errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean()) # error cuadrático medio