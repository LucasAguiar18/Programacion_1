"""Lucas Aguiar. Programación 1. 12/11/2024.
Desafío 4: 
Tienes dos listas de números enteros de diferentes longitudes. Desarrolla un programa que sume los elementos de las listas en las posiciones correspondientes. 
Si una lista es más corta que la otra, los elementos que falten deben considerarse como 0 en la suma."""

# Lista 1
lista1 = [1, 2, 3, 4, 5]

# Lista 2
lista2 = [1, 2, 3, 4, 5]

# Lista de resultado
lista_resultado = []

#sumamos las listas por columnas 

for i in range(max(len(lista1), len(lista2))):

        # Obtenemos el elemento de la lista 1 en la posición i
        elemento1 = lista1[i] if i < len(lista1) else 0

        # Obtenemos el elemento de la lista 2 en la posición i
        elemento2 = lista2[i] if i < len(lista2) else 0
        
        # Sumamos los elementos y agregamos el resultado a la lista de resultado
        lista_resultado.append(elemento1 + elemento2)

print(f"La lista 1 es: {lista1}")

print(f"La lista 2 es: {lista2}")

print(f"La lista de resultado es: {lista_resultado}")