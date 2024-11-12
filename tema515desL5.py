"""Lucas Aguiar. Programación 1. 12/11/2024. 
Desafío 5: 
Usa una "list comprehension" para crear una lista llamada potencias que contenga las potencias de 2 de los números del 0 al 9 
(es decir, 2 elevado a la potencia de cada número). Imprime la lista resultante."""

# Utilizamos una lista comprehension para crear la lista de potencias

potencias = [2 ** i for i in range(10)]

# Imprimimos la lista

print(f"La lista de potencias es: {potencias}")
