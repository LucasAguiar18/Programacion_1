"""Lucas Aguiar. Programación 1. Encapsulamiento: 
Desafío 2:
Modifica la clase Autor para que pueda tener una lista de libros escritos por el autor. 
Proporciona un método para agregar libros a esta lista."""

class Autor:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []

    # Método para agregar libros
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    # Método para obtener la lista de libros
    def obtener_libros(self):
        return self.__libros

    # Método getter para el nombre
    def get_nombre(self):
        return self.__nombre

# Ejemplo de uso
autor = Autor("Miguel de Cervantes")
autor.agregar_libro("El Quijote de la Mancha")
autor.agregar_libro("La Galatea")

autor2 = Autor("Lucas Aguiar")
autor2.agregar_libro("Mi historia")
autor2.agregar_libro("La bicicleta")

print(f"Autor: {autor.get_nombre()}")
print("Libros escritos:")
for libro in autor.obtener_libros():
    print(f"- {libro}")

print(f"Autor:{autor2.get_nombre()}")
print("Libros escritos:")
for libro2 in autor2.obtener_libros():
    print(f"- {libro2}")
