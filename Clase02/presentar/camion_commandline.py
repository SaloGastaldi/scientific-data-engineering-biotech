#Ejercicio 2.10: Ejecución desde la linea de comandos con parámetros
#camion_commandline.py
import csv
import sys
def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    costo_total = 0
    for row in rows:
        try:
            costo_por_cajones = (int(row[1]) * float(row[2]))
            costo_total = costo_total + costo_por_cajones
        except:
            pass
    return costo_total
    f.close()
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/camion.csv'


costo = costo_camion(nombre_archivo)
print('Costo total:', costo) 
