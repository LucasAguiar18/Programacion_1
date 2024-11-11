"""Lucas Aguiar. Programación 1. 11/11/2024
Desafío 4:
Implementa una clase EscritorAcademico que herede de Escritor y Academico, e incluya un método adicional para publicar artículos académicos.
 Asegúrate de utilizar correctamente la función super() para inicializar las clases base."""

class Escritor:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def mostrar_datos_escritor(self):
        print (f"El nombre del escritor es: {self.nombre}")
        print (f"El género que escribe es: {self.genero}")

class Academico:
    def __init__(self, especialidad):
        self.especialidad = especialidad

    def mostrar_datos_academico(self):
        print (f"La especialidad del escritor es: {self.especialidad}")


class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, especialidad):
        super().__init__(nombre, genero)
        Academico.__init__(self, especialidad)


    def publicar_articulo_academico(self):
        print (f"{self.nombre} ha publicado un artículo en la especialidad de {self.especialidad}")

# Ejemplo de uso

escritor_academico = EscritorAcademico("Lucas Aguiar", "masculino", "informática")
escritor_academico.mostrar_datos_escritor()
escritor_academico.mostrar_datos_academico()
escritor_academico.publicar_articulo_academico()