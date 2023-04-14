nombre = "Jose"
edad = 25
#nombreDelPaciente = "Juan" NO SE USA CAMEL CASE#
nombre_del_paciente = "Pedro" #USAMOS SNAKE CASE#

#Los parentesis no hacen falta, pero si voy a poner condiciones multilinea debo usarlos#
if nombre == "Juan" and edad > 20:
    print("Bienvenido Juan")
else:
    if nombre == "Maria":
        print("Bienvenida Maria")
    else:
        if nombre == "Jose":
            print("Bienvenido Jose") 
        else:
            print("Bienvenido")

#Uso el pass para saltear una linea rellenando un bloque vacio para poner algo luego#
if (nombre == "Pedro"):
    pass

#para hacer un comentario de una linea uso el #

'''
De esta forma hago un comentario multilinea
Uso 3 comillas simples de apertura y de cierre
'''

# if nombre == "Juan":
#     print("Bienvenido Juan")
# else:
#     if nombre == "Maria":
#         print("Bienvenida Maria")
#     else:
#         if nombre == "Jose":
#             print("Bienvenido Jose") 
#         else:
#             print("Bienvenido")
# Tambien puedo comentar usando CTRL+K+C y descomentar usando CTRL+K+U