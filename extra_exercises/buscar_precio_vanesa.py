#Buscar precios
def buscar_precio(fruta):
    with open ('../Data/precios.csv', 'rt') as f:
        for line in f:
            lista = line.split(',')           
            if lista[0] == fruta:  
                precio = lista[1]              
                print(f'El precio de un cajon de {fruta} es: {precio}') 
                return precio                
#            else:
#                print(f'{fruta} no figura en el listado de precios')
    return print(f'{fruta} no figura en el listado de precios')               
           
precio_de_fruta = buscar_precio('Frambuesa')
print(precio_de_fruta)
