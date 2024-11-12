"""Lucas Aguiar. Programación 1. 11/11/2024
Desafío 2: 
Crea un programa que tome una lista de valores y realice operaciones matemáticas sobre ellos. 
Implementa el manejo de varias excepciones comunes como ZeroDivisionError, TypeError, y ValueError."""

try:
    # Ingresamos una lista de valores
    valores = [1, 2, 3, 4, 5]

    #Crear un menu para que el usuario elina una operacion para hacer
    print("Elija una operación:")
    print("1. Sumar")
    print("2. Multiplicar")
    print("3. Dividir")
    print("4. Salir")

    opcion = int(input("Ingrese el número de la opción: "))

    if opcion == 4:
        print("Saliendo del programa...")
        exit()
    
    if opcion == 1:
    # Calculamos la suma de los valores, solicitamos al usuario que elija dos numero que esten en la lista 
        print("La lista de valores ingresada es:", valores)
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num1 not in valores or num2 not in valores:
        raise ValueError("Los valores ingresados no están en la lista")
    
    # Calculamos la suma
    suma = num1 + num2
    print("La suma de", num1, "y", num2, "es:", suma) 
except ValueError:
    print("Error: Los valores ingresados no están en la lista")

    if opcion == 2:
    # Calculamos la multiplicacion de los valores, solicitamos al usuario que elija dos numero que esten en la lista
        print("La lista de valores ingresada es:", valores)
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num1 not in valores or num2 not in valores:
        raise ValueError("Los valores ingresados no están en la lista")
    
    # Calculamos la multiplicacion
    multiplicacion = num1 * num2
    print("La multiplicación de", num1, "y", num2, "es:", multiplicacion)
except TypeError:
    print("Error: Los valores ingresados no son numéricos")
    
    if opcion == 3:
    # Calculamos la division de los valores, solicitamos al usuario que elija dos numero que esten en la lista
        print("La lista de valores ingresada es:", valores)
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num1 or num2 == 0:
        raise ValueError("No se puede dividir por 0")
    
    # Calculamos la division
    division = num1 / num2
    print("La division de", num1, "y", num2, "es:", division)

except ZeroDivisionError:
    print("Error: No se puede dividir entre 0")
