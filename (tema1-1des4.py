def verificar_multiplos(numero):
    es_multiplo_de_2 = numero % 2 == 0
    es_multiplo_de_3 = numero % 3 == 0
    es_multiplo_de_5 = numero % 5 == 0
    es_multiplo_de_7 = numero % 7 == 0
    es_multiplo_de_9 = numero % 9 == 0
    es_multiplo_de_10 = numero % 10 == 0
    es_multiplo_de_11 = numero % 11 == 0

    print(f"El número {numero} es múltiplo de:")
    print(f"2: {es_multiplo_de_2}")
    print(f"3: {es_multiplo_de_3}")
    print(f"5: {es_multiplo_de_5}")
    print(f"7: {es_multiplo_de_7}")
    print(f"9: {es_multiplo_de_9}")
    print(f"10: {es_multiplo_de_10}")
    print(f"11: {es_multiplo_de_11}")

# Solicitar al usuario ingresar un número
numero_ingresado = int(input("Ingresa un número para verificar si es múltiplo de 2, 3, 5, 7, 9, 10 y 11: "))

# Llamar a la función para verificar los múltiplos
verificar_multiplos(numero_ingresado)
