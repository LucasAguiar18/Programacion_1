"""Lucas Aguiar. Programacion 1. 5/11/2024. 
Desafío 4:Piensa en otros atributos y métodos que podrías 
agregar a la clase `Autor` para hacerla más completa."""

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, premio):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.libros = []
        self.premio = premio

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Biblioteca:
    def __init__(self):
        self.autores = {}
        self.libros = {}

    def agregar_autor(self, nombre, nacionalidad, fecha_nacimiento, premio):
        autor = Autor(nombre, nacionalidad, fecha_nacimiento, premio)
        self.autores[nombre] = autor
        print("Autor agregado correctamente")
        return autor

    def agregar_libro(self, titulo, autor_nombre):
        if autor_nombre in self.autores:
            autor = self.autores[autor_nombre]
            libro = Libro(titulo, autor)
            autor.libros.append(libro)
            self.libros[titulo] = libro
            print("Libro agregado correctamente")
            return libro
        else:
            print("No se encontró el autor")

    def mostrar_libros(self):
        print("\nLibros:")
        for libro in self.libros.values():
            print(f"- {libro.titulo} de {libro.autor.nombre}")

    def mostrar_autores(self):
        print("\nAutores:")
        for autor in self.autores.values():
            print(f"- {autor.nombre} ({autor.nacionalidad}) - Fecha de nacimiento: {autor.fecha_nacimiento} - Premio: {autor.premio}")
            


# CREAR BIBLIOTECA
biblioteca = Biblioteca()

# PRUEBAS DE USO
autor = biblioteca.agregar_autor("Lucas Aguiar", "Uruguayo", "12/12/1990","Premio Literatura")
autor2 = biblioteca.agregar_autor("EL EPEP", "Colombiano", "01/01/1980","Premio a mejor libro")

biblioteca.agregar_libro("El amor en la oscuridad", "Lucas Aguiar")
biblioteca.agregar_libro("el pepito", "EL EPEP")

biblioteca.mostrar_libros()
biblioteca.mostrar_autores()