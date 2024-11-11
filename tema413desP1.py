"""Lucas Aguiar. Programación 1. 11/11/2024
Desafío 1: 
Crea una clase Musico que tenga un método instrumento y crea dos subclases Guitarrista y Baterista que sobrescriban el método instrumento. 
Instancia objetos de estas clases y demuestra el polimorfismo."""

# Clase base Musico

class Musico:
    def __init__(self, nombre,):
        self.nombre = nombre

        def instrumento(self):
            return "guitarra"

# Subclase Guitarrista

class Guitarrista(Musico):
    def instrumento(self):
       return "guitarra electrica"

# Subclase Baterista

class Baterista(Musico):
    def instrumento(self):
        return "bateria"



guitarrista = Guitarrista("Lucas")
baterista = Baterista("Luana")

print(f"{guitarrista.nombre} toca {guitarrista.instrumento()}")
print(f"{baterista.nombre} toca {baterista.instrumento()}")