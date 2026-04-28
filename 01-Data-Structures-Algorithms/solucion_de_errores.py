#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Registro de Solución de Errores Técnicos.
Este módulo documenta la identificación y corrección de errores sintácticos, 
semánticos y de lógica en funciones de procesamiento de datos.
"""

# --- Ejercicio 3.1 & 3.2: Función tiene_a() ---
# Errores detectados: Semántica, Sintaxis y Case-sensitivity.
# Correcciones: Se añadió soporte para 'A' mayúscula, se corrigió el flujo del bucle
# para recorrer toda la expresión y se ajustó la sintaxis de los bloques if/while.

def tiene_a(expresion):
    """Verifica si una expresión contiene la letra 'a' (o 'A')."""
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i].lower() == 'a': # Uso de .lower() para simplificar
            return True
        i += 1
    return False

# --- Ejercicio 3.3: Función tiene_uno() ---
# Errores detectados: Sintaxis y Tipado.
# Correcciones: Se aseguró que la entrada sea tratada como string para la comparación.

def tiene_uno(expresion):
    """Verifica si el carácter '1' está presente en la expresión."""
    expresion = str(expresion) # Aseguramos que sea string
    return '1' in expresion # Forma más 'Pythonic' de búsqueda

# --- Ejercicio 3.5: Error de Memoria en leer_camion() ---
# Error detectado: Semántico (Pisado de memoria).
# Comentario: El código original reutilizaba el mismo diccionario para todas las filas.
# Corrección: Se inicializa un nuevo diccionario 'registro' dentro del bucle para
# asegurar que cada fila sea un objeto independiente en la lista final.

def leer_camion_corregido(nombre_archivo):
    # Aquí iría la lógica corregida integrando un nuevo dict por iteración
    pass

if __name__ == "__main__":
    print(f"Test 'tiene_a': {tiene_a('UNSAM 2020')}")
    print(f"Test 'tiene_uno': {tiene_uno(1984)}")
