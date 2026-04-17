numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
        print('No es válido. Intentá de nuevo.')
        raise RuntimeError('¡Qué moco!')
print(f'Ingresaste {n}.')
