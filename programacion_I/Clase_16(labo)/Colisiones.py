import pygame, sys
from pygame.locals import *

AZUL = (0,0,255)
ROJO = (255,0,0)

ANCHO = 800
ALTO = 600
FPS = 30

pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO,ALTO))#Width y Height
pygame.display.set_caption("Test_Juego_2")
# PANTALLA.fill((255,255,255))
imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill("Green")

rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (ANCHO//2, ALTO//2)

imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill("Blue")

rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (ANCHO//2, ALTO//2)

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.fill("Black")

    rectangulo_vertical.y += 10
    PANTALLA.blit(imagen_vertical, rectangulo_vertical)
    if rectangulo_vertical.top > ALTO:
        rectangulo_vertical.bottom = 0

    rectangulo_horizontal.x += 10
    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)
    if rectangulo_horizontal.left> ANCHO:
        rectangulo_horizontal.right = 0

    if rectangulo_vertical.colliderect(rectangulo_horizontal):
        imagen_horizontal.fill("Red")
        imagen_vertical.fill("White")
    else:
        imagen_horizontal.fill("Green")
        imagen_vertical.fill("Blue")

    pygame.draw.line(PANTALLA,"Blue",(400,0),(400,800),1)
    pygame.draw.line(PANTALLA,"Blue",(0,300),(800,300),1)

    pygame.display.flip()

