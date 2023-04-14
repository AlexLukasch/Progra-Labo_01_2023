#LISTAS#
#Definir y agregar elementos por extension y por metodo append#
mi_lista = []

#Con append agrego elementos#
mi_lista.append(4) # 0
mi_lista.append(5) # 1
mi_lista.append(2) # 2
mi_lista.append(6) # 3

#print(mi_lista)#
#Recorrer listas por indice y por elementos, permite modificar#
# for i in range(len(mi_lista)):
#     print(mi_lista[i])

#Recorro con una variable que toma cada elemento de la lista, y solo se usa para lectura#
for numero in mi_lista:
    print(numero)

#Eliminar elementos de una lista#
mi_lista.remove(2)
print(mi_lista)

#TUPLAS, colecciones inmutables#
mi_tupla = (3,6,9,7)
print(type(mi_tupla))

#SET, coleccion que toma como base otra coleccion y quita los duplicados#
mi_set = set([5,6,9,5,7,4,5,3])
print(mi_set)

#Diccionarios#
#Definicion por extension#
# mi_diccionario = {"codigo":5, "descripcion":"Coca-Cola"}
# print(mi_diccionario)
# mi_diccionario = {}
# mi_diccionario["codigo"] = 5
# mi_diccionario["descripcion"] = "Coca-Cola"
# print(mi_diccionario["codigo"])
# for clave in mi_diccionario:
#     print(clave)

# for clave in mi_diccionario:
#     print(f"{clave}: {mi_diccionario[clave]}")
#Definición de un diccionario#

#Definir un diccionario y agregar claves y valores#

#Obtener claves#

#Obtener valores#

#Listas de DICCIONARIOS#
# lista_productos = []
# producto1 = {"codigo":5, "descripcion":"Coca-Cola", "Precio": 400}
# producto2 = {"codigo":2, "descripcion":"Pepsi", "Precio": 350}
# producto3 = {"codigo":9, "descripcion":"Fanta", "Precio": 300}
# lista_productos = [producto1,producto2,producto3]

# lista_productos.append(producto1)
# lista_productos.append(producto2)
# lista_productos.append(producto3)

lista_productos = []
CANTIDAD = 3
for i in range(CANTIDAD):
    codigo = int(input("Ingrese el codigo: "))
    descripcion = input("Ingrese la descripcion: ")
    precio = float(input("Ingrese el precio: "))
    un_producto = {}#En cada iteracion creo un nuevo diccionario en memoria#
    un_producto["codigo"] = codigo
    un_producto["descripcion"] = descripcion
    un_producto["precio"] = precio
    lista_productos.append(un_producto)

for producto in lista_productos:
    print(f"{producto['codigo']}--{producto['descripcion']}--{producto['precio']}")
# print(lista_productos)

#Crear la lista y cargar elementos#

#Recorrer la lista y mostrar los elementos#