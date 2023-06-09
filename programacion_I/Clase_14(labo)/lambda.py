from data_stark import lista_personajes
from functools import reduce
def sumar(a, b):
    suma = a + b
    return suma

def restar(a, b):
    resta = a - b
    return resta

def multiplicar(a, b):
    resultado = a * b
    return resultado

def dividir(a, b):
    if (b != 0):
        retorno = a / b
    else:
        retorno = False
    return retorno

def calcular(a, b, operacion):
    return operacion(a, b)

# print(calcular(1, 2, sumar))
# print(calcular(5, 8, multiplicar))
# print(calcular(9, 3, restar))
# print(calcular(15, 0, dividir))

# OBJETOS DE PRIMERA CLASE #
# Se pueden asignar a una variable
# Se pueden pasar como parámetros de una función y retornarse

# def potenciar(a, b):
#     retorno = a ** b
#     return retorno

# def calcular(a, b, operacion):
#     return operacion(a, b)

# # Expresiones Lambda #
# resultado = calcular(3, 5, lambda a, b: a**b)
# resultado = calcular(3, 5, lambda a, b: a/b)
# print(resultado)

lista_numeros = [9, 5, 7, 3, 1, 5, 9, 2]

# MAP:
# Ejemplo una lista que reste 2 a cada elemento de la lista
# Map me devuelve un elemento de tipo map, debo convertirlo para usarlo
# nueva_lista = list(map(lambda item: item - 2, lista))
# print(nueva_lista)

############################################################################

# colores = set(map(lambda heroe: heroe["color_ojos"], lista_personajes))
# print(colores)

############################################################################

# FILTER:
# def buscar_pares(lista):
#     pares = []
#     for x in lista:
#         if x % 2 == 0:
#             pares.append(x)
#     return pares

#filtrada = buscar_pares(lista_numeros)
# filtrada = list(filter(lambda numero: numero % 2 == 0, lista_numeros))
# filtrada_femeninos = list(filter(lambda heroe: heroe["genero"] == "F", lista_personajes))

# print(filtrada)
# print(filtrada_femeninos)

# REDUCE #

# acumulador = 0
# for numero in lista_numeros:
#     acumulador = acumulador + numero

# total = reduce(lambda acumulador, numero: acumulador + numero, lista_numeros, 0)

# print(total)
maximo = 0
for numero in lista_numeros:
    if numero > maximo:
        maximo = numero

maximo = reduce(lambda maximo, numero: maximo if maximo > numero else numero, lista_numeros, 0)

print(maximo)
