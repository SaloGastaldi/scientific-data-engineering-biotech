#Ejercicio 4.9: Propagación
#propaga.py
 
lista = [0, 0, 0, 1, 0, 0]
lista2 = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
"""
def propaga_derecha(fosforos):
    n = len(fosforos)
    for i in range(n-1):
        if fosforos[i] == 1 and fosforos[i+1] == 0:
             fosforos[i+1] = 1
    return fosforos
    
print(propaga_derecha(lista))
print(propaga_derecha(lista2))

def propaga_izquierda(fosforos):
    n = len(fosforos)
    for i in range(n-1, 0, -1):
        if fosforos[i] == 1 and fosforos[i-1] == 0:
            fosforos[i-1] = 1
    return fosforos

print(propaga_izquierda(lista))
print(propaga_izquierda(lista2))
   
"""

def propaga(fosforos):
    n = len(fosforos)
    for i in range(n-1):
        if fosforos[i] == 1 and fosforos[i+1] == 0:
             fosforos[i+1] = 1
    for i in range(n-1, 0, -1):
        if fosforos[i] == 1 and fosforos[i-1] == 0:
            fosforos[i-1] = 1
    return fosforos

print(propaga(lista))
print(propaga(lista2))