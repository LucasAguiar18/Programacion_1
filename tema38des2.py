"""Lucas Aguiar. Programación 1. 15/8/2024. Utiliza el módulo `random` de Python para crear un programa que genere una contraseña aleatoria de 8 caracteres que incluya letras minúsculas, letras mayúsculas y números."""

import random
import string

#definimos la funcion que genere la contraseña
def generar_contrasena():
  
  #definimos como va a estar compuesta la contraseña
  
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for _ in range(8))
    return contrasena

#llamamos a la funcion para generar la contraseña
contrasena_generada = generar_contrasena()
#imprimimos la contraseña generada
print("Esta es su contraseña generada:", contrasena_generada)
