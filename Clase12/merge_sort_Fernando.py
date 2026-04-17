def merge_sort(lista):
    comps = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])[0]
        der = merge_sort(lista[medio:])[0]       
        lista_nueva, comps= merge(izq, der, comps = comps)
    return lista_nueva, comps
def merge(lista1, lista2, comps = 0):
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        comps += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado, comps




Esto no debería devolverte
izq, comps_izq  y
der, zomps_der?
y luego sumar esas comp_izq + zomp_der?
izq = merge_sort(lista[:medio])[0]
der = merge_sort(lista[medio:])[0]  
