import random

# Definir el número de autos
num_autos = 5

# Generar velocidades aleatorias para cada auto (por ejemplo entre 1 y 20 unidades por segundo)
velocidades = [random.randint(1, 20) for _ in range(num_autos)]

# Inicializar las distancias recorridas por cada auto
distancias = [0] * num_autos

# Simular la carrera por 10 segundos
for segundo in range(10):
    for i in range(num_autos):
        distancias[i] += velocidades[i]

# Encontrar la distancia máxima recorrida
distancia_maxima = max(distancias)

# Encontrar todos los autos que han recorrido la distancia máxima
ganadores = [i for i, distancia in enumerate(distancias) if distancia == distancia_maxima]

# Imprimir los resultados
for i in range(num_autos):
    print(f"Auto {i+1}: Velocidad = {velocidades[i]}, Distancia recorrida = {distancias[i]}")

# Imprimir el ganador o los ganadores
if len(ganadores) == 1:
    print(f"\nEl auto ganador es el Auto {ganadores[0]+1}")
else:
    print("\nHay un empate entre los autos:", ', '.join(f"Auto {ganador+1}" for ganador in ganadores))
