#Ejercicio 4.8:Invertir una lista
#invlista.py

def invertir_lista(lista):
    invertida = []
    i = -1
    for e in lista:
        elemento = lista[i]
        invertida.append(elemento)
        i -= 1
    return invertida

lista = [1, 2, 3, 4, 5]
lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

print(invertir_lista(lista))
print(invertir_lista(lista2))
