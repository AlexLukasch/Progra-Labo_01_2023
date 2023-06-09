import pygame
import random

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
FPS = 15

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Primer Jueguito")

#fuente = pygame.font.SysFont("Arial", 60)# Le pongo una fuente de texto
#texto = fuente.render("Hola estudiantes de 1BD",False,VERDE,AZUL_CLARO) #El booleano aca es para difuminar

circulos = []
for i in range(500):
    x = random.randint(1,ANCHO_VENTANA-1)
    y = random.randint(1,ALTO_VENTANA-1)
    circulos.append((x, y))# Creo 500 pares de coordenadas, círculos

reloj = pygame.time.Clock()

flag = True
while flag:
    reloj.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
    VENTANA.fill(NEGRO)
    # VENTANA.blit(texto,(100,200))

    for c in circulos:
        c[0] += 1 # Sumo a x
        c[1] += 2 # Sumo a Y
        if c[0] > ANCHO_VENTANA:
            c[0] = 0
        if c[1] > ALTO_VENTANA:
            c[1] = 0

    for c in circulos:
        pygame.draw.circle(VENTANA, ROJO, (c[0], c[1]), 5, 10)


    pygame.display.update()

pygame.quit()
