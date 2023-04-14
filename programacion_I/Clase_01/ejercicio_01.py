''' EJERCICIO_01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo ("barbijo", "jabón" o "alcohol")
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.
'''
import math 

#Ingreso de tipo de producto#
tipo_producto = str(input("Ingrese el tipo de producto (Barbijo|Jabon|Alcohol): "))
tipo_producto = str.lower(tipo_producto)

while(tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol"):
    print("Error, por favor ingrese un tipo de producto válido: ")
    tipo_producto = str(input("Ingrese el tipo de producto (Barbijo|Jabon|Alcohol): "))
    tipo_producto = str.lower(tipo_producto)
tipo_producto = str.title(tipo_producto)#Para validar el string lo paso todo a minúscula y luego uso title para poner la primera letra en mayúscula#

#Ingreso de precio#
precio_producto = input("Ingrese el precio unitario del producto: ")
precio_producto = float(precio_producto)

while(math.isnan(precio_producto)==True):
    print("Error, por favor ingrese un precio válido: ")
    precio_producto = int(input("Ingrese el precio del producto: "))

#Ingreso la cantidad de unidades#
cantidad_unidades = int(input("Ingrese la cantidad productos comprados: "))

while(math.isnan(cantidad_unidades)==True):
    print("Error, por favor ingrese una cantidad válida")
    precio_producto = int(input("Ingrese la cantidad productos comprados: "))

#Marca del producto#
marca = input("Ingrese la marca del producto:\n")
marca = str.title(marca)

#Fabricante del producto#
fabricante = input("Ingrese el fabricante del producto:\n")
fabricante = str.title(fabricante)

#Calculo el precio total#
precio_total = cantidad_unidades * precio_producto

#Salida de datos#
print("Tipo de producto:", tipo_producto)
print("Precio unitario del producto:", precio_producto)
print("Cantidad de unidades:", cantidad_unidades)
print("Marca del producto:", marca)
print("Fabricante del producto:", fabricante)
print("Precio total de la compra:", precio_total)
