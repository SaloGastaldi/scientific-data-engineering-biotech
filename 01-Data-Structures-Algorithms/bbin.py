#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Binary Search Algorithms.
Implementation of efficient searching and insertion point discovery 
in sorted sequences.
"""

def busqueda_binaria(lista, x):
    """
    Búsqueda binaria estándar.
    Pre: 'lista' debe estar ordenada.
    Pos: Devuelve la posición de 'x' si está en la lista, sino -1.
    """
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2 
        if lista[medio] == x:
            return medio # Elemento encontrado
        if lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return -1

def donde_insertar(lista, x):
    """
    Encuentra la posición óptima para insertar 'x' manteniendo el orden.
    Pre: 'lista' debe estar ordenada.
    Pos: Devuelve el índice donde 'x' debería ser insertado.
    """
    izq = 0
    der = len(lista) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio
        if lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    
    # Si no se encuentra, 'izq' queda en la posición de inserción
    return izq

if __name__ == "__main__":
    # Test cases
    datos = [1, 3, 5, 7, 9, 11, 13, 15]
    objetivo = 8
    
    pos_busqueda = busqueda_binaria(datos, objetivo)
    pos_insercion = donde_insertar(datos, objetivo)
    
    print(f"Lista: {datos}")
    print(f"Elemento {objetivo}:")
    print(f" - Encontrado en índice: {pos_busqueda} (No encontrado)")
    print(f" - Debería insertarse en índice: {pos_insercion}")
