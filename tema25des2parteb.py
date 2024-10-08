#Pedir dos numeros al usuario 
num1= float(input ("Ingrese el primer numero"))
num2= float(input ("Ingrese el segundo numero"))

#Pedirle al usuario que tipo de operacion quiere hacer 

operacion= input("operación que desea realizar(suma, resta, multiplicacion, division)")
resultado=0

#Depende de la operacion que se elige, la cuenta que se realizara 

if operacion == "suma":
    resultado= num1 + num2
    print("el resultado es", resultado)

elif operacion=="resta":
    resultado= num1 - num2
    print("el resultado es", resultado)

elif operacion=="multiplicacion":
    resultado= num1 * num2
    print("el resultado es", resultado)

elif operacion=="division":
    resultado= num1 / num2
    print("el resultado es", resultado )
