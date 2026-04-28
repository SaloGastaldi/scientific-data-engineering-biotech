#Ejercicio 3.9: La funcion zip() 
#Modificacion del ejercicio 2.18 para que elija columnas dentro de un archivo a partir de sus encabezados
import csv
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        costo_total = 0
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            except ValueError:
                pass
                print(f'Fila {n_fila}: No puede interpretar {fila}')
        return costo_total


def leer_camion(nombre_archivo):
     camion = []
     with open(nombre_archivo, 'rt') as f:
         filas = csv.reader(f)
         encabezados = next(filas)
         for n_fila, fila in enumerate(filas, start=1):
             try:
                 record = dict(zip(encabezados, fila))
                 camion.append(record)
             except ValueError:
                 print(f'Fila {n_fila}: No puede interpretar {fila}')
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
costo = costo_camion('../Data/fecha_camion.csv')

precios = leer_precios('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/precios.csv')
recaudacion = 0
for s in camion:
    recaudacion += int(s['cajones']) * float(precios[s['nombre']])

diferencia = recaudacion - costo

print(f'::Balance::\n| Costo del camion: {costo} | Recaudacion ventas: {recaudacion} | Ganancias: {diferencia:.2f} |')
