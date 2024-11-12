"""Lucas Aguiar. Programación 1. 12/11/2024
Desafío 4: 
Crea una excepción personalizada llamada NegativeNumberError que se dispare si el usuario intenta ingresar un número negativo en un programa de cálculo de raíces cuadradas.
 Implementa el manejo de esta excepción en el programa."""

class NegativeNumberError(Exception):
    def __init__(self, message="El número ingresado no puede ser negativo"):
        super().__init__(message)

try:
    # Solicitamos un número al usuario
    numero = float(input("Ingrese un número: "))
    
    # Validamos que el número sea positivo
    if numero < 0:
        raise NegativeNumberError()
    
    # Calculamos la raíz cuadrada
    raiz = numero ** 0.5
    
    # Mostramos el resultado
    print(f"La raíz cuadrada de {numero} es: {raiz}")

except NegativeNumberError as error:
    print(f"Error: {error}")

except ValueError:
    print("Error: Debe ingresar un número")

