#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:14:23 2021

@author: salo
"""
#Ejercicio 6.14: Busqueda binaria (Ahora sí la funcion donde_insertar() hace busqueda binaria!)

#bbin.py
def busqueda_binaria(lista, x, verbose = True):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Poscondición:
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
#   if verbose:
#        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2 # si en vez de ''//' ponemos '/', queda un valor float, no entero!
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
#        if verbose:
#            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x, verbose = True):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Poscondición:
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
#    if verbose:
#        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2 # si en vez de ''//' ponemos '/', queda un valor float, no entero!
#        if verbose:
#            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado! Si lo encontramos, salimos!
            break 
            
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if not (izq<= der):
        pos = izq
    return pos

#Ejercicio 6.15: Insertar un elemento en una lista
def insertar(lista, x):
    busqueda = busqueda_binaria(lista, x)
    if busqueda == -1:
        posicion = donde_insertar(lista, x)
        print(f'El elemento {x} no está en la lista, debería insertarse en la posición {posicion} para mantener el orden.')
    else:
        posicion = busqueda
        print(f'El elemento {x} se encuentra en la lista, en la posicion {posicion}')
    
   

lista_ejemplo = [1, 2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
lista = [0,2,4,6]

"""
Probé esto en el interprete
insertar(lista, 4)
El elemento 4 se encuentra en la lista, en la posicion 2

insertar(lista, 3)
El elemento 3 no está en la lista, debería insertarse en la posición 2 para mantener el orden.
"""
    
