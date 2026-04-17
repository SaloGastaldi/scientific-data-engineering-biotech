#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:07:48 2021

@author: salo
"""
"""
# Problema: Dada una lista "lista" y un elemento "e"
#devolver el índice de "e" en "lista" si "e" está
#en lista, devolver -1 si e no está en lista.

#Una forma de resolver el problema: recorre desde la posicion 0 al ultimo
def buscar_elem(lista, e):
    i = 0
    pos = -1
    while i < len(lista):
        if lista[i] == e:
            pos = i
            break #una vez que encuentra el valor, corta, entonces cuando buscamos donde está -2 en l2, nos da que está en la posicion 2. (antes daba posicion 6) 
        i += 1
    return pos
#Otra forma de resolver el problema: recorre desde la ultima posicion de la lista a la posicion 0
def buscar_elem2(lista, e):
    p = len(lista) - 1
    
    while p >= 0 and lista[p]!=e:
        p -= 1
    return p


#Otra forma de resolver el problema es con un for    
def buscar_elem3(lista, e):
    for i in range(len(lista)): #Acá te da todo lo que hay en todas las posiciones!
        if lista[i] == e:
            pos = i
            break
    return pos

#Cuarta opcion 
def buscar_elem4(lista, e):
    pos = -1
    for idx, elem in enumerate(lista): #dado el indice y el elemento
        if elem == e:
            pos = idx
            break
    return pos    


l = [3, 6, 7, 1, 9, -2]
l2 = [3,6,-2,7,1,9,-2,-3]

print(buscar_elem(l2, -2))
print(buscar_elem2(l2, -2))
print(buscar_elem3(l2, -2))
print(buscar_elem4(l2, -2))
"""
#%%
"""
# Listas por comprension
l1 = [0,1,2,3,4,5,6,7,8,9]

l2 = [x for x in range(10)] #para x en un rango de 0 a 9, agarrá ese elemento y ponelo en x(el primero que aparece) para generar una lista
print(l2)

lista_nombres = ['Nico', 'Ivan', 'Meli', 'San', 'Mili', 'Salo']
inicial = [nom for nom in lista_nombres if nom[0] in 'AEIOU']
print(inicial)

ejemplo = [l for nom in lista_nombres for l in nom if l in "aeiou"]
print(ejemplo)
#Ejemplo de la tabla de multiplicar que había que generar. Lista de listas
tabla_de_multiplicar = [ [y*x for x in range(10)] for y in range(10)]
print(tabla_de_multiplicar)



tabla_sumas = [ [ sum([x for j in range(y)]) for x in range(10)] for y in range(10)]
print(tabla_sumas)
"""
#%%
a = [1,2,3,4]
b = a
print(a)
print(b)
a [0] = 100
print(a)
print(b)
b [3] = 999
print(a)
print(b)

#%% 
def multiplica(par1, par2):
    return (par1 * par2)

def fun3(par1, par2, par3):
    a = par1(par2, par3)
    print(a)
fun3(multiplica, 'una cadena', 3)
