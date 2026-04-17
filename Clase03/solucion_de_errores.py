#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:15:52 2021

@author: salo
"""
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentarios:
#1-Error de semántica. 
#2-En la línea 26, 27 y 28, agregué print() al principio, para que me devuelva en pantalla True o False, según corresponda. 
#3-En la linea 22, agregué "expresion[i] == 'A'", para que tenga en cuanta las A mayuscula que aparezcan en la expresion.                     
#4-En la línea 24, ubiqué al contador para que salga del loop corriendo un caracter. El código original, no hacía el recorrido sobre todos los caracteres de la expresion, solo evaluaba el primer caracter. 

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.2. Funcion tiene_a(), nuevamente
#Comentarios:
#1-Error sintaxis.
#2-En la línea 39, agregué ":" a final.
#3-En la línea 42, agregué ":" al final. 
#4-En la línea 43, agregué ":" al final y cambié "=" por "==". También añadí "expresion[i] == 'A'" para que tenga en cuenta las A mayuscula que aparezcan en la expresion.
#5-En la línea 46, cambié "Falso" por "False". 

def tiene_a(expresion):    
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.3. Funcion tiene_uno()
#Comentarios:
#1-Error sintaxis y semántico. 
#2-En la línea 68, 69 y 70, agrugué print() al principio para que me devuelva en la pantalla "True" o "False", según corresponda.  
#3-En la línea 70, agruegué las '' a la expresion. 

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno('1984'))

#%%
#Ejercicio 3.4. Funcion suma()
#Comentarios:
#1-Error semántico.
#2-En la línea 80, agregué "return c" para que me devuelva el valor de la variable c. 

def suma(a,b):
    c = a + b
    return c

a = 6
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5. Funcion leer camion()
#Comentario:
#1-Error semántico.
#2-En la línea 107, agregué "registro={}" para que devuelva en pantalla todas las filas del archivo. De la manera que estaba el código original, solo devolvía la última fila, pisando la memoria de las filas anteriores.  

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
            registro={}
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
