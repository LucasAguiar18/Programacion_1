"""Lucas Aguiar. Programación 1. 10/11/2024.
Desafío 4:
Crea una función que tome un objeto Autor y devuelva una lista de todos los títulos de libros escritos por el autor. 
Asegúrate de que la lista de libros sea accesible solo a través de métodos de la clase Autor."""


class Autor:
   
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # Lista para almacenar títulos de libros

    # Método getter para obtener el nombre del autor
    @property
    def nombre(self):
        return self.__nombre

    # Método setter para establecer el nombre del autor
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # Método getter para obtener la nacionalidad del autor
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Método setter para establecer la nacionalidad del autor
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Método para agregar un título de libro a la lista de libros del autor
    def agregar_libro(self, titulo):
        self.__libros.append(titulo)  # Agrega el título a la lista

    # Método para obtener la lista de títulos de libros del autor
    def get_titulos_libros(self):
        return self.__libros

# Ejemplo de uso
autor = Autor("Lucas Aguiar", "Uruguayo")
autor.agregar_libro("El Viaje Infinito")
autor.agregar_libro("Memorias del Pasado")

# Imprime la lista de títulos de libros del autor
print("Libros escritos por", autor.nombre)
print(autor.get_titulos_libros())
