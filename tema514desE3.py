"""Lucas Aguiar. Programación 1. 12/11/2024
Desafío 3: 
Escribe una función que calcule el factorial de un número entero positivo.
 Maneja las excepciones si el número ingresado es negativo, no es entero, o es demasiado grande para ser procesado."""

def factorial(n):
    # Validamos que el número sea entero positivo
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número ingresado debe ser un entero positivo")
    
    # Validamos que el número no sea demasiado grande para ser procesado
    if n > 100:
        raise OverflowError("El número ingresado es demasiado grande para calcular el factorial")
    
    # Calculamos el factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

try:
    # Solicitamos un número al usuario
    numero = int(input("Ingrese un número entero positivo: "))
    
    # Calculamos el factorial
    resultado = factorial(numero)
    
    # Mostramos el resultado
    print(f"El factorial de {numero} es: {resultado}")

except ValueError as error_valor:
    print(f"Error: {error_valor}")

except OverflowError as error_overflow:
    print(f"Error: {error_overflow}")
