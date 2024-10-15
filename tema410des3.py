# Listas para almacenar tiendas, productos y empleados
tiendas = []
productos = []
empleados = []
transacciones = []

# Función auxiliar para buscar un elemento en una lista (tienda, producto, empleado)
def buscar_elemento(lista, nombre):
    return next((elemento for elemento in lista if elemento["nombre"] == nombre), None)

# Función para crear una tienda
def crear_tienda(nombre):
    tiendas.append({"nombre": nombre, "productos": [], "empleados": []})

# Función para crear un producto
def crear_producto(nombre, precio):
    productos.append({"nombre": nombre, "precio": precio, "cantidad": 0})

# Función para crear un empleado
def crear_empleado(nombre, puesto):
    empleados.append({"nombre": nombre, "puesto": puesto})

# Función para agregar un producto a una tienda
def agregar_producto_a_tienda(tienda_nombre, producto_nombre, cantidad):
    tienda = buscar_elemento(tiendas, tienda_nombre)
    producto = buscar_elemento(productos, producto_nombre)
    
    if tienda and producto:
        producto["cantidad"] = cantidad  
        tienda["productos"].append(producto)
    else:
        print("Error: Tienda o producto no encontrados.")

# Función para agregar un empleado a una tienda
def agregar_empleado_a_tienda(tienda_nombre, empleado_nombre):
    tienda = buscar_elemento(tiendas, tienda_nombre)
    empleado = buscar_elemento(empleados, empleado_nombre)
    
    if tienda and empleado:
        tienda["empleados"].append(empleado)
    else:
        print("Error: Tienda o empleado no encontrados.")

# Función para registrar una transacción
def registrar_transaccion(tienda_nombre, producto_nombre, cantidad):
    tienda = buscar_elemento(tiendas, tienda_nombre)
    if tienda:
        producto = buscar_elemento(tienda["productos"], producto_nombre)
        if producto and producto["cantidad"] >= cantidad:
            producto["cantidad"] -= cantidad
            transacciones.append({
                "tienda": tienda_nombre,
                "producto": producto_nombre,
                "cantidad": cantidad
            })
            print(f"Transacción exitosa: {cantidad} {producto_nombre} vendidos en {tienda_nombre}.")
        else:
            print("Error: Producto no encontrado o cantidad insuficiente.")
    else:
        print("Error: Tienda no encontrada.")

# Función para mostrar el estado de las tiendas
def mostrar_tiendas():
    for tienda in tiendas:
        print(f"Tienda: {tienda['nombre']}")
        print("Productos:")
        for producto in tienda["productos"]:
            print(f"  - {producto['nombre']} - Cantidad: {producto['cantidad']}")
        print("Empleados:")
        for empleado in tienda["empleados"]:
            print(f"  - {empleado['nombre']} - Puesto: {empleado['puesto']}")
        print()

# Ejemplo de uso:
crear_tienda("Tienda A")
crear_producto("Laptop", 1000)
crear_producto("Celular", 500)
crear_empleado("Juan", "Cajero")
crear_empleado("Ana", "Gerente")

agregar_producto_a_tienda("Tienda A", "Laptop", 10)
agregar_empleado_a_tienda("Tienda A", "Juan")
agregar_empleado_a_tienda("Tienda A", "Ana")

registrar_transaccion("Tienda A", "Laptop", 2)

crear_tienda("Tienda B")
crear_producto("Mouse",500)
crear_producto("Teclado", 250)
crear_empleado("Lucas", "Gerente")
crear_empleado("Pablo", "Cajero")

agregar_producto_a_tienda("Tienda B", "Mouse", 1500)
agregar_empleado_a_tienda("Tienda B", "Pablo")
agregar_empleado_a_tienda("Tienda B", "Lucas")

# Mostrar estado de la tienda
mostrar_tiendas()
