import pygame
from settings import *

def crear_bloque(imagen: pygame.Surface = None,left:int = 0, top:int = 0, ancho:int = 50, largo:int = 50, 
             color:tuple[int,int,int] = (255, 255, 255), dir:int = 3, borde:int = 0, 
             radio:int = -1, speed_x: int = 1, speed_y: int = 1,
             ) -> dict:
    if imagen:
      imagen = pygame.transform.scale(imagen,(ancho,largo))
    return {"rect": pygame.Rect(left,top,ancho,largo), "color": color, 
            "dir": dir, "borde": borde, "radio": radio, "img": imagen,
            "speed_x": speed_x, "speed_y": speed_y}

def crear_tarjeta(posicion: tuple[int,int], color:tuple[int,int,int] = RED, speed: int = 5):
   r = pygame.Rect(0,0, LASER_WIDTH, LASER_HEIGHT)
   r.midbottom = posicion
   return {"rect": r, "color": color, "speed": speed}

def crear_jugador(imagen: pygame.Surface, left:int = 0, top:int = 0, ancho:int
                   = 50, largo:int = 50, color_tarjeta: tuple[int,int,int] = 
                   YELLOW, dir:int = 0, speed_x:int = 1, speed_y:int = 1):
   return crear_bloque(imagen, left, top, ancho, largo, color_tarjeta, dir,
                       speed_x = speed_x, speed_y = speed_y)