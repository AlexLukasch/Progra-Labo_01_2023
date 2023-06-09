import pygame

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

timer_event = pygame.USEREVENT + 0 #Defino un evento personalizado
pygame.time.set_timer(timer_event, 1000)
reloj = pygame.time.Clock()

flag = True
while flag:
    reloj.tick(15)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        if evento.type == timer_event:
            print("SE ACTIVO EL EVENTO PERSONALIZADO")

    

    pygame.display.update()

pygame.quit()
