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

flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

    lista_teclas = pygame.key.get_pressed()
    if(lista_teclas[pygame.K_f]):
        print("Presionaste F")
    if(lista_teclas[pygame.K_LEFT]):
        print("Izquierda")  
    if(lista_teclas[pygame.K_RIGHT]):
        print("Derecha")  
    if(lista_teclas[pygame.K_ESCAPE]):
        print("Saliendo...")    
        flag = False    

    pygame.display.update()

pygame.quit()
