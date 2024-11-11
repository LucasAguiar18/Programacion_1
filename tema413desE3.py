"""Lucas Aguiar. Programación 1. 10/11/2024
Desafío 3:
Implementa la clase Autor con métodos getter y setter utilizando decoradores 
@property para manejar los atributos privados nombre y nacionalidad."""


class Autor:
    
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre  
        self.__nacionalidad = nacionalidad  

    # Método getter para obtener el nombre del autor
    @property
    def nombre(self):
        return self.__nombre

    # Método setter para establecer el nombre del autor
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # Método getter para obtener la nacionalidad del autor
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Método setter para establecer la nacionalidad del autor
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

# Ejemplo de uso
autor = Autor("Lucas Aguiar", "Uruguayo")
print("Autor:", autor.nombre)
print("Nacionalidad:", autor.nacionalidad)
