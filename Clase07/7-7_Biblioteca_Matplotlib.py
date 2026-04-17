#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:26:37 2021

@author: salo
"""
"""
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt

# Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
#plt.figure(figsize=(8, 6), dpi=80)
#Cambio: Tamaño de la figura apaisada
plt.figure(figsize=(10, 6), dpi=80)

# Crea un nuevo subplot, en una grilla de 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plotea el coseno con una línea azul contínua de ancho 1 (en pixeles)
#plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
#Cambio: coseno azul, linea mas gruesa
#cambio2: pongamosle un titulo
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="coseno")

# Plotea el seno con una línea verde contínua de ancho 1 (en pixeles)
#plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")
#Cambio: seno rojo y linea mas gruesa
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="seno")

#añadimos leyenda
plt.legend(loc='upper left')

# Rango del eje x
#plt.xlim(-4.0, 4.0)
#Cambio: limites de los ejes
plt.xlim(X.min() * 1.1, X.max() * 1.1)

# Ponemos marcas (ticks) en el eje x
#plt.xticks(np.linspace(-4, 4, 9))
#Cambio: destacar valores interesantes en eje x
#plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
#Cambio2: Texto en la marcas del eje x
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# Rango del eje y
#plt.ylim(-1.0, 1.0)
#Cambio: limites de los ejes
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# Ponemos marcas (ticks) en el eje y
#plt.yticks(np.linspace(-1, 1, 5))
#Cambio: destacar valores interesantes en eje y
#plt.yticks([-1, 0, +1])
#CAmbio2: texto en el rango del eje y
plt.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])

#Mover el contorno
ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#Anotamos puntos interesantes. 
#Vamos a marcar algunos puntos interesantes usando el comando annotate. 
#Elegimos el valor 2π/3 y queremos marcar tanto el seno como el coseno. 
#Vamos a dibujar una marca en la curva y una línea recta punteada. 
#Además, vamos a usar annotate para mostrar texto y una flecha para destacar el valor de las funciones.
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ],[np.sin(t), ], 50, color='red')

plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#El diablo está en los detalles
#Los ejes tapan los trazos de las funciones seno y coseno, y estas tapan los valores escritos sobre los ejes.
#=> Marcas y textos más grandes y semi-transparentes
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65)) 


# Podemos grabar el gráfico (con 72 dpi)
# plt.savefig("ejercicio_2.png)", dpi=72)
    
    
#plt.close(1)     # Cierra la figura 1
"""
#Funcion para convertir distancia de cm a pulgadas
def cm2inch(value):
    return value/2.54

fig = plt.figure(figsize=(cm2inch(12.8), cm2inch(9.6)))
"""
# Mostramos el resultado en pantalla
plt.show()
