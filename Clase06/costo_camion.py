#Ejercicio 6.12: Un poco mas allá => (Ejercicio 2.9: Funciones de la biblioteca MODIFICADO!)
#costo_camion.py
import informe_funciones as informe
def costo_camion(nombre_archivo_camion):
    camion = informe.leer_camion(nombre_archivo_camion)
    costo_total = 0
    for producto in camion:
        cajones = producto['cajones']
        precio = producto['precio']
        costo_por_cajones = cajones * precio
        costo_total = costo_total + costo_por_cajones
    return costo_total
  

