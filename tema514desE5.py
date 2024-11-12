"""Lucas Aguiar. Programación 1. 12/11/2024
Desafío 5: 
Desarrolla un programa que abra un archivo de texto, lea su contenido y lo muestre. 
Implementa manejo de excepciones para archivos que no existan y usa finally para asegurarte de que el archivo se cierre adecuadamente en cualquier caso. """

try:
    # Solicitamos el nombre de la ruta del  archivo al usuario
    ruta_archivo = input("Ingrese el nombre de la ruta del archivo: ")
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, "r") as archivo:
        # Leemos el contenido del archivo
        contenido = archivo.read()
        
        # Mostramos el contenido
        print(f"Contenido del archivo: {contenido}")

except FileNotFoundError:
    print("Error: El archivo no existe")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo")

finally:
    # Cerramos el archivo
    print("Archivo cerrado")