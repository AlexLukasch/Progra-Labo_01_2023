import pygame

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return lista_girada

def reescalar_imagenes(lista_imagenes, W, H):
    for lista in lista_imagenes:
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i], (W, H))


personaje_camina_izquierda = girar_imagenes(personaje_camina_izquierda, True, False)