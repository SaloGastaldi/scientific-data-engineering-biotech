#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:41:25 2021

@author: salo
"""

#%% 3.5 Impresión con formato
"""
nombre = 'Naranja'
cajones = 100
precio = 91.1
print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}')
""" 
#%%Formato a diccionarios
"""
s = {
    'nombre': 'Naranja',
    'cajones': 100,
    'precio': 91.1
}
print('{nombre:>10s} {cajones:10d} {precio:10.2f}'.format_map(s))
"""
#%% El método format()
"""
print('{nombre:>10s} {cajones:10d} {precio:10.2f}'.format(nombre='Naranja', cajones=100, precio=91.1))
print('{:10s} {:10d} {:10.2f}'.format('Naranja', 100, 91.1))
"""
#%% Formato estilo C
"""
print('The value is %d' %3)
print('%5d %-5d %10d' % (3,4,5))
print('%0.2f' % (3.1415926,))
"""
#%% Ejercicio 3.12: Formato de números
"""
value = 42863.1
print(value)
print(f'{value:>0.4f}')
print(f'{value:>16.2f}')
print(f'{value:<16.2f}')
print(f'{value:*>16,.2f}')
print('%0.4f' % value)
print('%16.2f' % value)
f = '%0.4f' % value
print(f)
"""