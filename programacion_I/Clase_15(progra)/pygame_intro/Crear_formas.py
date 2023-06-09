import pygame, sys

AZUL = (0,0,255)

pygame.init()

PANTALLA = pygame.display.set_mode((500,400))#Width y Height
pygame.display.set_caption("Test_Juego")
PANTALLA.fill((255,255,255))

rectangulo = pygame.draw.rect(PANTALLA, "Blue", (100,50, 100, 50),1)
rectangulo_2 = pygame.draw.rect(PANTALLA, "Green", (250, 100, 25, 100),3)

pygame.draw.line(PANTALLA, "Green", (100, 105), (199, 20), 1)

pygame.draw.circle(PANTALLA, AZUL, (100,100), 25, 1)

pygame.draw.ellipse(PANTALLA, "Red", (270, 150, 40, 80), 5)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

