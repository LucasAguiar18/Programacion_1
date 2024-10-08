"""
Lucas Aguiar, Programacion 1.
Desafío 1: Calificaciones Aprobatorias y Desaprobatorias
Supón que estás analizando las calificaciones de los estudiantes y quieres saber cuántos
aprobaron y cuántos desaprobaron. Se considera que una calificación de 7 
o superior es aprobatoria y cualquier calificación menor a 7 es desaprobatoria.
Utiliza lo que aprendiste sobre bucles y condicionales para resolver este problema.
"""
#primero pedimos calificaciones
while True:
  calificacion = float (input("ingrese una calificacion por favor (entre 1 y 12) o 0 para terminar: "))
  if calificacion == 0:
   break
  #a medida que damos calificaciones que ya nos diga si aprueba o no aprueba 
  if calificacion  >= 7: 
    print("aprobado",calificacion)
  if calificacion < 7:
    print("no aprobado",calificacion)
