import pygame, sys
from Class_imagen import Imagen
from pygame.locals import *

AZUL = (0,0,255)
ROJO = (255,0,0)

ANCHO = 800
ALTO = 600
FPS = 40

pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO,ALTO))#Width y Height
pygame.display.set_caption("Test_Juego_2")

imagen_vertical = Imagen((100,100),(ANCHO//2, ALTO//2),("Green","Red"))
imagen_horizontal = Imagen((100,100),(ANCHO-50,ALTO//2),("Blue","White"))

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.fill("Black")

    pygame.draw.line(PANTALLA,"Blue",(400,0),(400,800),1)
    pygame.draw.line(PANTALLA,"Blue",(0,300),(800,300),1)

    PANTALLA.blit(imagen_vertical.imagen, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.imagen, imagen_horizontal.rectangulo)

    imagen_vertical.mover_imagen("Vertical", 10, (ANCHO,ALTO))
    imagen_horizontal.mover_imagen("Horizontal", 10, (ANCHO,ALTO))

    # if imagen_vertical.rectangulo.colliderect(imagen_horizontal.rectangulo):
    #     imagen_horizontal.imagen.fill(imagen_horizontal.color_colision)
    #     imagen_vertical.imagen.fill(imagen_vertical.color_colision)
    # else:
    #     imagen_horizontal.imagen.fill(imagen_horizontal.color)
    #     imagen_vertical.imagen.fill(imagen_vertical.color)

    imagen_vertical.detectar_colision(imagen_horizontal)

    pygame.display.flip()

