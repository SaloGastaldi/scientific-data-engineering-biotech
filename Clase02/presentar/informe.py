#Ejercicio 2.15: Lista de tuplas
# fragmento de costo_camion.py
#import csv
#def leer_camion(nombre_archivo):
#    camion = []
#    with open(nombre_archivo, 'rt') as f:
#        rows = csv.reader(f)
#        headers = next(rows)
#        for row in rows:
#            lote = (row[0], int (row[1]), float(row[2]))
#            camion.append(lote)
#    return camion

#Ejercicio 2.16: Lista de diccionarios
#import csv
#def leer_camion(nombre_archivo):
#    camion = []
#    diccionario_camion = {}
#    with open(nombre_archivo, 'rt') as f:
#        rows = csv.reader(f)
#        headers = next(rows)
#        for row in rows:
#            diccionario_camion[headers[0]] = row[0]
#            diccionario_camion[headers[1]] = int(row[1])
#            diccionario_camion[headers[2]] = float(row[2])
#            camion.append(diccionario_camion)
#            diccionario_camion = {}
#    return camion

#Ejercicio 2.17: Diccionarios como contenedores
#import csv
#def leer_precios(nombre_archivo): 
#    diccionario_precios = {}
#    with open(nombre_archivo, 'rt') as csv_file:
#        rows = csv.reader(csv_file)
#        for row in rows:
#            try:
#                diccionario_precios[row[0]] = float(row[1])
#            except:
#                pass
#    return diccionario_precios



#Ejercicio 2.18: Balances
import csv
def leer_camion(nombre_archivo):
     camion = []
     diccionario_camion = {}
     with open(nombre_archivo, 'rt') as f:
         rows = csv.reader(f)
         headers = next(rows)
         for row in rows:
             diccionario_camion[headers[0]] = row[0]
             diccionario_camion[headers[1]] = int(row[1])
             diccionario_camion[headers[2]] = float(row[2])
             camion.append(diccionario_camion)
             diccionario_camion = {}
     return camion

def leer_precios(nombre_archivo): 
    diccionario_precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                diccionario_precios[row[0]] = float(row[1])
            except:
                pass
    return diccionario_precios

 
camion = leer_camion('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/camion.csv')
costo_camion = 0
for s in camion:
    costo_camion += s['cajones'] * s['precio']
#print(f'Costo del camion: {costo_camion}')

precios = leer_precios('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/precios.csv')
recaudacion = 0
for s in camion:
    recaudacion += s['cajones'] * precios[s['nombre']]
#print(f'Recaudacion ventas: {recaudacion}') 

diferencia = recaudacion - costo_camion
#print(f'Ganancias: {diferencia:.2f}')

print(f'::Balance::\n| Costo del camion: {costo_camion} | Recaudacion ventas: {recaudacion} | Ganancias: {diferencia:.2f} |')
