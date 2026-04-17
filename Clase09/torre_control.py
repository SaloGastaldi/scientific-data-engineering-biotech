#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:54:46 2021

@author: salo
"""
#Ejercicio 9.12: Torre de Control
#torre_control.py

class TorreDeControl():
    def __init__(self):
        self.cola_de_espera = ColaPrioridad()
        
    def nuevo_arribo(self, nombre):
        self.cola_de_espera.encolar_prioritario(nombre)
        
    def nueva_partida(self, nombre):
        self.cola_de_espera.encolar(nombre)
        
    def ver_estado(self):
        self.cola_de_espera.imprimir()
    
    def asignar_pista(self):
        if self.cola_de_espera.esta_vacia() == False:
            return self.cola_de_espera.desencolar()
        else:
            print(f'No hay vuelos en espera.')


class ColaPrioridad:

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []
        self.items_con_prioridad = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def encolar_prioritario(self, x):
        '''Encola el elemento x.'''
        self.items_con_prioridad.append(x)

    def proximo(self):
        '''Devuelve el próximo elemento sin desencolar
        Requiere que la cola no sea vacía'''
        if len(self.items_con_prioridad):
            res = self.items_con_prioridad[0]
        else:
            res = self.items[0]
        return res

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')

        if len(self.items_con_prioridad):
            res = self.items_con_prioridad.pop(0)
            print(f'El vuelo {res} aterrizó con éxito.')
        else:
            res = self.items.pop(0)
            print(f'El vuelo {res} despegó con exito.')
       
    def largo_cola(self):
        '''Devuelve el largo de la cola.'''
        return len(self.items) + len(self.items_con_prioridad)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return self.largo_cola() == 0

    def imprimir(self):
        res = "Vuelos esperando para aterrizar: "
        res += ", ".join(self.items_con_prioridad)
        res += "\n"
        res += "Vuelos esperando para despegar: "
        res += ", ".join(self.items)
        print(res)