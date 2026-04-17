#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:30:03 2021

@author: salo
"""
#Ejerccio 5.9: Crear
import random
import numpy as np


def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)
     
#Ejercicio 5.10: Incompleto

def album_incompleto(A):
    if 0 in A:
        return True
    else:
       return False
#print(album_incompleto(crear_album(figus_total)))    
#Ejercicio 5.11: Comprar
        
def comprar_figu(figus_total):
    figus = np.arange(0, figus_total, 1)
    return random.choice(figus)  # tengo que elegir un numero en un rango de 0-5
    
#print(comprar_figu(figus_total))
#Ejercicio 5.12: Cantidad de compras

def cuantas_figus(figus_total):
    album_nuevo = crear_album(figus_total)
    contador = 0
    while album_incompleto(album_nuevo) == True:
        figu_nueva = comprar_figu(figus_total)
        album_nuevo[figu_nueva] += 1
        contador += 1
    return contador 
"""
figus_total = 6
print(f'Para completar un álbum de {figus_total} figus, se debieron comprar {cuantas_figus(figus_total)} figus.')

#Ejercicio 5.13

n_repeticiones = 1000
resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
promedio = int(np.mean(resultados))
print(f'Para completar un álbum de {figus_total} figus, hay que comprar un promedio de {promedio} figus.')

#Ejercicio 5.14
n_repeticiones = 100
figus_total = 670
resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
promedio = int(np.mean(resultados))
print(f'Para completar un álbum de {figus_total} figus, hay que comprar un promedio de {promedio} figus.')
"""
#Ejercicio 5.15 y 5.16
figus_total = 670
figus_paquete = 5
def comprar_paquete(figus_total, figus_paquete):
    paquete = np.arange(0, figus_total, 1)
    return random.choices(paquete, k=figus_paquete)

#paquete_comprado = comprar_paquete(figus_total, figus_paquete)
#print(paquete_comprado)
#Ejercicio 5.17
def cuantos_paquetes(figus_total, figus_paquete):
    album_nuevo = crear_album(figus_total)
    contador = 0
    while album_incompleto(album_nuevo) == True:
        figus_nuevas = comprar_paquete(figus_total, figus_paquete)
        for figu in figus_nuevas:
           album_nuevo[figu] += 1
        contador += 1
    return contador

paquetes_comprados = cuantos_paquetes(figus_total, figus_paquete)
print(f'Para llenar un álbum de {figus_total} figus, se debieron comprar {paquetes_comprados} paquetes de figus.')

#Ejercicio 5.18
""" 
n_repeticiones = 100
resultados = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio_paquetes = int(np.mean(resultados))
print(f'Para completar un álbum de {figus_total} figus, hay que comprar un promedio de {promedio_paquetes} paquetes de figus.')
"""
n_repeticiones = 1000
resultados = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio_paquetes = int(np.mean(resultados))
print(f'Para completar un álbum de {figus_total} figus, hay que comprar un promedio de {promedio_paquetes} paquetes de figus.')

#Ejercicio 5.19

import matplotlib.pyplot as plt
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()