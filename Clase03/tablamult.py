#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 08:45:58 2021

@author: salo
"""
#Ejercicio 3.17: Tabla de multiplicar
#tablamult.py
#Comentario: seguramente se pueda escribir el código de una forma más simplificada, con una función que haga exactamente lo que hice. Lo cuál no logré hacer, así que, aquí va de la forma que me salió!
"""
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
cero_0 = numeros[0]
uno_0 = cero_0 + numeros[0]
dos_0 = uno_0 + numeros[0]
tres_0 = dos_0 + numeros[0]
cuatro_0 = tres_0 + numeros[0]
cinco_0 = cuatro_0 + numeros[0]
seis_0 = cinco_0 + numeros[0]
siete_0 = seis_0 + numeros[0]
ocho_0 = siete_0 + numeros[0]
nueve_0 = ocho_0 + numeros[0]

cero_1 = 0
uno_1 = numeros[1]
dos_1 = uno_1 + numeros[1]
tres_1 = dos_1 + numeros[1]
cuatro_1 = tres_1 + numeros[1]
cinco_1 = cuatro_1 + numeros[1]
seis_1 = cinco_1 + numeros[1]
siete_1 = seis_1 + numeros[1]
ocho_1 = siete_1 + numeros[1]
nueve_1 = ocho_1 + numeros[1]

cero_2 = 0
uno_2 = numeros[2]
dos_2 = uno_2 + numeros[2]
tres_2 = dos_2 + numeros[2]
cuatro_2 = tres_2 + numeros[2]
cinco_2 = cuatro_2 + numeros[2]
seis_2 = cinco_2 + numeros[2]
siete_2 = seis_2 + numeros[2]
ocho_2 = siete_2 + numeros[2]
nueve_2 = ocho_2 + numeros[2]

cero_3 = 0
uno_3 = numeros[3]
dos_3 = uno_3 + numeros[3]
tres_3 = dos_3 + numeros[3]
cuatro_3 = tres_3 + numeros[3]
cinco_3 = cuatro_3 + numeros[3]
seis_3 = cinco_3 + numeros[3]
siete_3 = seis_3 + numeros[3]
ocho_3 = siete_3 + numeros[3]
nueve_3 = ocho_3 + numeros[3]

cero_4 = 0
uno_4 = numeros[4]
dos_4 = uno_4 + numeros[4]
tres_4 = dos_4 + numeros[4]
cuatro_4 = tres_4 + numeros[4]
cinco_4 = cuatro_4 + numeros[4]
seis_4 = cinco_4 + numeros[4]
siete_4 = seis_4 + numeros[4]
ocho_4 = siete_4 + numeros[4]
nueve_4 = ocho_4 + numeros[4]

cero_5 = 0
uno_5 = numeros[5]
dos_5 = uno_5 + numeros[5]
tres_5 = dos_5 + numeros[5]
cuatro_5 = tres_5 + numeros[5]
cinco_5 = cuatro_5 + numeros[5]
seis_5 = cinco_5 + numeros[5]
siete_5 = seis_5 + numeros[5]
ocho_5 = siete_5 + numeros[5]
nueve_5 = ocho_5 + numeros[5]

cero_6 = 0
uno_6 = numeros[6]
dos_6 = uno_6 + numeros[6]
tres_6 = dos_6 + numeros[6]
cuatro_6 = tres_6 + numeros[6]
cinco_6 = cuatro_6 + numeros[6]
seis_6 = cinco_6 + numeros[6]
siete_6 = seis_6 + numeros[6]
ocho_6 = siete_6 + numeros[6]
nueve_6 = ocho_6 + numeros[6]

cero_7 = 0
uno_7 = numeros[7]
dos_7 = uno_7 + numeros[7]
tres_7 = dos_7 + numeros[7]
cuatro_7 = tres_7 + numeros[7]
cinco_7 = cuatro_7 + numeros[7]
seis_7 = cinco_7 + numeros[7]
siete_7 = seis_7 + numeros[7]
ocho_7 = siete_7 + numeros[7]
nueve_7 = ocho_7 + numeros[7]

cero_8 = 0
uno_8 = numeros[8]
dos_8 = uno_8 + numeros[8]
tres_8 = dos_8 + numeros[8]
cuatro_8 = tres_8 + numeros[8]
cinco_8 = cuatro_8 + numeros[8]
seis_8 = cinco_8 + numeros[8]
siete_8 = seis_8 + numeros[8]
ocho_8 = siete_8 + numeros[8]
nueve_8 = ocho_8 + numeros[8]

cero_9 = 0
uno_9 = numeros[9]
dos_9 = uno_9 + numeros[9]
tres_9 = dos_9 + numeros[9]
cuatro_9 = tres_9 + numeros[9]
cinco_9 = cuatro_9 + numeros[9]
seis_9 = cinco_9 + numeros[9]
siete_9 = seis_9 + numeros[9]
ocho_9 = siete_9 + numeros[9]
nueve_9 = ocho_9 + numeros[9]



print(f'{cero_0:7d} {uno_1:4d} {uno_2:>4d} {uno_3:>4d} {uno_4:>4d} {uno_5:>4d} {uno_6:>4d} {uno_7:>4d} {uno_8:>4d} {uno_9:>4d}')
print(f'----------------------------------------------------')
print(f'0: {cero_0:>4d} {uno_0:>4d} {dos_0:>4d} {tres_0:>4d} {cuatro_0:>4d} {cinco_0:>4d} {seis_0:>4d} {siete_0:>4d} {ocho_0:>4d} {nueve_0:>4d}') 
print(f'1: {cero_1:>4d} {uno_1:>4d} {dos_1:>4d} {tres_1:>4d} {cuatro_1:>4d} {cinco_1:>4d} {seis_1:>4d} {siete_1:>4d} {ocho_1:>4d} {nueve_1:>4d}')
print(f'2: {cero_2:>4d} {uno_2:>4d} {dos_2:>4d} {tres_2:>4d} {cuatro_2:>4d} {cinco_2:>4d} {seis_2:>4d} {siete_2:>4d} {ocho_2:>4d} {nueve_2:>4d}')
print(f'3: {cero_3:>4d} {uno_3:>4d} {dos_3:>4d} {tres_3:>4d} {cuatro_3:>4d} {cinco_3:>4d} {seis_3:>4d} {siete_3:>4d} {ocho_3:>4d} {nueve_3:>4d}')
print(f'4: {cero_4:>4d} {uno_4:>4d} {dos_4:>4d} {tres_4:>4d} {cuatro_4:>4d} {cinco_4:>4d} {seis_4:>4d} {siete_4:>4d} {ocho_4:>4d} {nueve_4:>4d}')
print(f'5: {cero_5:>4d} {uno_5:>4d} {dos_5:>4d} {tres_5:>4d} {cuatro_5:>4d} {cinco_5:>4d} {seis_5:>4d} {siete_5:>4d} {ocho_5:>4d} {nueve_5:>4d}')
print(f'6: {cero_6:>4d} {uno_6:>4d} {dos_6:>4d} {tres_6:>4d} {cuatro_6:>4d} {cinco_6:>4d} {seis_6:>4d} {siete_6:>4d} {ocho_6:>4d} {nueve_6:>4d}')
print(f'7: {cero_7:>4d} {uno_7:>4d} {dos_7:>4d} {tres_7:>4d} {cuatro_7:>4d} {cinco_7:>4d} {seis_7:>4d} {siete_7:>4d} {ocho_7:>4d} {nueve_7:>4d}')
print(f'8: {cero_8:>4d} {uno_8:>4d} {dos_8:>4d} {tres_8:>4d} {cuatro_8:>4d} {cinco_8:>4d} {seis_8:>4d} {siete_8:>4d} {ocho_8:>4d} {nueve_8:>4d}')
print(f'9: {cero_9:>4d} {uno_9:>4d} {dos_9:>4d} {tres_9:>4d} {cuatro_9:>4d} {cinco_9:>4d} {seis_9:>4d} {siete_9:>4d} {ocho_9:>4d} {nueve_9:>4d}')
"""
#Ejercicio 3.17: Tabla de multiplicar
#tablamult.py
#Comentario: código simplificado del codigo anterior!
def tabla(N):
    print('      ', end='')
    
    for j in range(N):
        print(f'{j:>5}', end='')
        
    print('\n','---------------------------------------------------------')    
    for x in range(N):
        valor = 0
        print()
        print(f'{x:>5}:', end='')
        for y in range(N):
            print(f'{valor:>5}', end='')
            valor = valor + x

tabla(10)

