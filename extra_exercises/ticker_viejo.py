#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:27:59 2021

@author: salo
"""
#Ejercicio 10.15: Código simple
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
        rows = csv.reader(lines)
        rows = elegir_columnas(rows, [0, 1, 2])
        rows = cambiar_tipo(rows, [str, float, int])
        rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
        return rows

#    def filtrar_datos(filas, nombres):
#        for fila in filas:
#            if fila['nombre'] in nombres:
#                yield fila
                
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
        imprimir(rows, formateador)

 #   if __name__ == '__main__':
 #       import sys
 ##       main(sys.argv)