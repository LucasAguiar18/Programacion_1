"""Lucas Aguiar. Programación 1. 11/11/2024. 
Desafío 4: Polimorfismo en figuras geométricas
En este desafío, se te pide que implementes el polimorfismo con métodos de clase en figuras geométricas. 
Deberás crear una clase base Figura con un método area y dos subclases Circulo y Cuadrado que sobrescriban este método para calcular el área de cada figura."""

import math

# Clase base Figura
class Figura:
    def area(self):
        pass

# Subclase Circulo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2
    
    def muestra_info(self):
        return f"El área del círculo es: {self.area()}"

# Subclase Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    def muestra_info(self):
        return f"El área del cuadrado es: {self.area()}"

# Ejemplo de uso
circulo = Circulo(15)
cuadrado = Cuadrado(13)

print(circulo.muestra_info())
print(cuadrado.muestra_info())
