import pygame

def crear_rect(imagen = None, left: int = 0, top: int = 0, ancho: int = 50, 
               largo: int = 50, color: tuple = (255, 255, 255), dir: int = 3,
               borde: int = 0, radio: int = -1) -> dict:
    if imagen:
      imagen = pygame.transform.scale(imagen, (ancho, largo))
    return {"rect": pygame.Rect(left,top,ancho,largo), "color": color, 
            "dir": dir, "borde": borde, "radio": radio, "img": imagen}

def crear_coin(coin_w: int = 25, coin_h: int = 25, left: int = 0,
               top: int = 0, color: tuple = (255, 255, 0), imagen = None):
    return crear_rect(imagen,left, top, coin_w, coin_h, color, 0, 0, 
                      coin_h // 2)