#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:54:39 2021

@author: salo
"""

#Ejercicio 12.7
def merge_sort(lista, cont = 0):
    """Ordena lista mediante el método merge sort, ingresa contador número entero positivo
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada y el contador de las comparaciones totales."""
    cont += 1
    if len(lista) < 2:
        cont +=1
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio],cont=cont)[0]
        der = merge_sort(lista[medio:],cont=cont)[0]
        lista_nueva = merge(izq, der,cont)[0]
        contador=merge(izq, der,cont)[1]
        cont+= contador + 1
    return lista_nueva, cont
def merge(lista1, lista2,count):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2 y el contador de comparaciones actualizado."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        count+=2
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        count+= 1 + 2 
            # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado,count

