#Ejercicio integrador_01_00 Alexander Lukasch Belbey 1B#
from data_stark import lista_personajes
from os import system
import math

system('cls')

def confirmar_continuar():
    input("Presione enter para continuar...\n")

def convertir_strings_numeros():
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        heroe['peso'] = float(heroe['peso'])
        heroe['fuerza'] = int(heroe['fuerza'])

def mostrar_nombres():
    print("Mostrando nombres de los superhéroes:\n")
    for heroe in lista_personajes:
        print(f"{heroe['nombre']}")

def mostrar_nombres_alturas():
    print("Mostrando nombre y altura de los superhéroes:\n")
    for heroe in lista_personajes:
        print(f"{heroe['nombre']}")
        print(f"Altura: {heroe['altura']}cm\n")

# def mostrar_mas_alto():
#     max_altura = 0
#     for heroe in lista_personajes:
#         if(max_altura == 0 or heroe["altura"] > max_altura):
#             max_altura = heroe["altura"]
#             nombre_mas_alto = heroe["nombre"]
#     print(f"El superhéroe más alto es: {nombre_mas_alto}")
#     print(f"Su altura es de: {max_altura}cm\n")

# def mostrar_mas_bajo():
#     min_altura = 0
#     for heroe in lista_personajes:
#         if(min_altura == 0 or heroe["altura"] < min_altura):
#             min_altura = heroe["altura"]
#             nombre_mas_bajo = heroe["nombre"]
#     print(f"El superhéroe más bajo es: {nombre_mas_bajo}")
#     print(f"Su altura es de: {min_altura}cm\n")

def mostrar_nombres_max_min_altura():
    max_altura = 0
    min_altura = 0
    for heroe in lista_personajes:
        if(max_altura == 0 or heroe["altura"] > max_altura):
            max_altura = heroe["altura"]
            nombre_mas_alto = heroe["nombre"]
    print(f"El superhéroe más alto es: {nombre_mas_alto}")
    print(f"Su altura es de: {max_altura}cm\n")  
    
    for heroe in lista_personajes:
        if(min_altura == 0 or heroe["altura"] < min_altura):
            min_altura = heroe["altura"]
            nombre_mas_bajo = heroe["nombre"]
    print(f"El superhéroe más bajo es: {nombre_mas_bajo}")
    print(f"Su altura es de: {min_altura}cm\n")  

def mostrar_altura_prom():
    acumulador_altura = 0
    contador_heroes = 0
    for i in range(len(lista_personajes)):
        acumulador_altura = acumulador_altura + lista_personajes[i]["altura"]

    prom_altura = acumulador_altura / i+1
    prom_altura = "{:.2f}".format(prom_altura)
    print(f"El promedio de altura de los superhéroes es: {prom_altura}cm\n")

def mostrar_pesos_max_min():
    max_peso = 0
    min_peso = 0
    for heroe in lista_personajes:
        if(max_peso == 0 or heroe["peso"] > max_peso):
            max_peso = heroe["peso"]
            nombre_mas_pesado = heroe["nombre"]

    for heroe in lista_personajes:
        if(min_peso == 0 or heroe["peso"] < min_peso):
            min_peso = heroe["peso"]
            nombre_mas_ligero = heroe["nombre"]

    print(f"El superhéroe más pesado es: {nombre_mas_pesado}")
    print(f"Su peso es de: {max_peso}kg\n")

    print(f"El superhéroe más ligero es: {nombre_mas_ligero}")
    print(f"Su peso es de: {min_peso}kg\n")

#Convierto los datos necesarios de string a int o float para poder hacer cálculos#
convertir_strings_numeros()

while True:
    opcion = int(input("/////////////////// MENU DE OPCIONES ///////////////////\n"
                       "Elija una opcion para mostrar la información:\n"
                       "1. Mostrar los nombres de los superhéroe.\n"
                       "2. Mostrar los nombres y altura de cada superhéroe.\n"
                       "3. Mostrar el superhéroe más alto y el más bajo.\n"
                       "4. Mostrar la altura promedio de los superhéroes.\n"
                       "5. Mostrar el superhéroe más y menos pesado.\n"
                       "Pulse cualquier otro número para salir del programa\n"
                       "////////////////////////////////////////////////////////\n"))
    match opcion:
        case 1:
            mostrar_nombres()
            confirmar_continuar()
        case 2:
            mostrar_nombres_alturas()
            confirmar_continuar()
        case 3:
            mostrar_nombres_max_min_altura()
            confirmar_continuar()
        case 4:
            mostrar_altura_prom()
            confirmar_continuar()
        case 5:
            mostrar_pesos_max_min()
            confirmar_continuar()
        case other:
            print("Saliendo del programa...\n")
            break