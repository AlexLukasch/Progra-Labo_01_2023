from data_stark import * #Importo todo con el *#

#Listar los superhéroes agrupados por color de ojos#
'''
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
'''
def listar_agrupados(lista:list, key_ojos:str):
    lista_colores = []
    for heroe in lista:
        color = heroe[key_ojos]
        lista_colores.append(color)
    lista_colores_filtrada = set(lista_colores)

    for color in lista_colores_filtrada:
        print(color)
        for heroe in lista:
            if heroe[key_ojos] == color:
                print(f"\t{heroe['nombre']}")

    print(lista_colores_filtrada)



listar_agrupados(lista_personajes, "color_pelo")