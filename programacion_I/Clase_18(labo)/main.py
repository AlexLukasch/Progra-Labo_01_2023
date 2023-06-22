import pygame, sys
from modo import *
from configuraciones import *
from pygame.locals import *

#########################################################
def obtener_rectangulos(principal)->dict:
    diccionario = {}

    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -6, principal.width, 6)
    diccionario["right"] = pygame.Rect(principal.right -2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)

    return diccionario

def aplicar_gravedad(pantalla, que_hace, lados_personaje, lados_plataformas):
    global desplazamiento_y
    global bandera_estado_salto
    if bandera_estado_salto:
        animar_personaje(que_hace, pantalla, lados_personaje["main"])
        #lados_personaje["main"].y += desplazamiento_y

        for lado in rectangulo_personaje:
            lados_personaje[lado].y += desplazamiento_y

        if desplazamiento_y + gravedad < limite_velocidad_caida:
            desplazamiento_y += gravedad

    for piso in lados_plataformas:
        if lados_personaje["bottom"].collidirect(piso["top"]):
            lados_personaje["main"].bottom = piso["main"].top + 5 #Detecto la colision personaje-piso
            bandera_estado_salto = False
            desplazamiento_y = 0 #Freno el movimiento en y
            break
        else:
            bandera_estado_salto = True


def mover_personaje(lados_personaje, velocidad):
    for lado in lados_personaje:
        lados_personaje[lado].x += velocidad

def animar_personaje(acciones_personaje, pantalla, rectangulo_personaje):
    global contador_pasos #Digo que es una variable global
    largo = len(acciones_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0

    pantalla.blit(acciones_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1

def actualizar_pantalla(pantalla, que_hace, velocidad, lista_plataformas):
    global bandera_estado_salto
    global desplazamiento_y

    pantalla.blit(fondo,(0,0))
    #Recorrer la lista de plataformas para ubicar mas de una (FOR)
    pantalla.blit(plataforma,(lista_plataformas[1]["main"].x), (lista_plataformas[1]["main"]).y) # Plataforma

    match que_hace:
        case "derecha":
            if not bandera_estado_salto:
                animar_personaje(personaje_camina, pantalla, lados_personaje["main"])
            mover_personaje(lados_personaje, velocidad)
        case "izquierda":
            if not bandera_estado_salto:
                animar_personaje(personaje_camina_izquierda, pantalla, lados_personaje["main"])
            mover_personaje(lados_personaje, velocidad*-1)#multiplico por -1 para invertir la direccion
        case "salta":
            if not bandera_estado_salto:
                bandera_estado_salto = True
                desplazamiento_y = potencia_salto
            aplicar_gravedad(pantalla, personaje_salta, rectangulo_personaje)
        case "quieto":
            if not bandera_estado_salto:
                animar_personaje(personaje_quieto, pantalla, lados_personaje["main"])

    aplicar_gravedad(pantalla, personaje_salta, lados_personaje, lista_plataformas[0])#Cambie piso por su posicion en la lista


#########################################################
W, H = 1900,900
TAM_PANTALLA = (W,H)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAM_PANTALLA)

#FONDO
fondo = pygame.image.load("")
fondo = pygame.transform.scale(fondo,TAM_PANTALLA)

#VARIABLES_SALTO
gravedad = 1 #Velocidad a la que cae el personaje
potencia_salto = -15
limite_velocidad_caida = 15
bandera_estado_salto = False
desplazamiento_y = 0

#PERSONAJE
contador_pasos = 0
x_inicial = W/2 - 300
y_inicial = 650
posicion_actual_x = 0
velocidad = 10

lista_animaciones = [personaje_quiero,personaje_camina,personaje_salta]

reescalar_imagenes(lista_animaciones, 75, 85)

rectangulo_personaje = personaje_salta[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

lados_personaje = obtener_rectangulos(rectangulo_personaje)

que_hace = "quieto"

#PISO
piso = pygame.Rect(0,0, W, 20)
piso.top = rectangulo_personaje.bottom

lados_piso = obtener_rectangulos(lados_piso)

#PLATAFORMA
plataforma = pygame.image.load("ruta de la plataforma")
plataforma = pygame.transform.scale(plataforma,(400,75))
rectangulo_plataforma = plataforma.get_rect()
rectangulo_plataforma.x = 500
rectangulo_plataforma.y = 620

lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

lista_plataformas = [lados_piso, lados_plataforma]

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        que_hace = "salta"
    else:
        que_hace = "quieto"

    actualizar_pantalla(PANTALLA, que_hace, velocidad, lista_plataformas)

    if get_mode() == True:
        pygame.draw.rect(PANTALLA, "Blue", rectangulo_personaje, 2)
        pygame.draw.rect(PANTALLA, "Green", piso, 2)
        pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma, 2)

    pygame.display.update()