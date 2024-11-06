"""
 Lucas Aguiar. Programación 1.  15/10/2024. Crea una clase Libro que tenga atributos privados
 para el título, autor y ISBN. Proporciona métodos
 getter y setter para cada atributo.
"""

# Clase base Autor
class Autor:
    def __init__(self, nombre, anio_nacimiento):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento

    def mostrar_info(self):
        return f"Autor: {self.nombre}, nacido en {self.anio_nacimiento}"

# Clase derivada Poeta
class Poeta(Autor):
    def __init__(self, nombre, anio_nacimiento, tipo_poema):
        super().__init__(nombre, anio_nacimiento)
        self.tipo_poema = tipo_poema

    def mostrar_info_poeta(self):
        return f"Poeta: {self.nombre}, nacido en {self.anio_nacimiento}, escribe poesía {self.tipo_poema}"

# Ejemplo de uso
poeta = Poeta("Pablo Neruda", 1904, "lírica")
print(poeta.mostrar_info())          

