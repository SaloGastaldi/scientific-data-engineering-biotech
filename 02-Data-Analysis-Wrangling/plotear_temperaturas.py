#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:59:11 2021

@author: salo
"""
#Ejercicio 5.8: Empezando a plotear
import numpy as np
temperaturas = np.load('../Data/Temperaturas.npy')
import matplotlib.pyplot as plt
plt.hist(temperaturas,bins=10)
plt.show()
