
#Ejercicio 2.7: Buscar precios
#buscar_precio.py

def buscar_precio(fruta_verdura):
    f = open('../Data/precios.csv', 'rt')
    headers = next(f).split(',')
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

precio = buscar_precio('Frambuesa')
