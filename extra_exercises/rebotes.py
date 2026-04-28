# Ejercicio 1.5: Pelota
# rebotes.py
altura_arrojada = 100                     # altura en metros
num_rebotes = 1

while num_rebotes <= 10:
    print(num_rebotes, round (altura_arrojada * 0.6**num_rebotes, 4))
    num_rebotes = num_rebotes + 1 
