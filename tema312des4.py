"""Lucas Aguiar. Programacion1. 15/10/2024. Desafio 4:Piensa en otros atributos y 
métodos que podrías agregar a la clase `Autor` para hacerla más completa."""

class Autor:

    def __init__(self, nombre, nacionalidad, edad, premios, profesiones):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.edad = edad
        self.premios = premios  
        self.profesiones = profesiones  
        self.libros = []

    def agregar_libros(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"\nLibros de {self.nombre}:")
        for libro in self.libros:
            print(f"- {libro.titulo}")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Edad: {self.edad}")
        print(f"Premios: {(self.premios)}")
        print(f"Profesiones: {(self.profesiones)}")


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


# Agregar Autores con los nuevos atributos

autor1 = Autor("Lucas", "Uruguayo", 19, ["Premio Nacional"], ["Escritor", "Profesor"])
autor2 = Autor("Luana", "Uruguaya", 18, ["Premio Internacional"], ["Escritora", "Profesora"])

libro1 = Libro("El alma de la noche", "Novela", "978-84-316-1484-4", autor1)
libro2 = Libro("Mi historia", "Novela", "978-84-316-1485-1", autor2)

autor1.agregar_libros(libro1)
autor2.agregar_libros(libro2)

# Mostrar datos

libro1.mostrar_datos()
libro2.mostrar_datos()

autor1.mostrar_libros()
autor2.mostrar_libros()

autor1.mostrar_informacion()
autor2.mostrar_informacion()
