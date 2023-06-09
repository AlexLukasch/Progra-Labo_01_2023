import pygame, sys
from pygame.locals import *

pygame.init()
screen_size = (1000,500)
PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("HOMEROLAND")
# ICONO
icono = pygame.image.load(r"Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\icono_homero.png")
pygame.display.set_icon(icono)

# FONDO
fondo = pygame.image.load("Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\\fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, screen_size)
PANTALLA.blit(fondo,(0,0))

# MUSICA
pygame.mixer.music.load("Progra-Labo_01_2023\programacion_I\Clase_16(labo)\Recursos\intro.mp3")
pygame.mixer.music.play(-1)#Si lo dejo vacio se reproduce entero 1 vez, con -1 se loopea
pygame.mixer.music.set_volume(0.1)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
