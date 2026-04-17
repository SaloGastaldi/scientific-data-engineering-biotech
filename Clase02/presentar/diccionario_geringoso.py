#Ejercicio 1.18: Geringoso
#Geringoso.py
def geringoso(cadena):
    aeiou = 'aeiou'
    capadepenapa = ''
    for c in cadena:
        if c in aeiou:
            capadepenapa = capadepenapa + c + 'p' + c
        else:
            capadepenapa = capadepenapa + c
    return capadepenapa


lista = ['banana', 'manzana', 'mandarina']
diccionario_geringoso = {}

for palabra in lista:
    palabra_traducida = geringoso(palabra)
    diccionario_geringoso[palabra] = palabra_traducida
print(diccionario_geringoso) 



        
