"""Lucas Aguiar. Programación 1. 15/8/2024. Investiga y utiliza al menos tres funciones del módulo `string` que puedan ser útiles para mejorar nuestro procesador de texto."""

# Importamos el módulo string para utilizar las funciones que nos interesan

import string

# Solicitamos al usuario que ingrese un texto en minúsculas
texto = input("ingrese un texto en minusculas:")

# Definimos la función para contar la cantidad de palabras en el texto
def contar_palabras(texto):
  palabras_separadas = texto.split()
  return len(palabras_separadas)

print("La cantidad de palabras en el texto es:",contar_palabras (texto))

#Definimos otra función para convertir el texto a mayuscula

def convertir_mayuscula(texto):
  return texto.upper()

print("El texto en mayuscula es:", convertir_mayuscula(texto))

#Definimos otra función para contar puntos y comas en el texto
def contar_puntos_comas(texto):
  puntos_comas = texto.count(".") + texto.count(",")
  return puntos_comas

print("La cantidad de puntos y comas en el texto es:", contar_puntos_comas(texto))