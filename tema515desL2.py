"""Lucas Aguiar. Programación 1. 12/11/2024.
Desafío 2: 
Un sistema de inventario tiene una lista con los códigos de productos. 
Desarrolla un programa que permita al usuario introducir un código de producto y que determine si ese código está en la lista. 
Si el código se encuentra, el programa debe devolver la posición en la que aparece; si no está, debe mostrar un mensaje indicando que no se ha encontrado el código."""

#Lista con los codigos

codigos = ["A01", "B02", "C03", "D04", "E05"]

#Mostramos la lista de los codigos

print (f"La lista de los codigos es: {codigos}")

#Solicitamos el codigo al usuario

codigo_usuario = input("Ingrese el código del producto: ")

#Buscamos el codigo en la lista

if codigo_usuario in codigos:
    posicion = codigos.index(codigo_usuario)
    print(f"El código {codigo_usuario} se encuentra en la posición {posicion+1}")
else:
    print(f"El código {codigo_usuario} no se ha encontrado en la lista")
