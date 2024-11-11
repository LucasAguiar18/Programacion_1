"""Lucas Aguiar. Programación 1. 11/11/2024. 
Desafío 3: 
En este desafío, vamos a extender la clase Libro para crear una subclase `LibroEspecializado`. 
Un `LibroEspecializado`, además de tener un título y un autor, también tiene un campo de estudio y un nivel de especialización (básico, intermedio, avanzado)."""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def muestra_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor,nivel_especializacion):
        super().__init__(titulo, autor)
        self.especializacion = nivel_especializacion

    def muestra_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Especialización: {self.especializacion}"
    
#ejemplo de uso 
libro_especializado = LibroEspecializado("Mi historia", "Lucas Aguiar", "Intermedio")
print(libro_especializado.muestra_info()) 
