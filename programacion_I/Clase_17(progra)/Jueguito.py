import pygame
from Donas import *
LARGO = 800
ALTO = 800
SCREEN_SIZE = (LARGO,ALTO)
FPS = 60

pygame.init()
RELOJ = pygame.time.Clock()
DERECHA = 1
IZQUIERDA = 0

# FUENTE
fuente = pygame.font.SysFont("Arial", 60)# Le pongo una fuente de texto
# PUNTAJE 
SCORE = 

tick = pygame.USEREVENT + 0 #Defino un evento personalizado
pygame.time.set_timer(tick, 50)

#PANTALLA
screen = pygame.display.set_mode(SCREEN_SIZE)

fondo = pygame.image.load(r"Progra-Labo_01_2023\programacion_I\Clase_17(progra)\Recursos\fondo.png")
fondo_final = pygame.transform.scale(fondo, SCREEN_SIZE)
screen.blit(fondo_final,(0,0))

########################################## HOMERO #########################################
imagen_homero_derecha = pygame.image.load("Progra-Labo_01_2023\programacion_I\Clase_17(progra)\Recursos\derecha.png")
imagen_homero_derecha = pygame.transform.scale(imagen_homero_derecha,(200,250))

imagen_homero_izquierda = pygame.transform.flip(imagen_homero_derecha,True,False)

imagen_homero = imagen_homero_derecha

rectangulo_homero = imagen_homero_derecha.get_rect()
rectangulo_homero.x = 400
rectangulo_homero.y = 570
rectangulo_homero.width = 200
rectangulo_homero.height = 200

x = 493
y = 658
z = 4

rectangulo_boca = pygame.Rect(x,y,z,z)

personaje = {"superficie": imagen_homero, "rectangulo": rectangulo_homero, "rect_boca": rectangulo_boca, "score": 0}

# DONAS
lista_donas = crear_lista_donas(50)

flag = True
while flag:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == tick:
            update_donas(lista_donas)

    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_RIGHT]:
        #imagen_homero_derecha = pygame.image.load("Progra-Labo_01_2023\programacion_I\Clase_17(progra)\Recursos\derecha.png")
        #imagen_homero_derecha = pygame.transform.scale(imagen_homero,(200,250))
        imagen_homero = imagen_homero_derecha
        nueva_x = rectangulo_homero.x + 10
        if nueva_x > 0 and nueva_x < LARGO - rectangulo_homero.width:
            rectangulo_homero.x += 10

    if lista_teclas[pygame.K_LEFT]:
        #imagen_homero_izquierda = pygame.image.load("Progra-Labo_01_2023\programacion_I\Clase_17(progra)\Recursos\izquierda.png")
        #imagen_homero_izquierda = pygame.transform.scale(imagen_homero,(200,250))
        imagen_homero = imagen_homero_izquierda
        nueva_x = rectangulo_homero.x - 10
        if nueva_x > 0 and nueva_x < LARGO:
            rectangulo_homero.x -= 10

    screen.blit(fondo, (0,0))
    screen.blit(imagen_homero,rectangulo_homero)

    for dona in lista_donas:
        screen.blit(dona["superficie"], dona["rectangulo"])

    verificar_colision(lista_donas, personaje)

    texto = fuente.render(f"SCORE")

    pygame.display.update()


pygame.quit()