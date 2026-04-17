#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:37:02 2021

@author: salo
"""
#Ejercicio 5.2: Generala no necesariamente servida
#generala.py
import random
def tirar(cant_dados):
    tirada = []
    for i in range(cant_dados):
        tirada.append(random.randint(1,6))
    return tirada
#    return [random.randint(1,6) for _ in range(cant_dados)]


def es_generala(tirada):
    if max(tirada)==min(tirada): #forma de saber si todos los elementos son iguales
        return True
    else:
        return False

def cuantos_de_cada(dados_en_mesa):
    return sorted([(dados_en_mesa.count(d), d) for d in range(1,6+1)], reverse = True) #devuelve la cantidad de veces que se repite el valor d del dado. Sorted los ordena de menos a mayor

def generala_varias_manos():
    manos = 3
    mesa = [] 
    for i in range(manos):
        mesa = mesa + tirar(5 - len(mesa))
        if i < manos -1:
            (cant, valor) = cuantos_de_cada(mesa)[0]
            mesa = [valor] * cant    
    return es_generala(mesa)
    
N = 1000000
G = sum([es_generala(tirar(5)) for _ in range(N)])
G_varias_manos = sum([generala_varias_manos() for _ in range(N)])
prob = G/N
prob_varias_manos = G_varias_manos/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}')        
print(f'Tiré {N} veces, de las cuales {G_varias_manos} saqué generala luego de varias manos.')
print(f'Podemos estimar la probabilidad de sacar generala luego de varias manos mediante {prob_varias_manos:.6f}')        

