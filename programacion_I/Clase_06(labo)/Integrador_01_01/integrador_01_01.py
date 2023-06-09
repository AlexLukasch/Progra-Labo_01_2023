#Ejercicio integrador_01_01 Alexander Lukasch Belbey 1B#
from data_stark import lista_personajes
from funciones_integrador_01 import *
from os import system
system('cls')

lista_C_a_F = []
bandera_opcion_8 = 0
bandera_opcion_9 = 0
bandera_opcion_10 = 0
bandera_opcion_11 = 0

#Convierto los datos necesarios de string a int o float para poder hacer cálculos#
convertir_strings_numeros(lista_personajes)

while True:
    opcion = int(input("/////////////////// MENU DE OPCIONES ///////////////////\n"
                       "Elija una opcion para mostrar la información:\n"
                       "1. Mostrar los nombres de los superhéroes.\n"
                       "2. Mostrar los nombres y altura de cada superhéroe.\n"
                       "3. Mostrar el superhéroe más alto y el más bajo.\n"
                       "4. Mostrar la altura promedio de los superhéroes.\n"
                       "5. Mostrar el superhéroe más y menos pesado.\n"
                       "6. Mostrar superhéroes masculinos.\n"
                       "7. Mostrar superhéroes femeninos.\n"
                       "8. Mostrar el superhéroe más alto de género M.\n"
                       "9. Mostrar el superhéroe más alto de género F.\n"
                       "10. Mostrar el superhéroe más bajo de género M.\n"
                       "11. Mostrar el superhéroe más bajo de género F.\n"
                       "12. Mostrar la altura promedio de los superhéroes masculinos.\n"
                       "13. Mostrar la altura promedio de los superhéroes femeninos.\n"
                       "14. Mostrar los nombres de los superhéroes más altos y bajos de cada género.\n"
                       "15. Mostrar cuantos superhéroes tienen cada color de ojos.\n"
                       "16. Mostrar cuantos superhéroes tienen cada color de pelo.\n"
                       "17. Mostrar cuantos superhéroes tienen cada tipo de inteligencia.\n"
                       "18. Mostrar los superhéroes agrupados por color de ojos.\n"
                       "19. Mostrar los superhéroes agrupados por color de pelo.\n"
                       "20. Mostrar los superhéroes agrupados por tipo de inteligencia.\n"
                       "Pulse cualquier otro número para salir del programa\n"
                       "////////////////////////////////////////////////////////\n"))
    match opcion:
        case 1:
            print("Mostrando nombres de los superhéroes:\n")
            mostrar_una_key(lista_personajes, "nombre", "")
            confirmar_continuar()
        case 2:
            print("Mostrando nombre y altura de los superhéroes:\n")
            mostrar_dos_keys(lista_personajes, "nombre", "altura", "Nombre: ", "Altura: ")
            confirmar_continuar()
        case 3:
            mas_alto = buscar_maximo(lista_personajes, "altura")
            mostrar_dos_datos(mas_alto, "nombre", "altura", "El superhéroe más alto es:", "Su altura es de:")
            mas_bajo = buscar_minimo(lista_personajes, "altura")
            mostrar_dos_datos(mas_bajo, "nombre", "altura", "El superhéroe más bajo es:", "Su altura es de:")
            confirmar_continuar()
        case 4:
            prom_altura = calcular_promemdio(lista_personajes, "altura")
            print(f"El promedio de altura de los superhéroes es: {prom_altura}cm\n")
            confirmar_continuar()
        case 5:
            mas_pesado = buscar_maximo(lista_personajes, "peso")
            mostrar_dos_datos(mas_pesado, "nombre", "peso", "El superhéroe más pesado es:", "Su peso es de:")
            mas_liviano = buscar_minimo(lista_personajes, "peso")
            mostrar_dos_datos(mas_liviano, "nombre", "peso", "El superhéroe más liviano es:", "Su peso es de:")
            confirmar_continuar()
        case 6:#A#
            lista_masculinos = filtrar_un_criterio(lista_personajes, "genero", "M")
            print("Mostrando superhéroes de género masculino:\n")
            mostrar_una_key(lista_masculinos, "nombre", "Nombre: ")
            confirmar_continuar()
        case 7:#B#
            lista_femeninos = filtrar_un_criterio(lista_personajes, "genero", "F")
            print("Mostrando superhéroes de género femenino:\n")
            mostrar_una_key(lista_femeninos, "nombre", "Nombre: ")
            confirmar_continuar()
        case 8:#C#
            lista_masculinos = filtrar_un_criterio(lista_personajes, "genero", "M")
            mas_alto_masculino = buscar_maximo(lista_masculinos, "altura")
            lista_C_a_F.append(mas_alto_masculino)#Guardo para el punto I#
            mostrar_dos_datos(mas_alto_masculino, "nombre", "altura", "El superhéroe más alto de género M es:", "Su altura es de:")
            bandera_opcion_8 = 1
            confirmar_continuar()
        case 9:#D#
            lista_femeninos = filtrar_un_criterio(lista_personajes, "genero", "F")
            mas_alto_femenino = buscar_maximo(lista_femeninos, "altura")
            lista_C_a_F.append(mas_alto_femenino)#Guardo para el punto I#
            mostrar_dos_datos(mas_alto_femenino, "nombre", "altura", "El superhéroe más alto de género F es:", "Su altura es de:")
            bandera_opcion_9 = 1
            confirmar_continuar()
        case 10:#E#
            lista_masculinos = filtrar_un_criterio(lista_personajes, "genero", "M")
            mas_bajo_masculino = buscar_minimo(lista_masculinos, "altura")
            lista_C_a_F.append(mas_bajo_masculino)#Guardo para el punto I#
            mostrar_dos_datos(mas_bajo_masculino, "nombre", "altura", "El superhéroe más bajo de género M es:", "Su altura es de:")
            bandera_opcion_10 = 1
            confirmar_continuar()
        case 11:#F#
            lista_femeninos = filtrar_un_criterio(lista_personajes, "genero", "F")
            mas_bajo_femenino = buscar_minimo(lista_femeninos, "altura")
            lista_C_a_F.append(mas_bajo_femenino)#Guardo para el punto I#
            mostrar_dos_datos(mas_bajo_femenino, "nombre", "altura", "El superhéroe más bajo de género F es:", "Su altura es de:")
            bandera_opcion_11 = 1
            confirmar_continuar()
        case 12:#G#
            lista_masculinos = filtrar_un_criterio(lista_personajes, "genero", "M")
            promedio_altura_masculinos = calcular_promemdio(lista_masculinos, "altura")
            print(f"El promedio de altura de los superhéroes masculinos es: {promedio_altura_masculinos}cm\n")
            confirmar_continuar()
        case 13:#H#
            lista_femeninos = filtrar_un_criterio(lista_personajes, "genero", "F")
            promedio_altura_femeninos = calcular_promemdio(lista_femeninos, "altura")
            print(f"El promedio de altura de los superhéroes femeninos es: {promedio_altura_femeninos}cm\n")
            confirmar_continuar()
        case 14:#I#(C a F)
            if(bandera_opcion_8 == 1 and bandera_opcion_9 == 1 and bandera_opcion_10 == 1 and bandera_opcion_11 == 1):
                mostrar_un_dato(lista_C_a_F[0], "nombre", "Nombre del superhéroe más alto de género M: ")
                mostrar_un_dato(lista_C_a_F[1], "nombre", "Nombre del superhéroe más alto de género F: ")
                mostrar_un_dato(lista_C_a_F[2], "nombre", "Nombre del superhéroe más bajo de género M: ")
                mostrar_un_dato(lista_C_a_F[3], "nombre", "Nombre del superhéroe más bajo de género F: ")
            else:
                print("ERROR. Primero calcule las opciones 8,9,10 y 11 para mostrar los nombres!\n")
            confirmar_continuar()
        case 15:#J#
            normalizar_letras_capitales(lista_personajes, "color_ojos")
            diccionario_colores_ojos = contar_elementos_por_clave(lista_personajes, "color_ojos")
            print("Mostrando cantidad de cada color de ojos:")
            mostrar_un_diccionario(diccionario_colores_ojos)
            confirmar_continuar()
        case 16:#K#
            normalizar_letras_capitales(lista_personajes, "color_pelo")
            normalizar_claves_vacias(lista_personajes, "color_pelo", "No hair")
            diccionario_colores_pelo = contar_elementos_por_clave(lista_personajes, "color_pelo")
            print("Mostrando cantidad de cada color de pelo:")
            mostrar_un_diccionario(diccionario_colores_pelo)
            confirmar_continuar()
        case 17:#L#
            normalizar_letras_capitales(lista_personajes, "inteligencia")
            normalizar_claves_vacias(lista_personajes, "inteligencia", "No tiene")
            diccionario_inteligencia= contar_elementos_por_clave(lista_personajes, "inteligencia")
            print("Mostrando cantidad de cada tipo de inteligencia:")
            mostrar_un_diccionario(diccionario_inteligencia)
            confirmar_continuar()
        case 18:#M#
            normalizar_letras_capitales(lista_personajes, "color_ojos")
            diccionario_colores_ojos = guardar_elementos_por_clave(lista_personajes, "color_ojos")
            print("Mostrando los superhéroes agrupados por color de ojos:")
            mostrar_un_diccionario(diccionario_colores_ojos)
            ###################################
            print(diccionario_colores_ojos)
            ###################################
            confirmar_continuar()
        case 19:#N#
            normalizar_letras_capitales(lista_personajes, "color_pelo")
            diccionario_colores_pelo = guardar_elementos_por_clave(lista_personajes, "color_pelo")
            print("Mostrando los superhéroes agrupados por color de pelo:")
            mostrar_un_diccionario(diccionario_colores_pelo)
            confirmar_continuar()
        case 20:#O#
            normalizar_letras_capitales(lista_personajes, "inteligencia")
            normalizar_claves_vacias(lista_personajes, "inteligencia", "No tiene")
            diccionario_inteligencia = guardar_elementos_por_clave(lista_personajes, "inteligencia")
            print("Mostrando los superhéroes agrupados por tipo de inteligencia:")
            mostrar_un_diccionario(diccionario_inteligencia)
            confirmar_continuar()
        case other:
            print("Saliendo del programa...\n")
            break