"""Lucas Aguiar. Programación 1. 12/11/2024.
Desafío 1: 
Desarrolla un programa que, dado un conjunto de tres números enteros introducidos por el usuario, determine cuál de ellos es el mayor. 
Considera la posibilidad de que algunos o todos los números sean iguales. 
El programa debe imprimir un mensaje claro con el número mayor o indicar si todos los números son iguales."""

# Solicitamos los tres numeros al usuario

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Comparamos los numeros

if numero1 > numero2 and numero1 > numero3:
    print(f"El número mayor es: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El número mayor es: {numero2}")
elif numero3 > numero1 and numero3 > numero2:
    print(f"El número mayor es: {numero3}")

#Verificar si son iguales

elif numero1 == numero2 and numero1 == numero3:
    print("Todos los números son iguales")

else:
    print("No hay un número mayor")

