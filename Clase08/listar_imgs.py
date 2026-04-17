#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:27:27 2021

@author: salo
"""
#Ejercicio 8.5: Recorrer el arbol de archivos
#listar_imgs.py
import sys
import os

def listar_imgs(directorio):
    print([file for file in os.listdir(directorio+'/un_directorio') if '.png' in file])

def main(argv):
    if len(argv)!=2:
        print(f'Uso adecuado: {sys.argv[0]}' ' directorio')
    else:
        listar_imgs(argv[1])
        
if __name__ == '__main__':
    main(sys.argv)

 
'''
Funciona poniendo en el interprete 
import listar_imgs
listar_imgs.main(['listar_imgs.py', '../Data/ordenar'])
Funciona con directamente con
python3 listar_imgs.py ../Data/ordenar
'''