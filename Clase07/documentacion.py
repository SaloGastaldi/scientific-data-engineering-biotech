#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:50:15 2021

@author: salo
"""
#documentacion.py
"""
#Ejercicio 7.6: Sumas


def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    if hasta <= desde:  #si hasta < desde entonces devuelve cero. Si el intervalo es vacio (desde = hasta) tambien devuelve cero.
        suma = 0
        return suma
    
    # Sin ciclo: diferencia de dos numeros triangulares
    n = hasta
    T_hasta = int((n*(n+1)/2))
    suma = T_hasta
    
    print(suma)
    # Usando un ciclo
    for i in range(desde, hasta+1):
        suma = sum(range(desde, hasta+1))
        return suma
    
print(sumar_enteros(0,6))

#Ejercicio 7.7: Invariante en sumas
'''
la variable suma es el invariante del ciclo en la funcion sumar_enteros(desde, hasta), definida en el ejercicio 7.6.

'''
"""
#Ejercicio 7.8: Funciones y documentación

def valor_absoluto(n):
    '''
    Valor absoluto
    Pre: recibe un número 'n'.
    Pos: devuelve su valor absoluto.
    '''
    if n >= 0:
        return n
    else:
        return -n
    #Invariante: n
print(valor_absoluto(-3))


def suma_pares(l):
    '''
    Cálculo de suma de pares
    
    Pre: recibe una lista de números 'l'.
    Pos: suma los números pares dentro de esa lista 'l'.
    '''
    res = 0 
    for e in l:        
        if e % 2 ==0: #si el el elemento 'e' es divisible por 2 => es par!
            res += e  # si es par, lo suma.
        else:
            res += 0 #si es impor, no lo suma.

    return res

l = [0, 1, 2, 3, 4, 5, 6, 7]
print(suma_pares(l))

def veces(a, b):
    '''Multiplicacion
    Pre: recibe un número 'a' y una cantidad de veces 'b'.
    La cantidad de veces 'b', tiene que ser un número positivo.
    Pos: devuelve la suma de 'b' veces el número 'a'.
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    #Invariantes: a, b
print(veces(-3, 50))

def collatz(n):
    '''
    Conjetura de Collatz 
    
    Pre: recibe un número 'n'. 'n' debe ser entero positivo.
    Pos: realiza una operacion matematica con la que se puede considerar la orbita de 'n'. Es decir, devuelve las imágenes sucesivas al iterar el ciclo definido.  
    '''
    res = 1

    while n!=1:             
        if n % 2 == 0:      
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

print(collatz(10))