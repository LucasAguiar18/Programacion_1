class Autor:
    def __init__(self, nombre= "", nacionalidad= ""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

#Mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")

#Agregar un libro al autor
    def agregar_libro(self, libro):
        self.libros.append(libro)

    #Eliminar libros
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"\nLibro '{libro}' eliminado correctamente.")
        else:
            print(f"\nEl libro '{libro}' no se encuentra en la lista de libros del autor.")

    #Mostrar el autor 
    def mostrar_autor (self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        if self.libros:
            print("Libros publicados:")
            for libro in self.libros:
                print(f"{libro}")
            else:
                print("Este autor no ha publicado libros.")

autor1 = Autor("Lucas Aguiar", "Uruguayo")
autor1.agregar_libro("Harry")
autor1.agregar_libro("Mi historia")
autor1.mostrar_autor()

print(autor1.nombre)
print(autor1.nacionalidad)
print(autor1.libros)

autor1.eliminar_libro("Mi historia")
print ("\nDespues de eliminar\n")

print(autor1.nombre)
print(autor1.nacionalidad)
print(autor1.libros)
