# EJERCICIO_02
# Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
# python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
# al ingresar el número debemos mostrarle que regla de estilo representa y su
# descripción (Sacar la información de las diapositivas de las reglas de estilo).
# En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
# “Error, regla de estilo inexistente”

opcion = input("/////////////// REGLAS DE ESTILO /////////////\n"
               "Elija una opción para ver una regla de estilo\n"
               "1.\n2.\n3.\n4.\n"
               "5.\n6.\n7.\n8.\n")
opcion = int(opcion)
while(opcion > 8 or opcion < 1):
    opcion = input("ERROR. Por favor ingrese una opción del 1 al 8\n")
    opcion = int(opcion)

match(opcion):
    case 1:
        print("¿Qué es PEP?\n"
              "Python Enhancement Proposal es un documento"
              " que proporciona información a la comunidad de"
              " Python, o que describe una nueva característica.\n")
    case 2:
        print("¿Qué es PEP8?\n"
              "Es un conjunto de recomendaciones cuyo objetivo"
              " es ayudar a escribir código más legible y abarca"
              " desde cómo nombrar variables, al número máximo"
              " de caracteres que una línea debe tener.\n")
    case 3:
        print("Indentado\n"
              "Python no usa {} para designar bloques de código"
              " como otros lenguajes de programación, sino que"
              " usa bloques identados para indicar que un"
              " determinado bloque de código pertenece a por"
              " ejemplo un if.\n")
    case 4:
        print("Tamaño máximo de línea\n\n"
              "Se recomienda limitar el tamaño de cada línea a"
              " 79 caracteres, para evitar tener que hacer scroll a"
              " la derecha.\n")
    case 5:
        print("Líneas en blanco\n"
              "El uso de espacios en blanco mejora la legibilidad"
              " del código, y es por lo que la PEP8 indica dónde"
              " debemos usar espacios y dónde no.\n")
    case 6:
        print("Comentarios\n"
              "Cualquier comentario que contradiga el código es"
              " peor que ningún comentario.\n\n"
              "Si actualizamos el código, se debe actualizar los"
              " comentarios para evitar crear inconsistencias\n\n"
              "Evitar comentarios poco descriptivos que no"
              " aporten nada más allá de lo que ya se ve a simple"
              " vista.\n")
    case 7:
        print("Nombres\n"
              "Funciones: Uso de snake_case, letras en"
              " minúscula separadas por guión bajo: mi_funcion.\n\n"
              "Variables: Al igual que las funciones: variable,"
              " mi_variable.\n\n"
              "Clases: Uso de CamelCase, usando mayúscula y"
              " sin barra baja: MiClase, ClaseDePrueba.\n\n"
              "Métodos: Al igual que las funciones, usar snake"
              " case: metodo, mi_metodo.\n\n"
              "Constantes: Nombrarlas usando mayúsculas y"
              " separadas por guión bajas: UNA_CONSTANTE\n\n"
              "Módulos: Igual que las funciones: modulo.py,"
              " mi_modulo.py.\n")   
    case 8:
        print("Encoding (ñ)"
              "Los archivos se codifican por defecto en ASCII"
              " para Python 2 y UTF-8 para Python 3, por lo que"
              " será necesario definir la codificación que usemos"
              " cuando pretendamos usar otro tipo.\n") 