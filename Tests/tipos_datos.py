lista_personajes =\
[
  {
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
  },
  {
    "nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": "122.77",
    "peso": "25.73",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"
  }
]

lista_colores_ojos =\
[
    {
        "Blue": "Thor, Iron Man"
    },
    {
        "Brown": "Dr.Strange"
    }
]

def mostrar_una_key(lista:list, key:str, mensaje_key_1:str):
    if(type(lista) == list and len(lista)>0):
        for elemento in lista:
            print(f"{mensaje_key_1}{elemento[key]}")



#mostrar_una_key(lista_colores_ojos, "Blue", "Color X:")
if(lista_colores_ojos["Brown"] == lista_personajes[0]["color_ojos"]):
    print("HAY COINCIDENCIA\n")
else:
    print("ESTA TODO MAL\n")