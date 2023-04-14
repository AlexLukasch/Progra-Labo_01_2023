# def convertir_strings_numeros_indice():
#     for i in range(len(lista_personajes)):
#         lista_personajes[i]['altura'] = float(lista_personajes[i]['altura'])
#         lista_personajes[i]['peso'] = float(lista_personajes[i]['peso'])
#         lista_personajes[i]['fuerza'] = int(lista_personajes[i]['fuerza']) 
from os import system
system('cls')

def confirmar_continuar():
    system('pause')

def confirmar_continuar_input():
    input("Presione enter tecla para continuar...\n")
    #Por el momento solo funciona con enter#

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
            print("Estoy en la opcion 1\n")
            confirmar_continuar_input()
        case 2:
            print("Estoy en la opcion 2\n")
            confirmar_continuar()
        case 3:
            print("Estoy en la opcion 3\n")
        case 4:
            print("Estoy en la opcion 4\n")
        case 5:
            print("Estoy en la opcion 5\n")
        case other:
            print("Saliendo del programa...\n")
            break