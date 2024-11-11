"""Lucas Aguiar. Programación 1. 11/11/2024
Desafío 3:
Diseña una clase LibroDigital que herede de Libro y añada atributos como formato (e.g., PDF, EPUB)
 y tamaño_archivo. Además, implementa una subclase EBook que sobrescriba un método para mostrar información específica, como enlaces de descarga."""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_datos(self):
        print(f"\nTítulo: {self.titulo}")
        print(f"Autor: {self.autor}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato, tamaño_archivo):
        super().__init__(titulo, autor)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Formato: {self.formato}")
        print(f"Tamaño del archivo: {self.tamaño_archivo} MB")

class EBook(LibroDigital):
    def __init__(self, titulo, autor, formato, tamaño_archivo, enlaces_descarga):
        super().__init__(titulo, autor, formato, tamaño_archivo)
        self.enlaces_descarga = enlaces_descarga

    def mostrar_datos_especificos(self):
        super().mostrar_datos()
        print(f"Enlaces de descarga:")
        for enlace in self.enlaces_descarga:
            print(f"- {enlace}")

# Ejemplo de uso

libro = Libro ("Mi historia", "Lucas Aguiar")
libro.mostrar_datos()

libro_digital = LibroDigital("Harry", "Luana Román", "PDF", 12.5)
libro_digital.mostrar_datos()

ebook = EBook("La bicicleta", "Lucas Román", "PDF", 8, ["https://www.mypaginaofficial.com",])
ebook.mostrar_datos()
