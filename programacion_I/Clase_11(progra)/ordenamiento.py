# BURBUJEO #
# lista = [5,4,7,5,3]

# for i in range(len(lista)-1):
#     for j in range(i+1, len(lista)):
#         if(lista[i]>lista[j]):#Ordeno de menor a mayor#
#             print(f"i={i} - j={j}")
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux
# #Funciona con letras, ordena por orden alfabético determinado#
# print(lista)

lista = [{"nombre": "Juan", "edad":25},
         {"nombre": "Eduardo","edad":32},
         {"nombre": "Ana", "edad":32}]

# Ordenamiento por doble criterio #
for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        if(lista[i]["edad"] > lista[j]["edad"]):#Ordeno de menor a mayor#
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
        elif(lista[i]["edad"] == lista[j]["edad"]):
            if(lista[i]["nombre"] > lista[j]["nombre"]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

# Ordenamiento por doble criterio con menos líneas#
# for i in range(len(lista)-1):
#     for j in range(i+1, len(lista)):
#         if(lista[i]["edad"] > lista[j]["edad"]) or (lista[i]["edad"] == lista[j]["edad"]) and (lista[i]["nombre"] > lista[j]["nombre"]):
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux

print(lista)