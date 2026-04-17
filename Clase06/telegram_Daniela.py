# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:43:22 2021

@author: Lautaro
"""
import os
os.getcwd()
os.chdir("C:\\Users\\DANIELA\\Desktop\\ACADEMICO\\facultad\\Doctorado\\Python UNSAM\\2do intento\\Ejercicios\\ejercicios_python\\Clase07")

#cuestiones de diseño
def parse_csv(filas,types=None,has_headers=True,select=None,silence_errors=True):
    import csv
    registros=[]
    numfila=0
    for f in filas:
        fila = csv.reader(f)

        if not has_headers and select:
            raise RuntimeError ("Para seleccionar, necesito encabezados.")  #esto funciona
        if has_headers:
            encabezados = next(fila)
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]  
                encabezados = select
            else:
                indices = []
            
                numfila+=1
                if types:
                    try:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    
                        if not fila:    # Saltear filas vacías
                            continue
                        # Filtrar la fila si se especificaron columnas
                        if indices:
                            fila = [fila[index] for index in indices]       
                        # Armar el diccionario
                            registro = dict(zip(encabezados, fila))
                            registros.append(registro)       #hasta aca va perfecto
                    except ValueError as e:
                        if silence_errors:
                            continue
                        else:
                            print(f'No se pudo convertir la fila {fila}')
                            print(f'Motivo: {e}: la fila {numfila} está incompleta')
                            continue
        if not has_headers:
            
                numfila+=1
                
                if types:
                    try:
                        fila = [func(val) for func, val in zip(types, fila)]
                        registros.append((fila[0],fila[1]))
                        if not fila:    # Saltear filas vacías
                            continue
                    except ValueError as e:
                        if silence_errors:
                            continue
                        else:
                            print(f'No se pudo convertir la fila {fila}')
                            print(f'Motivo: {e}: la fila {numfila} está incompleta')
                            continue
        
                                                
    return registros   
#%%

import gzip
# with gzip.open('../Data/camion.csv.gz', 'rt') as file:
#     camion = parse_csv(file, types=[str,int,float],has_headers=True,select=['nombre','cajones','precio'])
# print(camion)

with gzip.open('../Data/camion.csv.gz', 'rt') as file:
    camion = parse_csv(file, types=[str,int,float])
print(camion)
#%%

lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion2=parse_csv(lines, types=[str,int,float],has_headers=True,select=['nombre','cajones','precio'])
           

 #%%                               
import csv
with open('../Data/camion.csv.gz') as f:
    lines2 = csv.reader(f)
    camion3 = parse_csv(lines2, types=[str,int,float],has_headers=True,select=['nombre','cajones','precio'])
