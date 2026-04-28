#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Urban Tree Analysis - Data Wrangling & Visualization
Focus: Correlation between height and diameter in species of Buenos Aires.
"""

import csv
import os
import numpy as np
import matplotlib.pyplot as plt

def leer_arboles(nombre_archivo):
    """
    Reads a CSV file and returns a list of dictionaries, 
    one for each tree in the dataset.
    """
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as f:
            filas = csv.reader(f)
            encabezados = next(filas)
            arboles = [{encab: val for encab, val in zip(encabezados, fila)} for fila in filas]
        return arboles
    except FileNotFoundError:
        print(f"Error: File {nombre_archivo} not found.")
        return []

def obtener_medidas(especies, arboleda):
    """
    Extracts height and diameter for a list of species.
    Returns a dictionary: {species_name: [(height, diameter), ...]}
    """
    return {
        especie: [
            (float(arbol['altura_tot']), float(arbol['diametro'])) 
            for arbol in arboleda if arbol['nombre_com'] == especie
        ] for especie in especies
    }

def scatter_plot_especie(especie, datos):
    """
    Generates a scatter plot for height vs diameter of a specific species.
    """
    if not datos:
        return

    medidas = np.array(datos)
    alto = medidas[:, 0]
    diam = medidas[:, 1]

    plt.figure(figsize=(8, 6))
    plt.scatter(diam, alto, alpha=0.3, s=50, c=np.random.rand(len(alto)))
    
    plt.xlim(0, 150) # Adjusted limits for better visualization
    plt.ylim(0, 50)
    plt.xlabel("Diameter (cm)")
    plt.ylabel("Height (m)")
    plt.title(f"Height-Diameter Correlation: {especie}")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def main():
    # Define file path (ensuring compatibility across OS)
    file_path = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    
    # Load Data
    arboleda = leer_arboles(file_path)
    if not arboleda:
        return

    especies_interes = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    diccionario_medidas = obtener_medidas(especies_interes, arboleda)

    # Visualization
    for especie in especies_interes:
        print(f"Plotting data for: {especie} ({len(diccionario_medidas[especie])} specimens)")
        scatter_plot_especie(especie, diccionario_medidas[especie])

if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt

def medidas_de_especies(especies, arboleda):
    diccionario_medidas = {}
    for especie in especies:
        diccionario_medidas[especie] = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
    return diccionario_medidas

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)


#Eucalipto
h0 = np.array(medidas[especies[0]])[:,0]
d0 = np.array(medidas[especies[0]])[:,1]

N = len(medidas)
colors = np.random.rand(N)
plt.scatter(d0, h0, c = colors, alpha = 0.3, s=50)
plt.xlim(0,30) 
plt.ylim(0,100)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Eucalipto")
plt.show()

#Palo borracho rosado
h1 = np.array(medidas[especies[1]])[:,0]
d1 = np.array(medidas[especies[1]])[:,1]

N = len(medidas)
colors = np.random.rand(N)
plt.scatter(d1, h1, c = colors, alpha = 0.3, s=50)
plt.xlim(0,30) 
plt.ylim(0,100)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Palo borracho rosado")
plt.show()

#Jacaranda
h2 = np.array(medidas[especies[2]])[:,0]
d2 = np.array(medidas[especies[2]])[:,1]

N = len(medidas)
colors = np.random.rand(N)
plt.scatter(d2, h2, c = colors, alpha = 0.3, s=50)
plt.xlim(0,30) 
plt.ylim(0,100)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandá")
plt.show()
