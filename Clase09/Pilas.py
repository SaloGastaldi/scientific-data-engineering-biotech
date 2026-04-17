#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:11:59 2021

@author: salo
"""
#Ejercicio 9.13: Implementar el TAD pila
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]
        
    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)
    
    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
        
    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    
    
def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")

pila_de_llamadas = Pila()
#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)
#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)
#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)
