#Ejercicio 2.7: Buscar precios
#buscar_precios.py

def buscar_precio(fruta_verdura):
    f = open('/home/salo/Documentos/Cursos/Python_2021/Ejercicios/ejercicios_python/Data/precios.csv', 'rt')
    precio_encontrado = None
    for line in f:
        line = line.rstrip('\n')
        row = line.split(',')
        if row[0] == fruta_verdura:
            precio_encontrado = row[1]
    if precio_encontrado != None:
        print(f'El precio de un cajón de {fruta_verdura} es: {precio_encontrado}')            
    else:   
        print(f'{fruta_verdura} no figura en el listado de precios.')
    f.close()

precio_encontrado = buscar_precio('Frambuesa')
precio_encontrado_kale = buscar_precio('Kale')

