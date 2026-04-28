#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:12:53 2021

@author: salo
"""
#Ejercicio 9.11: Canguros buenos y canguros malos
#Ahora sí está bien hecho!
#canguros_buenos.py

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        if not contenido:
            contenido = []
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito', ['pelota', 'mamadera']) #le puedo pasar una lista con las cosas que tiene cangurito dentro de su marsupio
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio('alcohol en gel')
madre_canguro.meter_en_marsupio(cangurito)        #mete al cangurito en el marsupio


 
"""
Tal vez la función super() se puede usar en las otras funciones definidas tambien, 
no me salio!
"""