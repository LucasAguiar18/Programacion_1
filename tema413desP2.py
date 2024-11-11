"""Lucas Aguiar. Programacion 1. 11/11/2024. 
Desafío 2: 
Añade un método biografia a la clase Autor y sobrescríbelo en la clase Escritor. 
Instancia un objeto de la clase Escritor y muestra cómo se puede acceder al método biografia de ambas clases."""

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def biografia(self):
        return f"Soy {self.nombre} {self.apellido} y soy escritor."
    
class Escritor(Autor):
    def __init__(self, nombre, apellido, genero):
        super().__init__(nombre, apellido)
        self.genero = genero

    def biografia(self):
        return f"Soy {self.nombre} {self.apellido} y me gusta escribir sobre {self.genero}."
    
# Ejemplo de uso

escritor = Escritor("Lucas", "Aguiar", "Fantasía")
print(escritor.biografia())

escritor2 = Escritor("Luana", "Román", "suspenso")

print(escritor2.biografia())