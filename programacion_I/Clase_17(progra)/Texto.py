import pygame

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Primer Jueguito")

fuente = pygame.font.SysFont("Arial", 60)# Le pongo una fuente de texto
texto = fuente.render("Hola estudiantes de 1BD",False,VERDE,AZUL_CLARO) #El booleano aca es para difuminar

flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        
    VENTANA.blit(texto,(100,200))
    pygame.display.update()

pygame.quit()
