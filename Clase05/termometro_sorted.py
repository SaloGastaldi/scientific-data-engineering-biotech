#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:36:40 2021

@author: salo
"""
import random
print(f'Valores de temperatura')
mu = 37.5
sigma = 0.2
n = 999
Tmedidas = []
for i in range(n):
    Tmedida = random.normalvariate(mu,sigma)
    Tmedidas.append(Tmedida)
    print(f'{Tmedida:.2f}', end=' ')
    
print(f'\n')  

def maximo(lista):
    T = lista[0]
    for t in lista:
        if t > T:
            T = t
        t += 1
    return T

maximo = maximo(Tmedidas)
print(f'Temperatura máxima: {maximo:.2f}')    
    
def minimo(lista):
    T = lista[0]
    for t in lista:
        if t < T:
            T = t
        t += 1
    return T

minimo = minimo(Tmedidas)
print(f'Temperatura mínima: {minimo:.2f}')

promedio = sum(Tmedidas)/n
print(f'Promedio: {promedio:.2f}')

valores_ordenados = sorted(Tmedidas)
valor_medio = int(n/2)
print(f'Mediana: {Tmedidas[valor_medio]:.2f}')

Q1 = int(((n + 1)/4))
Q3 = int(((3*(n + 1))/4))
print(f'Primer Cuartil: {Tmedidas[Q1]:.2f} \nSegundo Cuartil: {Tmedidas[valor_medio]:.2f} \nTercer Cuartil: {Tmedidas[Q3]:.2f}')

#Ejercicio 5.7: Guardar temperaturas
import numpy as np
Temp= np.array(Tmedidas)

#Corrí en el interprete de la ventana de spyder
#np.save('../Data/Temperaturas.npy', Temp) para guardar el archivo
#guardé los valores de los datos ordenados, porque lo uquiqué acá 
#abajo en el código, si lo ubiese ubicado más arriba, guardaba los datos
#como los fui tomando
