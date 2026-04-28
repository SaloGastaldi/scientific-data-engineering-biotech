#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:18:17 2021

@author: salo
"""

class TorreDeControl():
    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []
        self.items_con_prioridad = []

    def nueva_partida(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def nuevo_arribo(self, x):
        '''Encola el elemento x.'''
        self.items_con_prioridad.append(x)
        
    def asignar_pista(self):
        '''Devuelve el próximo elemento sin desencolar
        Requiere que la cola no sea vacía'''
        if len(self.items_con_prioridad):
            res = self.items_con_prioridad[0]
            print(f'El vuelo {res} aterrizó con éxito.')
        else:
            res = self.items[0]
            print(f'El vuelo {res} despegó con exito.')
            
        if self.esta_vacia():
            raise ValueError('No hay vuelos en espera')

        if len(self.items_con_prioridad):
            res = self.items_con_prioridad.pop(0)
        else:
            res = self.items.pop(0)
       
 
    def largo_cola(self):
        '''Devuelve el largo de la cola.'''
        return len(self.items) + len(self.items_con_prioridad)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return self.largo_cola() == 0
    
    
    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('No hay vuelos en espera')

        if len(self.items_con_prioridad):
            res = self.items_con_prioridad.pop(0)
        else:
            res = self.items.pop(0)
        return res
  
    

    def ver_estado(self):
        res = "Vuelos esperando para aterrizar: "
        res += ", ".join(self.items_con_prioridad)
        res += "\n"
        res += "Vuelos esperando para despegar: "
        res += ", ".join(self.items)
        print(res)
