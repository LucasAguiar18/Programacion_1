"""Lucas Aguiar. Programación 1. 19/08/2024
**Desafio 6:**

Calculadora de Fechas
Objetivo:
Escribir un programa en Python que permita calcular la diferencia entre dos fechas, utilizando el módulo `datetime.`"""

import datetime

#Función para calcular la diferencia entre dos fechas
def calcular_diferencia_fechas(fecha1, fecha2):
    diferencia = fecha2 - fecha1
    return diferencia.days

# Solicitamos una fecha al usuario (dd/mm/aaaa) en ese formato
print("Ingrese la primera fecha (dd/mm/aaaa):")
fecha1_str = input()
fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y")

# Solicitar al usuario la segunda fecha
print("Ingrese la segunda fecha (dd/mm/aaaa):")
fecha2_str = input()
fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y")

# Se calcula la diferencia entre las fechas ingresadas
diferencia = calcular_diferencia_fechas(fecha1, fecha2)

print("La diferencia entre las dos fechas es de", diferencia, "días.")
