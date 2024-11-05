"""Lucas Aguiar. Programacion 1. 4/11/2024. 
Desafío 3:Considera cómo podrías implementar una biblioteca que 
almacene múltiples autores y libros. ¿Qué estructuras de datos usarías?"""

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.autores = {}
        self.libros = {}

    def agregar_autor(self, nombre, nacionalidad):
        autor = Autor(nombre, nacionalidad)
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
            print(f"- {autor.nombre} ({autor.nacionalidad})")
            
# CREAR BIBLIOTECA
biblioteca = Biblioteca()

# PRUEBAS DE USO
autor = biblioteca.agregar_autor("Lucas Aguiar", "Uruguayo")
biblioteca.agregar_libro("El amor en la oscuridad", "Lucas Aguiar")

autor = biblioteca.agregar_autor("EL EPEP", "Colombiano")
biblioteca.agregar_libro("el pepito", "EL EPEP")

biblioteca.mostrar_libros()
biblioteca.mostrar_autores()
