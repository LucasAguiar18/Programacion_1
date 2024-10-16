"""Lucas Aguiar. Programacion1. 15/10/2024. Desafio 2:Crea una clase `Libro` con atributos como 
título, género e ISBN. ¿Cómo podrías relacionar esta clase con la clase `Autor`?"""

class Autor:

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    def agregar_libros(self,libro):
        self.libros.append(libro)
        
    def mostrar_libros(self):
        print(f"\nLibros de {self.nombre}:")
        for libro in self.libros:
         print(f"- {libro.titulo}")

class Libro:
    def __init__(self, titulo, genero, isbn, autor):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor

    def mostrar_datos(self):
        print(f"Datos del libro:")
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
        print(f"Autor: {self.autor.nombre}")

#Agregar Libros y Autores

autor1 = Autor("Lucas", "Uruguayo")
autor2 = Autor ("Luana", "Uruguaya")

libro1 = Libro("El alma de la noche", "Novela", "978-84-316-1484-4", autor1)

libro2 = Libro("Mi historia", "Novela", "978-84-316-1485-1", autor2)

autor1.agregar_libros(libro1)

autor2.agregar_libros(libro2)

#Mostrar datos

libro1.mostrar_datos()
libro2.mostrar_datos()

autor1.mostrar_libros()
autor2.mostrar_libros()

