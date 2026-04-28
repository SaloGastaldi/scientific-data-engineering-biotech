#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:25:54 2021

@author: salo
"""

#comparaciones_ordenamiento.py
import random
import copy
import numpy as np
import matplotlib.pyplot as plt
#Ordenamiento por seleccion  
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    comparaciones = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        comparaciones += n
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        
#        print("DEBUG: ", p[0], n, lista)

        # reducir el segmento en 1
        n = n - 1
    return comparaciones    

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
    comparaciones = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            comp = reubicar(lista, i + 1)
            comparaciones += comp
    return comparaciones
#    print("DEBUG: ", lista, cont)

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    comparaciones = 0 
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        comparaciones += 1
    lista[j] = v
    return comparaciones


#Ordenamiento burbujeo

#Recursivo 
#=> el conteo no lo debo tener bien hecho porque el promedio deberia dar 45 como el metodo de seleccion pero no da asi!

def ord_burbujeo(lista, comparaciones = 0):
    cambios = False    
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            cambios = True
        comparaciones += 1
    if not cambios:
        return comparaciones
    else:
        return ord_burbujeo(lista, comparaciones = comparaciones)
"""
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
"""    
#Ordenamiento metodo merge_sort
    
def merge_sort(lista):
    '''Ordena lista mediante el método merge sort, ingresa contador número entero positivo
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada y el contador de las comparaciones totales.'''
    if len(lista) < 2:
        lista_nueva = lista
        comparaciones = 0
    else:
        medio = len(lista) // 2
        izq, comp_izq = merge_sort(lista[:medio])
        der, comp_der = merge_sort(lista[medio:])
        lista_nueva, comp_merge = merge(izq, der)
        comparaciones = comp_izq + comp_der + comp_merge
        
    return lista_nueva, comparaciones

def merge(lista1, lista2):
    '''Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2 y el contador de comparaciones actualizado.'''
    i, j = 0, 0
    resultado = []
    comparaciones_aux = 0 
    
    while(i < len(lista1) and j < len(lista2)):
        comparaciones_aux += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado, comparaciones_aux   


#genero una lista   
def generar_lista(N):
    lista=[]
    for i in range(N):
        lista.append(random.randint(1,1000)) 
    return lista

#Ejercicio 12.4: experimento con 3 métodos
#promedio de la cantidad de comparaciones que hace cada metodo. Lista de largo 10, repetido 100 veces
N = 10
k = 100
cant_comp_seleccion = 0
cant_comp_insercion = 0
cant_comp_burbujeo = 0

for i in range(k):
    lista_original = generar_lista(N)
    lista_seleccion = copy.deepcopy(lista_original)
    lista_insercion = copy.deepcopy(lista_original)
    lista_burbujeo = copy.deepcopy(lista_original)


    ordenamiento_seleccion = ord_seleccion(lista_seleccion)
    ordenamiento_insercion = ord_insercion(lista_insercion)
    ordenamiento_burbujeo = ord_burbujeo(lista_burbujeo)


    cant_comp_seleccion += ordenamiento_seleccion
    cant_comp_insercion += ordenamiento_insercion
    cant_comp_burbujeo += ordenamiento_burbujeo


print(f'..::Lista de largo 10::.. \nPromedio de comparaciones realizadas por el metodo de ordenamiento:') 
promedio_seleccion = cant_comp_seleccion/k
print(f'  Seleccion: {promedio_seleccion}')
promedio_insercion = cant_comp_insercion/k
print(f'  Insercion: {promedio_insercion}')
promedio_burbujeo = cant_comp_burbujeo/k
print(f'  Burbujeo: {promedio_burbujeo}')




#genero una lista de listas
lista_de_listas = []
for i in range(1,257):
    lista = generar_lista(i)
    lista_de_listas.append(lista)

#Hago copia de la lista de listas
print(f'\n..::Lista de distintos largos::.. \nPromedio de comparaciones realizadas por el metodo de ordenamiento:')
lista_seleccion = copy.deepcopy(lista_de_listas)
lista_insercion = copy.deepcopy(lista_de_listas)
lista_burbujeo = copy.deepcopy(lista_de_listas)
lista_merge_sort = copy.deepcopy(lista_de_listas)


#Aplico el metodo de ordenamiento

comp_seleccion = []
for lista in lista_seleccion:
    comp_seleccion.append(ord_seleccion(lista))

comp_insercion = []
for lista in lista_insercion:
    comp_insercion.append(ord_insercion(lista))
        
comp_burbujeo = []
for lista in lista_burbujeo:
    comp_burbujeo.append(ord_burbujeo(lista))
    
comp_merge_sort = []
for lista in lista_merge_sort:
    comp_merge_sort.append(merge_sort(lista)[1])
    

#Genero los vectores y saco promedio
comparaciones_seleccion = np.array(comp_seleccion)
promedio_seleccion = np.mean(comparaciones_seleccion)
print(f'  Selección: {promedio_seleccion}')

comparaciones_insercion = np.array(comp_insercion)
promedio_insercion = np.mean(comparaciones_insercion)
print(f'  Inserción: {promedio_insercion}')

comparaciones_burbujeo = np.array(comp_burbujeo)
promedio_burbujeo = np.mean(comparaciones_burbujeo)
print(f'  Burbujeo: {promedio_burbujeo}')

comparaciones_merge_sort = np.array(comp_merge_sort)
promedio_merge_sort = np.mean(comparaciones_merge_sort)
print(f'  Merge sort: {promedio_merge_sort}')

#defino lo necesario para el grafico
x = np.linspace(1,256,num=256)
plt.figure()
plt.plot(x, comparaciones_seleccion, label = "Selección")
plt.plot(x, comparaciones_insercion, label = "Inserción")
plt.plot(x, comparaciones_burbujeo, label = "Burbujeo")
plt.plot(x, comparaciones_merge_sort, label = "Merge_sort")
plt.title("Comparaciones por Método de Ordenamiento")
plt.xlabel("Largo de la lista")
plt.ylabel("Número de comparaciones")
plt.legend()
plt.show()

'''
Complejidad de los metodos de ordenamiento
* Seleccion y Burbujeo, solamente depende del largo de la lista.
* Insercion, depende del largo de la lista y del estado (si está mas ordenada o mas desordenada va a tener una complejidad menor o mayor, respectivamente)
* Merge_sort es el mejor de todos los algoritmos graficados. Es el que mayor complejidad tiene y el que menos tarda (se ve en time_ordenamiento)
'''