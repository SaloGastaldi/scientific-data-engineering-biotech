#Ejercicio 3.8: Un ejemplo práctico de enumetare()
#costo_camion.py
"""
import csv
def costo_camion(nombre_archivo):
    f = open('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/missing.csv', 'rt')
    filas = csv.reader(f)
    encabezados = next(filas)
    for n_fila, fila in enumerate(filas, start=1):
        try:
            cajones = int(fila[1])
            precio = float(fila[2])
        except ValueError:
            print(f'Fila {n_fila}: No puede interpretar {fila}')
    f.close()
costo = costo_camion('../Data/missing.csv')
"""
#%%Ejercicio 3.9: La función zip ()
import csv
def costo_camion(nombre_archivo):
    with open('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/fecha_camion.csv', 'rt') as f:
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
    
costo = costo_camion('../Data/fecha_camion.csv')
print(f'Costo total: {costo}')