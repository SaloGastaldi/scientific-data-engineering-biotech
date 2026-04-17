#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:48:13 2021

@author: salo
"""

import pandas as pd

#df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv')
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
"""
#Ondas de mareas en el Rio de la Plata
df['12-25-2014':].plot()
#Vientos y ondas de tormenta en el Río de la Plata
df['10-15-2014':'12-15-2014'].plot()
"""
#Ejercicio 8.10
dh = df['12-25-2014':].copy()
delta_t = 0 # tiempo que tarda la marea entre ambos puertos
delta_h = 25.4 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()





'''
#Correlación con desplazamientos
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# Levanto las dos series
df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
# Me quedo con un fregmento
dh=df['10-01-2014':].copy()

# Selecciono los intervalos que voy a usar para desplazar SF
shifts = np.arange(-12,13)
# Genero un vector donde guardar los coeficientes de correlacion para cada deslpazamiento
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(shifts):
    #guardo el coeficiente de correlación r entre de SF desplazada con BA original.
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[12:-12],dh['H_BA'][12:-12])[0]
# ploteo los resultados   
plt.plot(shifts, corrs)
'''