# Ejercicio 05
# Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento
# de HR dispone de lista de justicieros pero solo tiene información detallada de algunos de
# ellos.
# Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista
# heroes_info se puedan listar los datos de cada héroe con el siguiente formato:
from os import system
system('cls')

heroes_info = [
    {
        "Nombre":"Super Girl",
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    {
        "Nombre":"Shazam",
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson",
    },
    {
        "Nombre":"Power Girl",
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    {
        "Nombre":"Wonder Woman",
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
]

#Recorro la lista de heroes, donde heroe es un diccionario#
for heroe in heroes_info:
    #Quito las repeticiones de habilidades en cada heroe con set#
    set_habilidades = set(heroe["Habilidades"])
    print(f"ID: {heroe['ID']}, Codename: {heroe['Nombre']}")
    print(f"Identidad: {heroe['Identidad']}, Origen: {heroe['Origen']}")

    #Como set_habilidades ya tiene la lista de habilidades, no pongo ['habilidades'] aca"#
    # print(f"Habilidades: {set_habilidades}")
    habilidades = "Habilidades: "
    habilidades_string = ""
    i = 0

    for habilidad in set_habilidades:
        if(i==0):
            habilidades_string += habilidad
            habilidades_string += " | "
        elif(i+1==len(set_habilidades)):
            habilidades_string += habilidad
        else:
            habilidades_string += habilidad
            habilidades_string += " | "
        i = i + 1

    habilidades += habilidades_string
    print(habilidades)
    print("----------------------------------------\n\n")