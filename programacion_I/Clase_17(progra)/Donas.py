import pygame
import random

def crear_dona(x, y, ancho, alto, path):
    imagen_dona = pygame.image.load(path)
    imagen_dona = pygame.transform.scale(imagen_dona, (ancho, alto))

    rectangulo = imagen_dona.get_rect()
    rectangulo.x = x
    rectangulo.y = y

    diccionario_dona = {}
    diccionario_dona["superficie"] = imagen_dona
    diccionario_dona["rectangulo"] = rectangulo
    diccionario_dona["velocidad"] = random.randrange(1,5,1)

    return diccionario_dona

def crear_lista_donas(cantidad):
    lista = []
    for i in range(cantidad):
        x = random.randrange(0, 740, 60)
        y = random.randrange(-1000, 0, 60)
        diccionario = crear_dona(x,y,60,60,"Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\dona.png")
        lista.append(diccionario)

    return lista

def update_donas(lista_donas):
    for dona in lista_donas:
        rect = dona["rectangulo"]
        rect.y += dona["velocidad"]

def verificar_colision(lista_donas, personaje):
    for dona in lista_donas:
        rectangulo = pygame.Rect(personaje["rectangulo"])
        if rectangulo.colliderect(dona["rectangulo"]):
            print("Colisiono")
            desaparecer_dona(dona)
        if dona["rectangulo"].y > 720:
            desaparecer_dona(dona)
            
def desaparecer_dona(dona):
    dona["rectangulo"].x = random.randrange(0.740,60)
    dona["rectangulo"].y = random.randrange(-1000,0,60)
 