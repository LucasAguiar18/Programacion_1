"""Lucas Aguiar. Programación 1. 11/11/2024
Desafío 5: Polimorfismo en operaciones matemáticas
En este desafío, aplicarás el polimorfismo para realizar diferentes operaciones matemáticas. 
Deberás crear una clase base Operacion con un método resultado y dos subclases Suma y Multiplicacion que sobrescriban este método para realizar las operaciones correspondientes."""

class Operacion:
    def resultado(self):
        pass

class Suma(Operacion):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def resultado(self):
        return self.num1 + self.num2
    
    def muestra_info(self):
        return f"La suma de {self.num1} y {self.num2} es: {self.resultado()}"
    
class Multiplicacion(Operacion):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def resultado(self):
        return self.num1 * self.num2
    
    def muestra_info(self):
        return f"La multiplicación de {self.num1} y {self.num2} es: {self.resultado()}"
    
    # Ejemplo de uso
suma = Suma(5, 10)

print(suma.muestra_info())

multiplicacion = Multiplicacion(3, 7)

print(multiplicacion.muestra_info())