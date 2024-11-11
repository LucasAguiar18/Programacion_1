"""Lucas Aguiar. Programación 1. 11/11/2024. 
Desafío 2:
Crea una clase Bibliotecario que herede de Usuario y tenga atributos específicos como sección y años_experiencia."""

class Usuario:
    def __init__(self, nombre, apellido, sección, años_experiencia):
        self.nombre = nombre
        self.apellido = apellido
        self.sección = sección
        self.años_experiencia = años_experiencia

class Bibliotecario (Usuario):
    def __init__(self, nombre, apellido, sección, años_experiencia):
        super().__init__(self, nombre, apellido, sección, años_experiencia)
        self.sección = sección
        self.años_experiencia = años_experiencia

# Ejemplo de uso

bibliotecario = Bibliotecario("Lucas", "Aguiar", "Biblioteca", "10")
print(f"Nombre: {bibliotecario.nombre}")
print(f"Apellido: {bibliotecario.apellido}")
print(f"Sección: {bibliotecario.sección}")
print(f"Años de experiencia: {bibliotecario.años_experiencia}")