"""Lucas Aguiar. Programación 1. 12/11/2024.
Desafío 3: 
Tienes una lista de números en la que algunos elementos están repetidos. 
Desarrolla un programa que elimine todos los elementos duplicados y deje únicamente una aparición de cada uno. La salida debe mostrar la lista original y la lista sin duplicados."""

# Primera lista 

lista_original = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]

# Creamos una lista vacía para almacenar los elementos sin duplicados

lista_sin_duplicados = []

# Iteramos sobre cada elemento de la lista original

for elemento in lista_original:

    # Verificamos si el elemento ya existe en la lista sin duplicados

    if elemento not in lista_sin_duplicados:
        # Si no existe, lo agregamos a la lista
        
        lista_sin_duplicados.append(elemento)
    
# Mostramos la lista original y la lista sin duplicados

print(f"La lista original es: {lista_original}")
print(f"La lista sin duplicados es: {lista_sin_duplicados}")
