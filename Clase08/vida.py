#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:09:15 2021

@author: salo
"""
#Ejercicio 8.1: Segundos vividos
#vida.py
from datetime import datetime

hoy = datetime.now()
fecha_hoy = hoy.strftime('%d/%m/%Y, %H:%M:%S')
print('Fecha actual:', fecha_hoy)

cadena_nacimiento = '17/12/1989'
nacimiento = datetime.strptime(cadena_nacimiento, '%d/%m/%Y')
fecha_nacimiento = nacimiento.strftime('%d/%m/%Y, %H:%M:%S')
print('Fecha de nacimiento:', fecha_nacimiento)

segundos_vividos = hoy - nacimiento
print('Cantidad de segundos vividos:', segundos_vividos.total_seconds())

#Ejercicio 8.2: Cuánto falta
cadena_primavera = '21/09/2021'
primavera = datetime.strptime(cadena_primavera, '%d/%m/%Y')
inicio_primavera = primavera.strftime('%d/%m/%Y')
#print(inicio_primavera)

hoy = datetime.now()
fecha_hoy = hoy.strftime('%d/%m/%Y')
#print(fecha_hoy)

dias = primavera - hoy
print(f'FALTAN {dias.days} DIAS PARA LA PRIMAVERA')

#Ejercicio 8.3: Fecha de reincorporación
from datetime import timedelta
cadena_i = '26-09-2020'
inicio = datetime.strptime(cadena_i, '%d-%m-%Y')
inicio_licencia = inicio.strftime('%d-%m-%Y')
#print(inicio)
print('Inicio de licencia por maternidad:', inicio_licencia)

reincorporacion = inicio + timedelta(days=200)
fin_licencia = reincorporacion.strftime('%d-%m-%Y')

print('Reincorporacion al trabajo:', fin_licencia)

#Ejercicio 8.4: Días hábiles

def dias_habiles(inicio, fin, feriados):
    '''
    Lista de fechas de dias habiles
    Pre: fecha inicio, fecha fin, lista de fechas correspondiente a los dias feriados
    Pos: lista de fechas de dias habiles
    '''
    formato_fecha = '%d/%m/%Y'
    fecha_inicio = datetime.strptime(inicio, formato_fecha)
    fecha_fin = datetime.strptime(fin, formato_fecha)
    diferencia = fecha_fin - fecha_inicio
    dias = diferencia.days
    fechas = []
    for days in range(dias+1):                         #para cada dia en el rango de dias entre las fecha inicio y fin
        fecha =  fecha_inicio + timedelta(days = days) #fecha nueva
        fecha_form = fecha.strftime(formato_fecha)     #da formato a la fecha nueva
        if fecha.weekday() < 5 and fecha_form not in feriados:                        #si la fecha nueva corresponde a un dia de la semana(ni sabado, ni domingo)
            fechas.append(fecha_form)                  #entonces, lo agrega a la lista de fechas de dias habiles
    return fechas
    
    

     
    


inicio = '06/05/2021'
fin = '31/12/2021'
feriados = ['12/10/2021', '23/11/2021', '07/12/2021', '08/12/2021', '25/12/2021']
print(dias_habiles(inicio, fin, feriados))

