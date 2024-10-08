"""
Lucas Aguiar. Programacion1 
Escriba un programa que pueda tomar los detalles de los productos (nombre, cantidad, precio) 
y produzca una factura bien formateada.
"""

#Pedimos al usuario que ingrese el nombre de un producto
producto=input("por favor ingrese el nombre de un producto:")

#pedimos al usuario que ingrese la cantidad del producto
cantidad=input("por favor ingrese la cantidad:")

#pedimos al usuario que ingrese el precio del producto
precioindividual=input("por favor ingrese el precio del producto:")

#calculamos el precio total de nuestra compra
preciototal= int(cantidad) * int (precioindividual) 

#imprimimos la factura 
print("el producto es:",producto)
print("la cantidad es:", cantidad)
print("el precio es:", precioindividual)
print("el precio total de su compra es:",preciototal)

print("Muchas garcias por elegirnos, vuelva pronto!")
