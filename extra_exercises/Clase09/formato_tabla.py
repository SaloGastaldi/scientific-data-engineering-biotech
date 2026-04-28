#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:51:34 2021

@author: salo
"""

# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Genera una tabla en formato HTML
    '''
    def encabezado(self, headers):
        inicio = '<tr><th>'
        cuerpo = '</th><th>'.join(headers)
        fin = '</th></tr>'
        print(f'{inicio}{cuerpo}{fin}')
    
    def fila(self, data_fila):
        inicio = '<tr><td>'
        cuerpo = '</td><td>'.join(data_fila)
        fin = '</td></tr>'
        print(f'{inicio}{cuerpo}{fin}')

#Ejercicio 9.7: Polimorfismo en acción

def crear_formateador(fmt):
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formateador

#Ejercicio 9.10: Ejemplo de getattr()

def imprimir_tabla(archivo, columnas, formateador):
    formateador.encabezado(columnas)
    for c in archivo:
        lista = []
        for colname in columnas:
            lista.append(str(getattr(c, colname)))
        formateador.fila(lista)
   