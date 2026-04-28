#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulación de Caminata Aleatoria (Random Walk).
Modelado de procesos estocásticos utilizando NumPy y visualización con Matplotlib.
Ideal para representar movimientos brownianos o difusión molecular.
"""

import numpy as np
import matplotlib.pyplot as plt

def camina(pasos):
    """Genera una trayectoria aleatoria de N pasos."""
    pasos_x = np.random.choice([-1, 0, 1], size=pasos)
    pasos_y = np.random.choice([-1, 0, 1], size=pasos)
    
    # Acumulamos los pasos para obtener la trayectoria
    trayectoria_x = np.cumsum(pasos_x)
    trayectoria_y = np.cumsum(pasos_y)
    
    return trayectoria_x, trayectoria_y

def main():
    n_trayectorias = 8
    n_pasos = 10000
    
    plt.figure(figsize=(10, 8))
    
    for i in range(n_trayectorias):
        x, y = camina(n_pasos)
        plt.plot(x, y, label=f'Partícula {i+1}', alpha=0.7)
    
    plt.title(f"Simulación de {n_trayectorias} Caminatas Aleatorias ({n_pasos} pasos)")
    plt.xlabel("Desplazamiento X")
    plt.ylabel("Desplazamiento Y")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
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
