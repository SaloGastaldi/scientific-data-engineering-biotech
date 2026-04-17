#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 19:07:31 2021

@author: salo
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4])
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])

g = plt.scatter(x = x, y = y)
plt.title('scatterplot de los datos')


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

regr = linear_model.LinearRegression()
regr.fit(x, y)

y_pred = regr.predict(x)
mean_squared_error(y, y_pred)
plt.plot(x, y_pred, color='blue', linewidth=3)
plt.show()
            
#Ejemplo:datos sintéticos

import numpy as np

N = 50
minx = 0
maxx = 500
x = np.random.uniform(minx, maxx, N)
r = np.random.normal(0, 25, N) # residuos simulados
y = 1.3*x + r

g = plt.scatter(x = x, y = y)
plt.title('gráfico de dispersión de los datos')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b

g = plt.scatter(x = x, y = y)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')