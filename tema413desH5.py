"""Lucas Aguiar. Programación 1. 11/11/2024. 
Desafío 5:
Crea una jerarquía de clases para representar diferentes tipos de empleados en una biblioteca, utilizando herencia múltiple y composición.
 Por ejemplo, implementa clases como Empleado, Gerente, Tecnico, y Voluntario, 
 donde Gerente y Tecnico hereden de Empleado, y algunos puedan tener roles adicionales mediante composición con otras clases como Administrador o Mantenimiento."""

# Clase base para todos los empleados
class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo

    def mostrar_ocupacion(self):
        print(f"{self.nombre} trabaja como {self.cargo}")

# Clase que representa un Gerente, hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, cargo, area_de_trabajo):
        super().__init__(nombre, cargo)
        self.area = area_de_trabajo

    def mostrar_datos(self):
        self.mostrar_ocupacion()
        print(f"Área de trabajo: {self.area}")

# Clase que representa un Técnico, hereda de Empleado
class Tecnico(Empleado):
    def __init__(self, nombre, cargo, especialidad):
        super().__init__(nombre, cargo)
        self.especialidad = especialidad

    def mostrar_datos(self):
        self.mostrar_ocupacion()
        print(f"Especialidad: {self.especialidad}")

# Clase que representa un Voluntario, hereda de Empleado
class Voluntario(Empleado):
    def __init__(self, nombre, cargo, organizacion):
        super().__init__(nombre, cargo)
        self.organizacion = organizacion

    def mostrar_datos(self):
        self.mostrar_ocupacion()
        print(f"Organización: {self.organizacion}")

# Clase adicional Administrador para usar mediante composición
class Administrador:
    def __init__(self, area_admin):
        self.area_admin = area_admin

    def mostrar_info_admin(self):
        print(f"Área de administración: {self.area_admin}")

# Clase adicional Mantenimiento para usar mediante composición
class Mantenimiento:
    def __init__(self, area_mantenimiento):
        self.area_mantenimiento = area_mantenimiento

    def mostrar_info_mantenimiento(self):
        print(f"Área de mantenimiento: {self.area_mantenimiento}")

# Ejemplos de uso
# Instanciando un gerente
gerente = Gerente("Luana Román", "Gerenta", "Biblioteca")
gerente.mostrar_datos()

# Instanciando un técnico
tecnico = Tecnico("Lucas Aguiar", "Técnico", "Sistemas informáticos")
tecnico.mostrar_datos()

# Instanciando un voluntario
voluntario = Voluntario("Pepito", "Voluntario", "Amigos de la Biblioteca")
voluntario.mostrar_datos()

# Instanciando un administrador adicional usando composición
admin = Administrador("Recursos Humanos")
admin.mostrar_info_admin()

# Instanciando un técnico de mantenimiento usando composición
mantenimiento = Mantenimiento("Equipos Eléctricos")
mantenimiento.mostrar_info_mantenimiento()
