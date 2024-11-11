"""Lucas Aguiar. Programación 1. 11/11/2024. 
Desafío 1: 
Implementa una clase Poeta que herede de Autor y tenga un atributo para el tipo de poesía que escribe."""

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

class Poeta (Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        super().__init__(nombre, nacionalidad)
        self.tipo_poesia = tipo_poesia

# Ejemplo de uso

poeta = Poeta("Lucas Aguiar", "Uruguayo", "Poesia Lirica")
print(f"Nombre: {poeta.nombre}")
print(f"Nacionalidad: {poeta.nacionalidad}")
print(f"Tipo de poesía: {poeta.tipo_poesia}")
