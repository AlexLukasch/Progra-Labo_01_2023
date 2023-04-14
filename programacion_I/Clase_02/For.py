# El range() genera una secuencia de números que van desde
# cero por defecto hasta el número que se pasa como parámetro menos uno.

# mi_lista = list(range(5))
# print(mi_lista)
#Me muestra los números del 0 al 4#

# mi_lista = list(range(10,20,2))
# print(mi_lista)
#Me muestra los números del 10 al 18 saltando de a 2#

# acumulador = 0
# for x in range(5):#El rango son las veces que se repetirá el for#
#     numero = int(input("Ingrese un numero: "))
#     acumulador += numero

# print("Valor acumulado: ", acumulador)

#En este caso el rango esta definido por los elementos de la lista#
# lista_nombres = ["Luis","Nicolas","Federico","Micaela","Silvina"]
# for nombre in lista_nombres:
#     print(nombre)

#Break#
# lista_numeros=[1,2,4,5,77,-1]
# for numero in lista_numeros:
#     if(numero==5):
#         break
#     print(numero)

#Continue se salta el código restante en la iteración actual#
#Y vuelve al principio si quedan iteraciones a completar#
# lista_numeros=[1,2,4,5,77,-1]
# for numero in lista_numeros:
#     if(numero==5):
#         continue
#     print(numero)

#Match#
color = str.lower(input("Ingrese un color\n"))

match(color):
    case "azul":
        print("Es azul")
    case "rojo":
        print("Es rojo")
    case "amarillo":
        print("Es amarillo")
    case "verde":
        print("Es verde")
    case other:#El caso default, también puede ser "case _:"#
        print("Es otro color")