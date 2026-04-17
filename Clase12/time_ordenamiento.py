#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:40:08 2021

@author: salo
"""
#Ejercicio 12.8:
#time_ordenamiento.py
import copy
import random
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt


#genero una lista
def generar_lista(N):
    lista=[]
    for i in range(N):
        lista.append(random.randint(1,1000)) 
    return lista

#genero una lista de listas
listas = []
for N in range(1, 257):
    listas.append(generar_lista(N))


lista_insercion = copy.deepcopy(listas)
lista_burbujeo = copy.deepcopy(listas)
lista_merge_sort = copy.deepcopy(listas)

#Ordenamiento por seleccion
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
            
#        print("DEBUG: ", lista)

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
    
    
#Ordenamiento burbujeo   

#Recursivo
def ord_burbujeo(lista):
    cambio = False    
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            cambio = True
    if not cambio:
        return lista
    else:
        return ord_burbujeo(lista)
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
#Ordenamiento merge_sort
        
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


#Experomento timeit para los metodos de ordenamiento
#Seleccion
def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos_seleccion = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion

tiempos_seleccion = experimento_timeit_seleccion(listas, 100)


#Insercion
def experimento_timeit_insercion(listas, num):

    tiempos_insercion = []
    
    global lista
    
    for lista in lista_insercion:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_insercion.append(tiempo_insercion)
        
    # paso los tiempos a arrays
    tiempos_insercion = np.array(tiempos_insercion)
    
    return tiempos_insercion

tiempos_insercion = experimento_timeit_insercion(lista_insercion, 100)


#burbujeo
def experimento_timeit_burbujeo(listas, num):

    tiempos_burbujeo = []
    
    global lista
    
    for lista in lista_burbujeo:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_burbujeo.append(tiempo_burbujeo)
        
    # paso los tiempos a arrays
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    
    return tiempos_burbujeo

tiempos_burbujeo = experimento_timeit_burbujeo(lista_burbujeo, 100)

#merge_sort
def experimento_timeit_merge_sort(listas, num):

    tiempos_merge_sort = []
    
    global lista
    
    for lista in lista_merge_sort:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_merge_sort = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_merge_sort.append(tiempo_merge_sort)
        
    # paso los tiempos a arrays
    tiempos_merge_sort = np.array(tiempos_merge_sort)
    
    return tiempos_merge_sort

tiempos_merge_sort = experimento_timeit_merge_sort(lista_merge_sort, 100)


#defino los parametros necesarios para graficar

eje_x = np.linspace(1,256,num=256)
plt.figure()
linea_seleccion = plt.plot(eje_x,tiempos_seleccion, label = "Selección")
linea_insercion = plt.plot(eje_x,tiempos_insercion, label = "Inserción")
linea_burbujeo = plt.plot(eje_x,tiempos_burbujeo, label = "Burbujeo")
linea_merge_sort = plt.plot(eje_x,tiempos_merge_sort, label = "Merge_sort")
plt.title("Comparaciones por Método de Ordenamiento")
plt.xlabel("Largo de la lista")
plt.ylabel("Tiempo de cálculo")
plt.legend()
plt.show()

'''
Tiempo de Calculo de los metodos de ordenamiento
Recordatorio: Cuanto mayor complejidad del algoritmo, menor tiempo tarda(lo dijeron en clases).
* Merge_sort es el más rápido
* Seleccion e insercion ahora se aproximan en el tiempo en el que tardan en ordenar 
* Burbujeo es el menos rápido. O el más lento!
=> Estos comentarios son basados en el gráfico luego de correr el programa, lo que no significa que el codigo del programa esté bien bien escrito!
'''