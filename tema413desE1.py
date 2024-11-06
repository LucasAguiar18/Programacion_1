"""Lucas Aguiar. Programación 1. Encapsulamiento: 
Desafío 1: 
Crea una clase Libro que tenga atributos privados para el título, autor y ISBN. 
Proporciona métodos getter y setter para cada atributo."""

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # Metodo getter
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_isbn(self):
        return self.__isbn
    
    # Metodo setter
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_isbn(self, isbn):
        self.__isbn = isbn

# Ejemplo de uso

libro = Libro("El Quijote de la Mancha", "Miguel de Cervantes", "978-84-666-0771-1")
print(f"Título: {libro.get_titulo()}")
print(f"Autor: {libro.get_autor()}")
print(f"ISBN: {libro.get_isbn()}")

libro.set_titulo("El Quijote de la Mancha ")

libro2 = Libro ("Mi historia", "Lucas Aguiar", "978-84-666-0771-")

print(f"\nTítulo: {libro2.get_titulo()}")
print(f"Autor: {libro2.get_autor()}")
print(f"ISBN: {libro2.get_isbn()}")
