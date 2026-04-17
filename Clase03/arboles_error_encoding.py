#Ejercicio 3.18: Lectura de los Arboles de un parque
import csv

from collections import Counter

def leer_parque(nombre_archivo, parque):
    arboles = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            if record['espacio_ve'] == parque:
                arboles.append(record)
    return arboles

parque_general_paz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
parque_los_andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
parque_centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

#Ejercicio 3.19: Determinar las especies en un parque

def especies(lista_arboles):
    especies = []
    for arbol in lista_arboles:
        especies.append(arbol['nombre_com'])
    unicos_especies = set(especies)
    return(unicos_especies)

#Ejercicio 3.20: Contar ejemplares por especie

def contar_ejemplares(lista_arboles):
    ejemplares = Counter()
    for arbol in lista_arboles:
        ejemplares[arbol['nombre_com']] += 1
    return ejemplares.most_common(5)

#Ejercicio 3.21: Alturas de una especien en una lista

def obtener_alturas(lista_arboles, especie):
    lista_alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista_alturas.append(float(arbol['altura_tot']))
    return lista_alturas

alturas_general_paz = obtener_alturas(parque_general_paz, 'Jacarandá')
altura_maxima_general_paz = max(alturas_general_paz)
altura_promedio_general_paz = sum(alturas_general_paz) / len(alturas_general_paz)
print(alturas_general_paz)
