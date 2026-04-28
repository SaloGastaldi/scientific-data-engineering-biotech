#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:25:23 2021

@author: salo
"""
#Ejercicio 6.13: Busqueda lineal sobre listas ordenadas.
#funcion busqyeda_lineal(lista,e) de la seccion 4.2, modificada!
#busqueda_en_listas.py 

def busqueda_lineal_ordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    lista_ordenada = sorted(lista)
    print(lista_ordenada)
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista_ordenada): # recorremos la lista
        medio = int(len(lista_ordenada)/2) #analiamos el valor del medio de la lista
        if i == medio and z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        if lista_ordenada[medio] > e:
            izq = lista_ordenada[:medio]
            lista_nueva = izq
            print(izq)
        if lista_ordenada[medio] < e:
            der = lista_ordenada[medio:]
            lista_nueva = der
            print(der)
        
    return pos

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
print(busqueda_lineal_ordenada(lista, 2))