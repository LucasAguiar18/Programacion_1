"""
Lucas Aguiar, Programación 1.
Toma el ejemplo del cálculo del promedio de calificaciones y mejóralo.
 En lugar de pedir las calificaciones una por una, modifica el código para pedir todas las calificaciones al mismo tiempo 
 (el estudiante puede ingresar las calificaciones separadas por comas)
 y luego calcular el promedio.
"""
# Pedimos al usuario que ingrese las calificaciones separadas por coma
calificaciones = input("Ingrese todas las calificaciones (entre 1 y 12) separadas por coma, o 0 para terminar: ")

# Convertir las calificaciones en una lista de enteros 
calificaciones = [int(calificacion) for calificacion in calificaciones.split(',')]
                  
#calculamos el promedio 
promedio = sum(calificaciones) / len(calificaciones)
print(f"El promedio de las calificaciones es: {promedio}")

