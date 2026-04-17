#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:11:33 2021

@author: salo
"""

#12.2 Ordenamientos sencillos de listas
#Ordenamiento por selección

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    
    return pos_max 



#Ordenamiento por inserción
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
            
        print("DEBUG: ", lista)

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        
    lista[j] = v

    
#Ejercicio 12.1
"""
lista = [0, 9, 3, 8, 5, 3, 2, 4]
#Ordenamiento por seleccion
DEBUG:  1 7 [0, 4, 3, 8, 5, 3, 2, 9]  #Busca el mayor elemento en la lista(desde la posicion 0 hasta n). Lo encuentra en la posicion 1 (valor 9) y lo coloca en la ultima posicion del segmento analizado, posicion 7.
DEBUG:  3 6 [0, 4, 3, 2, 5, 3, 8, 9]  #Busca el mayor elemento en la lista(desde la posicion 0 hasta n-1). Lo encuentra en la posicion 3 (valor 8) y lo coloca en la ultima posicion del segmento analizado, posicion 6.
DEBUG:  4 5 [0, 4, 3, 2, 3, 5, 8, 9]  #Busca el mayor elemento en la lista(desde la posicion 0 hasta n-1-1). Lo encuentra en la posicion 4 (valor 5) y lo coloca en la ultima posicion del segmento analizado, posicion 5.
DEBUG:  1 4 [0, 3, 3, 2, 4, 5, 8, 9]  #Busca el mayor elemento en la lista(desde la posicion 0 hasta n-1-1-1). Lo encuentra en la posicion 1 (valor 4) y lo coloca en la ultima posicion del segmento analizado, posicion 4.
DEBUG:  1 3 [0, 2, 3, 3, 4, 5, 8, 9]  #Busca el mayor elemento en la lista(desde la posicion 0 hasta n-1-1-1-1). Lo encuentra en la posicion 1 (valor 3) y lo coloca en la ultima posicion del segmento analizado, posicion 3.
DEBUG:  2 2 [0, 2, 3, 3, 4, 5, 8, 9]  #Busca el mayor elemento en la lista(desde la posicion 0 hasta n-1-1-1-1-1). Lo encuentra en la posicion 2 (valor 3) y lo coloca en la ultima posicion del segmento analizado, posicion 2. 
DEBUG:  1 1 [0, 2, 3, 3, 4, 5, 8, 9]  #Busca el mayor elemento en la lista(desde la posicion 0 hasta n-1-1-1-1-1-1). Lo encuentra en la posicion 1 (valor 2) y lo coloca en la ultima posicion del segmento analizado, posicion 1.
                                      #Quedó un unico elemento sin tratar, que es el que esta en la posicion 0 de la lista y es el menor de todos.
                                      
#Ordenamiento por insercion
DEBUG:  [0, 9, 3, 8, 5, 3, 2, 4]      #Considera el elemento de la lista en la posicion 1 y lo compara respecto al elemento en la posicion 0. No hace desplazamiento porque el valor 9 es mayor al valor 0.
DEBUG:  [0, 3, 9, 8, 5, 3, 2, 4]      #Considera el elemento de la lista en la posicion 2 y lo compara respecto al elemento en la posicion 1. Lo desplaza hacia la derecha porque el valor 3 en menor al valor 9. Lo compara respecto al elemento en la posicion 0. No lo desplaza porque el valor 3 es mayor que el valor 0.
DEBUG:  [0, 3, 8, 9, 5, 3, 2, 4]      #Considera el elemento de la lista en la posicion 3 y lo compara respecto al elemento en la posicion 2. Lo desplaza hacia la derecha porque el valor 8 es menor al valor 9. Lo compara respecto al elemento en la posicion 1. No lo desplaza porque el valor 8 es mayor que el valor 0.
DEBUG:  [0, 3, 5, 8, 9, 3, 2, 4]      #Considera el elemento de la lista en la posicion 4 y lo compara respecto al elemento en la posicion 3. Lo desplaza hacia la derecha porque el valor 5 es menor al valor 9. Lo compara respecto al elemento en la posicion 2. Lo desplaza hacia la derecha porque el valor 5 es menor que el valor 8. Lo compara respecto al elemento en la posicion 1. No lo desplaza porque el valor 5 es mayor que el valor 3.
DEBUG:  [0, 3, 3, 5, 8, 9, 2, 4]      #Considera el elemento de la lista en la posicion 5 y lo compara respecto al elemento en la posicion 4. Lo desplaza hacia la derecha porque el valor 3 es menor al valor 9. Lo compara respecto al elemento en la posicion 3. Lo desplaza hacia la derecha porque el valor 3 es menor que el valor 8. Lo compara respecto al elemento en la posicion 2. Lo desplaza hacia la derecha porque el valor 3 es menor que el valor 5. Lo compara respecto al elemento en la poscion 1. No lo desplaza porque el valor 3 es igual que el valor 3.
DEBUG:  [0, 2, 3, 3, 5, 8, 9, 4]      #Considera el elemento de la lista en la posicion 6 y lo compara respecto al elemento en la posicion 5. Lo desplaza hacia la derecha porque el valor 2 es menor al valor 9. Lo compara respecto al elemento en la posicion 4. Lo desplaza hacia la derecha porque el valor 2 es menor que el valor 8. Lo compara respecto al elemento en al posicion 3. Lo desplaza hacia la derecha porque el valor 2 es menor que el valor 5. Lo compara respecto al elemento en la posicion 2. Lo desplaza hacia la derecha porque el valor 2 es menor que el valor 3. Lo compara respecto a el elemento en la posicion 1. Lo desplaza hacia la derecha porque el valor 2 es menor que el valor 3. Lo compara respecto al valor en la posicion 0. No lo desplaza porque el valor 2 es mayor que el valor 0. 
DEBUG:  [0, 2, 3, 3, 4, 5, 8, 9]      #Considera el elemento de la lista en la posicion 7 y lo compara respecto al elemento en la posicion 6. Lo desplaza hacia la derecha porque el valor 4 es menor al valor 9. Lo compara respecto al elemento en la posicion 5. Lo desplaza hacia la derecha porque el valor 4 es menor que el valor 8. Lo compara respecto al elemento en la posicion 4. Lo desplaza hacia la derecha porque el valor 4 es menor que el valor 5. Lo compara respecto al elemento en la posicion 3. No lo desplaza porque el valor 4 es mayor que el valor 3.

"""

#Ejercicio 12.2: burbujeo
#burbujeo.py

#Recursivo
def ord_burbujeo_rec(lista):
    cambio = False    
    
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            cambio = True

    if not cambio:
        return lista
    else:
        return ord_burbujeo_rec(lista)

#No recursivo
def ord_burbujeo(lista):
    n = len(lista)
    comparaciones = 0
    cambio = True
    while cambio:
        cambio = False
        for i in range(n-1):
            if lista[i+1] < lista[i]:
                lista[i], lista[i+1] = lista[i+1], lista[1]
                cambio = True
        comparaciones += n - 1
        n -= 1
    return comparaciones


