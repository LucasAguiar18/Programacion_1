"""Lucas Aguiar.Programación 1. 15/08/2024. Utiliza el módulo `random` para crear un programa que genere un número aleatorio entre 1 y 100."""
#primero se importa el modulo random
import random

# se crea la variable que generara el numero aleatorio entre 1 y 100
def generear_numero_aleatorio():
  numero_aleatorio = random.randint(1, 100)
  return numero_aleatorio

#se muestra el numero aleatorio

numero_aleatorio = generear_numero_aleatorio()
print(f"El numero aleatorio es, {numero_aleatorio}")
