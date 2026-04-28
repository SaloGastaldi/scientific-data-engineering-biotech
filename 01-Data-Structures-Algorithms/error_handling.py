#Ejercicio 2.8: Administracion de errores
#def preguntar_edad(nombre):
#    edad = int(input(f'ingresá tu edad {nombre}: '))
#    if edad<0:
#        raise ValueError('La edad no puede ser negativa.')
#    return edad
#
#edad_Salo = preguntar_edad('Salo')
#print(f'Salo, tu edad es {edad_Salo}') 

for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')

#Funcion costo_camion() con archivo que tiene faltantes
#def costo_camion(nombre_archivo):
#    f = open(nombre_archivo, 'rt')
#    headers = next(f).split(',')
#    costo_total = 0
#    for line in f:
#        line = line.rstrip('\n')
#        row = line.split(',')
#        try:
#            costo_por_cajones = int(row[1]) * float(row[2])
#            costo_total = costo_total + costo_por_cajones
#        except:
#            print(f'Warning: datos erroneos en el archivo csv')
#    return costo_total
#    f.close()
#costo = costo_camion('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/missing.csv')
#print('Costo total:', costo)
