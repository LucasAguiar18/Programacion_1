"""Lucas Aguiar. Programación 1. 11/11/2024
Desafío 1: 
Solicita al usuario dos números enteros e implementa un try-except que maneje la división por cero y los valores no numéricos. 
Muestra mensajes de error apropiados en cada caso."""
try:
    #Solicitamos dos numeros al usuario

    num1 = int(input("ingrese el primer numero entero: "))

    num2 = int(input("ingrese el segundo numero entero: "))




    #Intentamos dividir num1 entre num2
    resultado = num1 / num2
    print(f"El resultado de la division es: {resultado}")

except ValueError:
    #Si se produce un ValueError, es porque uno de los valores ingresados no es un numero
    print("Error: Debe ingresar valores numéricos")

except ZeroDivisionError:
    #Si se produce un ZeroDivisionError, es porque se intentó dividir entre 0
    print("Error: No se puede dividir entre 0")
