"""Lucas Aguiar. Programación 1. 14/10/2024. Supón que estás desarrollando un juego de video con distintos tipos de personajes y 
armas. Los requerimientos cambian con frecuencia, añadiendo nuevos 
personajes y habilidades. Mantener y actualizar TADs en este escenario podría ser una tarea titánica."""

# Listas para personajes y armas
personajes = []  
armas = []      

# Función para agregar un personaje
def agregar_personaje(nombre, vida):
    personajes.append({"nombre": nombre, "vida": vida, "arma": None})
    print(f"Personaje '{nombre}' agregado con vida {vida}.")

# Función para agregar un arma
def agregar_arma(nombre_arma, daño):
    armas.append({"nombre": nombre_arma, "daño": daño})
    print(f"Arma '{nombre_arma}' agregada con daño {daño}.")

# Agregar personajes y armas utilizando las funciones
agregar_personaje("Thor", 100)
agregar_personaje("Loki", 80)

agregar_arma("Martillo", 30)
agregar_arma("Daga", 15)

# Asignar arma a un personaje
def asignar_arma(personaje_nombre, arma_nombre):
    for personaje in personajes:
        if personaje["nombre"] == personaje_nombre:
            for arma in armas:
                if arma["nombre"] == arma_nombre:
                    personaje["arma"] = arma
                    print(f"{personaje_nombre} recibió {arma_nombre}.")
                    return
    print("Personaje o arma no encontrados.")

# Simular un ataque
def atacar(atacante_nombre, objetivo_nombre):
    atacante = next((p for p in personajes if p["nombre"] == atacante_nombre), None)
    objetivo = next((p for p in personajes if p["nombre"] == objetivo_nombre), None)

    if atacante and objetivo and atacante["arma"]:
        objetivo["vida"] -= atacante["arma"]["daño"]
        print(f"{atacante_nombre} atacó a {objetivo_nombre} causando {atacante['arma']['daño']} de daño.")
    else:
        print("No se puede atacar. Verifique los nombres o si el atacante tiene un arma.")

# Asignar el arma
asignar_arma("Thor", "Martillo")

# Realizar un ataque
atacar("Thor", "Loki")  # Thor ataca a Loki

# Mostrar estado de los personajes
for personaje in personajes:
    print(f"{personaje['nombre']} - Vida: {personaje['vida']} - Arma: {personaje['arma']['nombre'] if personaje['arma'] else 'Sin arma'}")







