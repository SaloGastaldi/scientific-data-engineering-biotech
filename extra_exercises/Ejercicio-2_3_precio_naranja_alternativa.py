#Ejercicio 2.3: Precio de la naranja
#Ejercicio-2_3_precio_naranja.py
f = open('../Data/precios.csv', 'rt')
next(f)
for line in f:
    line = line.rstrip('\n')
    row = line.split(',')
    fruta = row[0]
    if fruta == 'Naranja':
        precio_fruta = row[1]        
        print(f'El precio de la naranja es: {precio_fruta}')
f.close()





