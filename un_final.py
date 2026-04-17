#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 17:00:20 2021

@author: salo
"""
#Respuestas Examen Final
#un_final.py

class Lote:
	def __init__(self, f, c, p):
		self.nombre = f
		self.cajones = c
		self.precio = p
	
	def __repr__(self):
		return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
	
	def __str__(self):
		return f'Lote: {repr(self.nombre)} / {self.cajones} / ${self.precio}'
	
	def costo(self):
		return self.cajones * self.precio
	
	def vender(self, n):
		self.cajones -= n
#%%
#Porque no obtengo la misma salida si ejecuto print(milote) 
#que si pido el valor de milote ?


>>> milote = Lote("naranja" , 100, 32.2)
>>> print(milote)
Lote: 'naranja' / 100 / $32.2
>>> milote
Lote(naranja, 100, 32.2)
>>>

#Respuesta​
#Porque print(milote) es lo que devuelve la función definida como __str__ de la clase Lote.
#Y el valor de milote es lo que devuelve la funcion definina como __repr__ de la clase Lote.
#%%
​
​
def iterador(n):
	for i in range (n):
		if i//2 == i/2:
			yield i
​
pares = iterador(10)
​
#%%
#Porqué el iterador "pares" devuelve 5 elementos, y no tantos como le pida ?
​
for elemento in pares: print(elemento)
0
2
4
6
8
​#Respuesta
#Porque la expresion generadora 
#%%
Porqué es mas eficiente usar una variante de ordenamiento por Seleccion que una variante de Merge Sort en este caso hipotético ?
​
Dada una secuencia de enteros S, se quiere implementar una estrategia para ubicar en el lugar correcto (en términos de ordenamiento ascendente) los K mayores elementos de S, donde K es significativamente menor que len(S). Para fijar ideas, digamos que S tiene mil millones de elementos y que K=12. 