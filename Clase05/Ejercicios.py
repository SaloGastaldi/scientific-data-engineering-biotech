#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:41:14 2021

@author: salo
"""
"""
import random

dado = random.randint(1,6)
print(dado)
"""
"""
import random
tirada = []
for i in range(5):
    tirada.append(random.randint(1,6))

print(tirada)
"""
#%%
#Ejercicio 5.1:Generala servida
"""
import random
def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada


def es_generala(tirada):
    if max(tirada)==min(tirada): #forma de saber si todos los elementos son iguales
        return True
    else:
        return False


N = 100000
"""
"""
G = sum([es_generala(tirar()) for i in range(N)])
F = sum([es_generala(tirar()) == False for i in range(N) if es_generala(tirar()) == False])
print(G)
print(F)   
"""
"""  
N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}')
"""
#%%
"""
import random
random.seed(31415)

tirada = []
for i in range(5):
    tirada.append(random.randint(1,6))

print(tirada)

#elecciones con reposicion
caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))
print(random.choices(caras,k=5))

#Elecciones sin recosicion
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
print(random.sample(naipes, k=3))
"""
#%%
# 5.2 NumPy
"""
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[0])
print(a[2])
print(a[2][3])
print(a[2,3])

a = np.array([1, 2, 3])
print(a)
np.zeros(2)
"""
#%% Ejercicio 5.6_ arange() y linspace()
"""
import numpy as np

np.arange(1, 20, 2)
#Out[16]: array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])
np.linspace(1, 19, num=10)
#Out[18]: array([ 1.,  3.,  5.,  7.,  9., 11., 13., 15., 17., 19.])
np.linspace(1, 20, num=10)
#Out[19]: 
#array([ 1.        ,  3.11111111,  5.22222222,  7.33333333,  9.44444444,
#       11.55555556, 13.66666667, 15.77777778, 17.88888889, 20.        ])
#La diferencia es el limite, si uno pone 19 da bien, pero si pone 20, cambia, dan numeros float
"""
#Cambiar la forma de un arreglo
"""
a = np.arange(6)
print(a)
b = a.reshape(3, 2)
print(b)
"""
# Agregar un nuevo eje a un arreglo

