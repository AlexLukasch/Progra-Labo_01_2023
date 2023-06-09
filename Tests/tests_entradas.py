from validaciones import *
import re

def normalizar_habilidades(lista:list):
    for elemento in lista:
        #cadena = elemento["habilidades"]
        #cadena_nueva = re.sub(cadena, " - ", " |$%")
        print(elemento["habilidades"])
        elemento["habilidades"] = re.split("\\s+\|\$%|\|\$%", elemento["habilidades"])
        #"[,\n]"

#result = re.sub("\\s+", " ", texto) #si uso r no uso \

lista_personajes = \
[
    {'id': 1, 'nombre': 'Babidi', 'raza': 'Wizard', 'poder_pelea': 20, 'poder_ataque': 1, 'habilidades': 'Mind Control |$%Summon Majins'}, 
    {'id': 2, 'nombre': 'Broly', 'raza': 'Saiyan', 'poder_pelea': 2000000, 'poder_ataque': 300000, 'habilidades': 'Gigantic Meteor|$%Omega Blaster'}
]

normalizar_habilidades(lista_personajes)
print(lista_personajes)

