#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:46:14 2021

@author: salo
"""

#Ejercicio 9.1: Objetos como estructura de datos.
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
#Ejercicio 9.2: Agregá algunos métodos    
    # Método costo()
    def costo(self):
        return self.cajones * self.precio
    
    # Método vender()
    def vender(self, cajones_vendidos):
        self.cajones = self.cajones - cajones_vendidos
    
#Ejercicio 9.9: Mejor salida para objetos
class Lote(object):
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    # Con `str()`
    def __str__(self):
       return f'{self.nombre}-{self.cajones}-{self.precio}'

    # Con `repr()`
    def __repr__(self):
        return f'Lote({object.__str__(self.nombre)},{self.cajones},{self.precio})'