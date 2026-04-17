#Ejercicio 2.9: Funciones de la biblioteca
import csv
def costo_camion(nombre_archivo):
    f = open('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/camion.csv', 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    costo_total = 0
    for row in rows:
        costo_por_cajones = (int(row[1]) * float(row[2]))
        costo_total = costo_total + costo_por_cajones
    return costo_total
    f.close()
costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo) 
