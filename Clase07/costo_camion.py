#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Ejercicio 6.12: Un poco mas allÃ¡ => (Ejercicio 2.9: Funciones de la biblioteca MODIFICADO!)
#costo_camion.py
#Ejercicio 7.2: Función main() 
#Ejercicio 7.3: Hacer un script
#Ejercicio 7.5: La funcion leer_camion del archivo informe.py con la nueva version de fileparse, funciona!
import informe
import sys

def costo_camion(nombre_archivo_camion):
    camion = informe.leer_camion(nombre_archivo_camion)
    costo_total = 0
    for producto in camion:
        cajones = producto['cajones']
        precio = producto['precio']
        costo_por_cajones = cajones * precio
        costo_total = costo_total + costo_por_cajones
    return costo_total

#Ejercicio 7.2: Función main() 
def main(argv):
    if len(argv) != 2:
        print(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    else:
        camion = argv[1]
        print(f'Costo total: {costo_camion(camion)}')

#Ejercicio 7.3: Hacer un script    
if __name__ == '__main__':
    main(sys.argv)
