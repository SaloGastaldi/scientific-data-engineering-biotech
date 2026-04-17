#Ejercicio 2.2: Lectura de un archivo de datos
#costo_camion.py

#with open('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/camion.csv', 'rt') as f:
#    headers = next(f).split(',')
#    costo_total = 0
#    for line in f:
#        line = line.rstrip('\n')
#        row = line.split(',')
#        costo_por_cajones = (int(row[1]) * float(row[2]))
#        costo_total = costo_total + costo_por_cajones
#print(f'Costo total {costo_total}')


#Ejercicio 2.6: Transformar un script en una funcion    
#costo_camion.py
def costo_camion(nombre_archivo):
    f = open('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/camion.csv', 'rt')
    headers = next(f).split(',')
    costo_total = 0
    for line in f:
        line = line.rstrip('\n')
        row = line.split(',')
        costo_por_cajones = (int(row[1]) * float(row[2]))
        costo_total = costo_total + costo_por_cajones
    return costo_total
    f.close()
costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo) 
