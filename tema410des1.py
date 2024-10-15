"""Lucas Aguiar. Programación 1. 10/10/2024. ### Desafío 1: Sistemas con Múltiples Entidades Interconectadas
Imagina un sistema de gestión de biblioteca que maneja libros, usuarios, préstamos y multas. Usar TADs separados para cada uno de estos elementos podría 
complicar la interacción y gestión de relaciones entre ellos."""

# Creamos las lista vacias para libros, usuarios, préstamos y multas
libros = []    
usuarios = []   
prestamos = [] 
multas = []     

# Función para agregar un libro a la biblioteca
def agregar_libro(titulo, autor, codigo):
    libro = {"titulo": titulo, "autor": autor, "codigo": codigo, "disponible": True}
    libros.append(libro)
    print(f"Libro agregado: {libro['titulo']} - {libro['autor']}.")

# Función para registrar un usuario en el sistema
def registrar_usuario(nombre, id_usuario):
    usuario = {"nombre": nombre, "id_usuario": id_usuario}
    usuarios.append(usuario)

# Función para buscar un libro por su código
def buscar_libro(codigo):
    for libro in libros:
        if libro["codigo"] == codigo:
            return libro
    return None #en caso de que el libro no exista 

# Función para buscar un usuario por su ID
def buscar_usuario(id_usuario):
    for usuario in usuarios:
        if usuario["id_usuario"] == id_usuario:
            return usuario
    return None  

# Función para prestar un libro a un usuario
def prestar_libro(codigo_libro, id_usuario, dias=7):
    libro = buscar_libro(codigo_libro)
    usuario = buscar_usuario(id_usuario)

    if libro and usuario and libro["disponible"]:
        prestamo = {
            "codigo_libro": codigo_libro,
            "id_usuario": id_usuario,
            "dias_restantes": dias  # Guardamos cuántos días tiene para devolver
        }
        prestamos.append(prestamo)
        libro["disponible"] = False  # Marcamos el libro como prestado
        print(f"Préstamo realizado: {libro['titulo']} a {usuario['nombre']}.")
    else:
        print("No se pudo realizar el préstamo.")

# Función para devolver un libro y aplicar multa si corresponde
def devolver_libro(codigo_libro, dias_pasados):
    for prestamo in prestamos:
        if prestamo["codigo_libro"] == codigo_libro:
            libro = buscar_libro(codigo_libro)
            usuario = buscar_usuario(prestamo["id_usuario"])

            if dias_pasados > prestamo["dias_restantes"]:
                dias_retraso = dias_pasados - prestamo["dias_restantes"]
                multa = dias_retraso * 2  
                registrar_multa(usuario["id_usuario"], multa)
                print(f"Multa aplicada: ${multa} por retraso.")

            libro["disponible"] = True  
            prestamos.remove(prestamo)  
            print(f"Devolución registrada: {libro['titulo']} por {usuario['nombre']}.")
            return

    print("No se encontró el préstamo para ese libro.")

# Función para registrar una multa
def registrar_multa(id_usuario, monto):
    multa = {"id_usuario": id_usuario, "monto": monto}
    multas.append(multa)

# Función para mostrar todas las multas registradas
def mostrar_multas():
    for multa in multas:
        usuario = buscar_usuario(multa["id_usuario"])
        if usuario:
            print(f"Usuario: {usuario['nombre']}, Multa: ${multa['monto']}")

# Pruebas del sistema
agregar_libro("1984", "George Orwell", "001")
agregar_libro("Cien años de soledad", "Gabriel García Márquez", "002")

registrar_usuario("Lucas", "U001")
registrar_usuario("Carlos", "U002")

prestar_libro("001", "U001", dias=7)  # Préstamo por 7 días
devolver_libro("001", dias_pasados=10)  # Se devuelve tras 10 días (3 días tarde)
mostrar_multas()
