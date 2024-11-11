"""Lucas Aguiar. Programación 1. 10/11/2024. 
Desafío 5:
Desarrolla una función que reciba una lista de objetos Autor y devuelva el autor que ha escrito el mayor número de libros.
 Utiliza el encapsulamiento para acceder a la información necesaria de cada objeto Autor."""

# Clase Autor: Representa un autor con nombre, nacionalidad y lista de títulos de libros
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # Lista para almacenar títulos de libros

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def agregar_libro(self, titulo):
        self.__libros.append(titulo)  # Agrega el título a la lista

    def get_titulos_libros(self):
        return self.__libros

# Función para encontrar el autor con el mayor número de libros
def autor_con_mas_libros(lista_autores):
    if not lista_autores:  # Verifica si la lista está vacía
        return None
    
    # Inicializa el autor con más libros como el primero en la lista
    autor_mayor = lista_autores[0]
    
    # Recorre la lista para encontrar el autor con más libros
    for autor in lista_autores:
        if len(autor.get_titulos_libros()) > len(autor_mayor.get_titulos_libros()):
            autor_mayor = autor
    
    return autor_mayor

# Ejemplo de uso
autor1 = Autor("Lucas Aguiar", "Uruguayo")
autor1.agregar_libro("El Viaje Infinito")
autor1.agregar_libro("Memorias del Pasado")

autor2 = Autor("PEPE", "Argentino")
autor2.agregar_libro("Caminos Cruzados")

autor3 = Autor("Luis Pérez", "Chileno")
autor3.agregar_libro("Sombras y Luces")
autor3.agregar_libro("Reflejos del Alma")
autor3.agregar_libro("El Último Sol")

lista_autores = [autor1, autor2, autor3]

# Encuentra el autor con más libros y muestra su nombre y la cantidad de libros
autor_mayor = autor_con_mas_libros(lista_autores)
if autor_mayor:
    print(f"El autor con más libros es {autor_mayor.nombre} con {len(autor_mayor.get_titulos_libros())} libros.")
else:
    print("La lista de autores está vacía.")
