import pygame, sys
from Class_imagen_2 import Imagen
from pygame.locals import *

ANCHO = 1000
ALTO = 500
FPS = 30

screen_size = (1000,500)
pygame.init()

PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("HOMEROLAND")
# ICONO
icono = pygame.image.load(r"Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\icono_homero.png")
pygame.display.set_icon(icono)

# FONDO
fondo = pygame.image.load("Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\\fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, screen_size)

# MUSICA
# pygame.mixer.music.load("Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\intro.mp3")
# pygame.mixer.music.play(-1)#Si lo dejo vacio se reproduce entero 1 vez, con -1 se loopea
# pygame.mixer.music.set_volume(0.1)

imagen_vertical = Imagen((100,100),(ANCHO//2, ALTO//2), "Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\dona.png")
imagen_horizontal = Imagen((150,200),(ANCHO-50,ALTO//2), "Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\homero.png")

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.blit(fondo,(0,0))

    PANTALLA.blit(imagen_vertical.imagen, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.imagen, imagen_horizontal.rectangulo)

    imagen_vertical.mover_imagen("Vertical", 10, (ANCHO,ALTO))
    imagen_horizontal.mover_imagen("Horizontal", 10, (ANCHO,ALTO))

    imagen_vertical.detectar_colision(imagen_vertical)

    pygame.display.flip()

