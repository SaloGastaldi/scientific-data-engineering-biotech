#Ejercicio 4.6: Búsqueda de un elemento
#busqueda_en_lista.py

def buscar_u_elemento(lista, e):
    pos = -1
    i = 0
    for u in lista:
        if u == e:
            pos = i
        i += 1
    return pos
def buscar_n_elemento(lista, e):
    contador = 0
    for n in lista:
        if n == e:
            contador += 1
        n += 1
    return contador

lista = [1, 2, 3, 2, 3, 4]
print(buscar_u_elemento(lista, 1))
print(buscar_n_elemento(lista, 1))
print(buscar_u_elemento(lista, 2))
print(buscar_n_elemento(lista, 2))
print(buscar_u_elemento(lista, 3))
print(buscar_n_elemento(lista, 3))
print(buscar_u_elemento(lista, 5))
print(buscar_n_elemento(lista, 5))

#Ejercicio 4.7:Búsqueda de máximo y mínimo
def maximo(lista):
    m = lista[0] 
    for e in lista:
        if e > m:
            m = e
        e += 1
    return m

def minimo(lista):
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
        e += 1
    return m
lista_2 = [1, 2, 7, 2, 3, 4]
lista_3 = [1, 2, 3, 4]
lista_4 = [-5, 4]
lista_5 = [-5, -4]
print(maximo(lista_2))
print(maximo(lista_3))
print(maximo(lista_4))
print(maximo(lista_5))
print(minimo(lista_2))
print(minimo(lista_3))
print(minimo(lista_4))
print(minimo(lista_5))
