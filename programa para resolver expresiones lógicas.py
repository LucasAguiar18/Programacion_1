def evaluar_expresion_logica(a, b, c):
    # Definir la expresión lógica
    expresion = ("escriba una expresion por favor")
    return expresion

def main():
    print("Programa para resolver expresiones lógicas de la forma ")
    
    while True:
        # Solicitar valores para las variables a, b y c
        a = input("Introduce el valor de a (True/False): ").strip().lower() == 'true'
        b = input("Introduce el valor de b (True/False): ").strip().lower() == 'true'
        c = input("Introduce el valor de c (True/False): ").strip().lower() == 'true'

        # Evaluar la expresión lógica
        resultado = evaluar_expresion_logica(a, b, c)
        print(f"Resultado de la expresión (a∧b)∨(¬c): {resultado}")
        
        # Preguntar si se desea continuar
        continuar = input("¿Quieres evaluar otra expresión? (si/no): ").strip().lower()
        if continuar != 'si':
            break

if __name__ == "__main__":
    main()
