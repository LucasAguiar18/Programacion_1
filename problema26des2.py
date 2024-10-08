# Inicializamos los contadores para la suma de calificaciones y el número de asignaturas
suma_calificaciones = 0
contador_asignaturas = 0

# Pedimos al usuario que ingrese todas las calificaciones separadas por comas
calificaciones_input = input("Ingrese las calificaciones (entre 1 y 12) separadas por comas: ")

# Dividimos la cadena de entrada en una lista de calificaciones
calificaciones = calificaciones_input.split(',')

# Procesamos cada calificación
for calificacion_str in calificaciones:
    try:
        calificacion = int(calificacion_str.strip())
        
        if calificacion < 1 or calificacion > 12:
            print(f"La calificación {calificacion} no es válida. Debe estar entre 1 y 12.")
            continue

        suma_calificaciones += calificacion
        contador_asignaturas += 1
    except ValueError:
        print(f"{calificacion_str} no es un número válido. Inténtalo de nuevo.")
        continue

# Calculamos y mostramos el promedio solo si se ingresaron calificaciones válidas
if contador_asignaturas > 0:
    promedio = suma_calificaciones / contador_asignaturas
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")
