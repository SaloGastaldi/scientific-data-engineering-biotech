#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:16:59 2021

@author: salo
"""
#Ejercicio 11.2: Números triangulares (modificacion del Ejercicio 7.6: Sumas)

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    def sumar(lista):
        '''Devuelve la suma de los elementos en la lista.'''
        res = 0
        if len(lista) != 0:
            n = 0 
            res = lista[n] + sumar(lista[n+1:])
        return res
    
    lista = [i for i in range(desde,hasta+1)]
    return sumar(lista)


#Ejercicio 11.3: Dígitos
    
def cuenta_digitos(n):
    '''
    Precondición: n entero positivo.
    Devuelve: la cantidad de digitos que tiene el número n.
    '''
    if n < 10:
        return 1          #caso base
    else:
        return 1 + cuenta_digitos(n // 10) 

#Ejercicio 11.4: Potencias
   
def es_potencia(n, b):
    '''
    Precondición: n y b son enteros
    Devuelve: True si n es potencia de b
    '''
    if n <= b:
        if (n == 1) or (n == b):
            return True
        else:
            return False
    else:
        return es_potencia(n/b, b)
            
#Ejercicio 11.5: Subcadenas
def posiciones_de(a, b, indx=0, l = False):
    '''Devuelve una lista con las posiciones en donde se encuentra b dentro de a'''
    if not l:
        l = []
    
    if len(a) == len(b) and b in a:        #Caso base
        l.append(indx)
        return l
    
    else:
        while len(a) > len(b):
            if b[0:] in a[0:len(b)]:
                l.append(indx)
            l = posiciones_de(a[1:], b, indx+1, l)
            return l

#Ejercicio 11.6: Paridad
'''No entiendo que hay que hacer'''

#Ejercicio 11.7: Máximo
def Maximo(lista):
    '''Devuelve el valor máximo de una lista sin usar la funcion max()'''
    if len(lista) == 1:   # caso base
        return lista[0]
    else:
        m = Maximo(lista[1:])
        return m if m > lista[0] else lista[0]

#Ejercicio 11.8: Replicar
#def replicar(lista, n):
#    '''Devuelve replicado n veces, los elementos de la lista'''
 
        
        
#Ejercicio 11.10: Combinatorios
def perms(s):
  if(len(s)==1):
    return s

  res = ''
  for x in range(len(s)):

    res += s[x] + perms(s[0:x] + s[x+1:len(s)])

  return res + '\n'
        
            
    
    



#Ejercicio 11.10: Combinatorios

#def combinaciones(lista, k):