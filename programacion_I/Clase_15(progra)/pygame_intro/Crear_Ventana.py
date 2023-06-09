import pygame, sys

pygame.init()

PANTALLA = pygame.display.set_mode((500,400))#Width y Height
pygame.display.set_caption("Test_Juego")

PANTALLA.fill((255,255,255))
# PANTALLA.fill("Red")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.fill()

