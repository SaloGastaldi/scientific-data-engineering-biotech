#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:31:11 2021

@author: salo
"""

#Ejercicio 7.9: Subplots fuera de una grilla
import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la tercera de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])
plt.show()


#Ejercicio 7.10: caminatas al azar
#random_walk.py
import numpy as np
import matplotlib.pyplot as plt

#una caminata al azar de N 
def randomwalk(largo):
    pasos = np.random.randint (-1,2, largo)  
    return pasos.cumsum()

#12 caminatas al azar de N pasos
N = 100000
max_caminatas = []
caminatas = []
for i in range(12):
    caminata = randomwalk(N)
    max_caminata = max(abs(caminata))
    caminatas.append(caminata)
    max_caminatas.append(max_caminata)  
    
    
#caminata que más se aleja y caminata que menos se aleja
mas_se_aleja = max(max_caminatas)
menos_se_aleja = min(max_caminatas)
for caminata in caminatas:
    if max(abs(caminata)) == mas_se_aleja:
        caminata_mas_se_aleja = caminata
    if max(abs(caminata)) == menos_se_aleja:
        caminata_menos_se_aleja = caminata
        
        
#Grafico grande superior
plt.figure(figsize=(10, 6), dpi=80)
plt.subplot(2, 1, 1)                         # define la figura de arriba
plt.yticks([-500, 0, +500],
          [r'$-500$', r'$0$', r'$+500$'])   #Resalta valores que nos interesa
plt.xticks([])                              #saca marcas del eje x
plt.ylim(-1000, 1000)                       #define limites en el eje x
ax = plt.gca()                              #Pone titulo al grafico
ax.set(title='12 Caminatas al azar')

for caminata in caminatas:
    plt.plot(caminata)


#Grafico chico abajo izquierda
plt.subplot(2, 2, 3)                       
plt.yticks([-500, 0, +500],                
          [r'$-500$', r'$0$', r'$+500$'])
plt.xticks([])                             
plt.ylim(-1000, 1000) 
ax = plt.gca()                              
ax.set(title='La caminata que más se aleja')
plt.plot(caminata_mas_se_aleja)
#Grafico chico abajo derecha                   
plt.subplot(2, 2, 4) # define la segunda de abajo
plt.ylim(-1000, 1000)
plt.xticks([]), plt.yticks([])
ax = plt.gca()                              
ax.set(title='La caminata que menos se aleja')
plt.plot(caminata_menos_se_aleja)
plt.show()


#Ejercicios Optativos
#Ejercicio 7.11: Gráficos de barras
import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + 0.1, y + 0.05, '%.2f' % y, ha='center', va= 'bottom')

for x, y in zip(X, Y2):
    plt.text(x + 0.1, -y - 0.05, '%.2f' % y, ha='center', va= 'top')

plt.xlim(-.5, n)
plt.xticks([])
plt.ylim(-1.25, 1.25)
plt.yticks([])

plt.show()

#Ejercicio 7.12: coordenadas polares
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes([0, 0, 1, 1], polar=True)

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r,bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r/10.))
    bar.set_alpha(0.5)

ax.set_xticklabels([])
ax.set_yticklabels([])
plt.show()


#Ejercicio 7.13: Setear el color de un scatter plot
import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks([])
plt.ylim(-1.5, 1.5)
plt.yticks([])

plt.show()
