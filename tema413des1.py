"""
 Lucas Aguiar. Programación 1.  15/10/2024. Crea una clase Libro que tenga atributos privados
 para el título, autor y ISBN. Proporciona métodos
 getter y setter para cada atributo.
"""

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo   # Atributo privado
        self.__autor = autor     
        self.__isbn = isbn       

    # Getter para el título
    def get_titulo(self):
        return self.__titulo

    # Setter para el título
    def set_titulo(self, titulo):
        self.__titulo = titulo

    # Getter para el autor
    def get_autor(self):
        return self.__autor

    # Setter para el autor
    def set_autor(self, autor):
        self.__autor = autor

    # Getter para el ISBN
    def get_isbn(self):
        return self.__isbn

    # Setter para el ISBN
    def set_isbn(self, isbn):
        self.__isbn = isbn

# Ejemplo de uso
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0")
print("Título:", libro1.get_titulo())
print("Autor:", libro1.get_autor())
print("ISBN:", libro1.get_isbn())

# Cambiar el título
libro1.set_titulo("El amor en los tiempos del cólera")
print("Nuevo título:", libro1.get_titulo())
