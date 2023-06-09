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

def mostrar_una_key(lista:list, key:str):
    if(type(lista) == list and len(lista)>0):
        for heroe in lista:
            print(f"{heroe[key]}")

def mostrar_dos_keys(lista:list, key1:str, key2:str):
    if(type(lista) == list and len(lista)>0):
        for heroe in lista:
            print(f"{key1}: {heroe[key1]}")
            print(f"{key2}: {heroe[key2]}\n")

def buscar_maximo(lista:list, key_altura:str)->dict:
    if(type(lista) == list and len(lista)>0):
        flag_altura = 0
        for heroe in lista:
            if(flag_altura == 0 or heroe[key_altura] > max_altura):
                max_altura = heroe[key_altura]  
                flag_altura = 1 
                mas_alto = heroe
        return mas_alto

def buscar_minimo(lista:list, key_altura:str)->dict:
    if(type(lista) == list and len(lista)>0):
        flag_altura = 0
        for heroe in lista:
            if(flag_altura == 0 or heroe[key_altura] < min_altura):
                min_altura = heroe[key_altura]
                flag_altura = 1
                mas_bajo = heroe
        return mas_bajo

def mostrar_dos_datos(dict:dict, key_nombre:str, key_altura:str, mensaje_nombre:str, mensaje_altura:str):
    nombre_mas_alto = dict[key_nombre]
    altura = dict[key_altura]
    print(f"{mensaje_nombre} {nombre_mas_alto}")
    print(f"{mensaje_altura} {altura}\n")

def mostrar_altura_prom(lista:list, key_altura:str):
    if(type(lista) == list and len(lista)>0):
        acumulador_altura = 0
        contador_heroes = 0
        for i in range(len(lista)):
            acumulador_altura = acumulador_altura + lista[i][key_altura]
            contador_heroes = contador_heroes + 1
            
        prom_altura = acumulador_altura / contador_heroes
        prom_altura = "{:.2f}".format(prom_altura)
        print(f"El promedio de altura de los superhéroes es: {prom_altura}cm\n")

#Convierto los datos necesarios de string a int o float para poder hacer cálculos#
convertir_strings_numeros()

while True:
    opcion = int(input("/////////////////// MENU DE OPCIONES ///////////////////\n"
                       "Elija una opcion para mostrar la información:\n"
                       "1. Mostrar los nombres de los superhéroes.\n"
                       "2. Mostrar los nombres y altura de cada superhéroe.\n"
                       "3. Mostrar el superhéroe más alto y el más bajo.\n"
                       "4. Mostrar la altura promedio de los superhéroes.\n"
                       "5. Mostrar el superhéroe más y menos pesado.\n"
                       "Pulse cualquier otro número para salir del programa\n"
                       "////////////////////////////////////////////////////////\n"))
    match opcion:
        case 1:
            print("Mostrando nombres de los superhéroes:\n")
            mostrar_una_key(lista_personajes, "nombre")
            confirmar_continuar()
        case 2:
            print("Mostrando nombre y altura de los superhéroes:\n")
            mostrar_dos_keys(lista_personajes, "nombre", "altura")
            confirmar_continuar()
        case 3:
            #mostrar_nombres_max_min_altura(lista_personajes)
            mas_alto = buscar_maximo(lista_personajes, "altura")
            mostrar_dos_datos(mas_alto, "nombre", "altura", "El superhéroe más alto es:", "Su altura es de:")
            mas_bajo = buscar_minimo(lista_personajes, "altura")
            mostrar_dos_datos(mas_bajo, "nombre", "altura", "El superhéroe más bajo es:", "Su altura es de:")
            confirmar_continuar()
        case 4:
            mostrar_altura_prom(lista_personajes, "altura")
            confirmar_continuar()
        case 5:
            #mostrar_pesos_max_min(lista_personajes)
            mas_pesado = buscar_maximo(lista_personajes, "peso")
            mostrar_dos_datos(mas_pesado, "nombre", "peso", "El superhéroe más pesado es:", "Su peso es de:")
            mas_liviano = buscar_minimo(lista_personajes, "peso")
            mostrar_dos_datos(mas_liviano, "nombre", "peso", "El superhéroe más liviano es:", "Su peso es de:")
            confirmar_continuar()
        case other:
            print("Saliendo del programa...\n")
            break