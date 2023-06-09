import pygame

class Imagen:
    def __init__(self, tamaño, origen, colores):#Le paso tuplas(RED, GREEN)
        self.imagen = pygame.Surface(tamaño)
        self.color = colores[0]
        self.color_colision = colores[1]
        self.imagen.fill(self.color)
        self.rectangulo = self.imagen.get_rect() #Tomo el rectangulo creado antes
        self.rectangulo.center = origen

    def mover_imagen(self,sentido: str,desplazamiento: int, tamaño_pantalla: tuple):
        if(sentido == "Vertical"):
            self.rectangulo.y += desplazamiento
            if(self.rectangulo.top > tamaño_pantalla[1]):
                self.rectangulo.bottom = 0
        else:
            self.rectangulo.x += desplazamiento
            if(self.rectangulo.left > tamaño_pantalla[0]):
                self.rectangulo.right = 0

    def detectar_colision(self, otra_imagen):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.imagen.fill(self.color_colision)
            otra_imagen.imagen.fill(otra_imagen.color_colision)
        else:
            self.imagen.fill(self.color)
            otra_imagen.imagen.fill(otra_imagen.color)
