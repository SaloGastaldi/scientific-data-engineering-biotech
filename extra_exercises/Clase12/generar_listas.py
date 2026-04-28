#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:06:35 2021

@author: salo
"""
import random

def generar_lista(N):
    lista=[]
    for i in range(N):
        lista.append(random.randint(1,1000)) 
    return lista



listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))
    
print(listas)