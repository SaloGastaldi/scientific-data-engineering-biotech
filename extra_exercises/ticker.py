#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:33:31 2021

@author: salo
"""

#Ejercicio 10.15: Código simple
#Ahora sí con expresiones generadoras!
# ticker.py

def ticker(camion_file, log_file, fmt):
    from vigilante import vigilar
    import csv
    import formato_tabla 
    import informe
    
    def cambiar_tipo(rows, types):
        for row in rows:
            yield [func(val) for func, val in zip(types, row)]

    def hace_dicts(rows, headers):
        for row in rows:
            yield dict(zip(headers, row))

    def elegir_columnas(rows, indices):
        for row in rows:
            yield [row[index] for index in indices]

    def parsear_datos(lines):
        lineas = csv.reader(lines)
        
        #rows = elegir_columnas(rows, [0, 1, 2])
        elegir_cols = ([row[index] for index in [0, 1, 2]] for row in lineas) #Expresion generadora para elegir columnas, devuelve una lista
    
        #rows = cambiar_tipo(rows, [str, float, int])
        camb_type = ([func(val) for func, val in zip([str, float, int], row)] for row in elegir_cols) #Expresion generadora de cambiar tipo, devuelve una lista e itera sobre las filas de elegir columna
        
        #rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
        diccionarios = (dict(zip(['nombre', 'precio', 'volumen'], elem)) for elem in camb_type) #Expresion generadora de armar diccionarios 
        filtrados = (fila for fila in diccionarios if fila['nombre'] in ['Lima', 'Naranja', 'Caqui', 'Mandarina', 'Durazno', 'Naranja'])
        return filtrados

    def filtrar_datos(filas, nombres):
        for fila in filas:
            if fila['nombre'] in nombres:
                yield fila
#    filtrados = fila for fila in diccionarios if fila['nombre'] in nombres
    
    def imprimir(filas, formateador):

        formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
        
        for fila in filas:
            nombre = fila['nombre'].strip('"')
            precio = float(fila['precio'])
            volumen = int(fila['volumen'])
            filadata = [ nombre, f'{precio:0.2f}', f'{volumen:0.2f}' ]
            formateador.fila(filadata)
    
    

     # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
        
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    filas = (fila for fila in filas if fila['nombre'] in camion)
    imprimir(filas, formateador)


#    def main(args):
#        if len(args) == 3:
#            ticker(args[1], args[2])
#        elif len(args) == 4:
#            ticker(args[1], args[2], args[3])
#        else:
#            raise SystemExit('Uso: %s  log_file formato' % args[0])

    if __name__ == '__main__':
        lines = vigilar('../Data/mercadolog.csv')
        rows = parsear_datos(lines)
        for row in rows:
            print(imprimir(rows, formateador))

 #   if __name__ == '__main__':
 #       import sys
 ##       main(sys.argv)