#se definen las variables para cambiar el texto 
def negrita(texto):
    return "\033[1m" + texto + "\033[0m"

def italica(texto):
    return "\033[3m" + texto + "\033[0m"
def subrayado(texto):
    return "\033[4m" + texto + "\033[0m"

texto = input("ingrese un texto que desee cambiar: ")
print(negrita(texto))
print(italica(texto))
print(subrayado(texto))
