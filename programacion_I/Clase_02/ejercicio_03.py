# EJERCICIO_03
# Es la gala final de Gran Hermano y la producción nos pide un programa para contar
# los votos de los televidentes y saber cuál será el participante que ganará el juego.
# Los participantes finalistas son: Nacho, Julieta y Marcos.
# El televidente debe ingresar:
# ● Nombre del votante
# ● Edad del votante (debe ser mayor a 13)
# ● Género del votante (masculino, femenino, otro)
# ● El nombre del participante a quien le dará el voto positivo.
# No se sabe cuántos votos entrarán durante la gala.
# Se debe informar al usuario:
# A. El promedio de edad de las votantes de género femenino
# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
# Nacho o Julieta.
# C. Nombre del votante más joven que votó a Nacho.
# D. Nombre de cada participante y porcentaje de los votos qué recibió.
# E. El nombre del participante que ganó el reality (El que tiene más votos)

opcion = "si"
acumulador_edad_femenino = 0
contador_votos_femeninos = 0
contador_votos_B = 0
contador_votos_nacho = 0
contador_votos_julieta = 0
contador_votos_marcos = 0
bandera_voto_joven = 0

#Ingreso de datos#
while(opcion == "si" or opcion == "s"):
    print("Rellene los siguientes datos")
    nombre_votante = input("Nombre del votante: ")
    nombre_votante = str.title(nombre_votante)

    edad_votante = int(input("Ingrese la edad del votante: "))
    while(edad_votante < 13):
        print("ERROR. El votante debe ser mayor a 13 años")
        edad_votante = int(input("Por favor ingrese una edad válida (Mayor a 13 años) "))

    genero_votante = str.lower(input("Ingrese el género del votante [Masculino|Femenino|Otro] "))
    
    while((genero_votante != "masculino" and genero_votante != "m") and
           (genero_votante != "femenino" and genero_votante != "f") and 
           (genero_votante != "otro" and genero_votante != "o")):
        genero_votante = str.lower(input("ERROR. Ingrese un género del votante válido [Masculino|Femenino|Otro]\n"))
    
    voto_positivo = str.lower(input("Ingrese a quien le dará el voto positivo [Nacho | Julieta | Marcos] "))
    while(voto_positivo != "nacho" and voto_positivo != "julieta" and voto_positivo != "marcos"):
        voto_positivo = str.lower(input("ERROR. Por favor ingrese un participante válido para el voto positivo [Nacho | Julieta | Marcos]"))

    #Contadores y acumuladores#
    #A#
    if(genero_votante == "femenino" or genero_votante == "f"):
        acumulador_edad_femenino += edad_votante
        contador_votos_femeninos += 1
    #B#
    if(voto_positivo == "nacho" or voto_positivo == "julieta"):
        if(genero_votante == "masculino" or genero_votante == "m"):
            if(edad_votante > 24 and edad_votante < 41):
                contador_votos_B += 1

    #Operaciones según votos#
    match(voto_positivo):
        case "marcos":
            contador_votos_marcos += 1
        case "julieta":
            contador_votos_julieta += 1
        case "nacho":
            if(bandera_voto_joven == 0 or edad_votante < edad_menor_votante_nacho):
                edad_menor_votante_nacho = edad_votante
                bandera_voto_joven = 1
            contador_votos_nacho += 1
            edad_menor_votante_nacho = edad_votante
            nombre_menor_votante_nacho = nombre_votante
    #E#
    
    if(contador_votos_marcos > contador_votos_julieta and contador_votos_marcos > contador_votos_nacho):
        ganador = "Marcos"
    elif(contador_votos_julieta > contador_votos_marcos and contador_votos_julieta > contador_votos_nacho):
        ganador = "Julieta"
    elif(contador_votos_nacho > contador_votos_marcos and contador_votos_nacho > contador_votos_julieta):
        ganador = "Nacho"
    else:
        ganador = "empate"

    opcion = str.lower(input("¿Desea cargar otro voto?[Si/No]\n"))

#Muestro la información pedida#
print("//////////////////////// RESULTADOS ////////////////////////\n")
if(contador_votos_femeninos > 0):  
    prom_edad_votos_f = acumulador_edad_femenino / contador_votos_femeninos
    print("El promedio de edad de las votantes de género femenino es: ", prom_edad_votos_f)
else:
    print("No hay votos femeninos")

if(contador_votos_B > 0):
    print("Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta: ",contador_votos_B)
else:
    print("No hay votantes masculinos de entre 25 y 40 años votantes de Nacho o Julieta")

if(bandera_voto_joven != 0):
    print("El nombre del votante más joven de Nacho es: ",nombre_menor_votante_nacho)
else:
    print("No hay votante más joven de Nacho")

print("Votos de cada participante: \n"
      "Nacho: ", contador_votos_nacho)
print("Julieta: ", contador_votos_julieta)      
print("Marchos: ", contador_votos_marcos)   

if(ganador != "empate"):
    print("============================\n"
      "EL GANADOR ES: ", ganador, "\n"
      "============================")
else:
    print("==============================\n"
          "Hubo un empate, no hay ganador\n "
          "==============================")