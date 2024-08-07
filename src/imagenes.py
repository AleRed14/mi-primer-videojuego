import pygame
from pygame.locals import *

def crear_fondo(nombre_archivo: str, screen_size: tuple[0,0]):
    return pygame.transform.scale(
        pygame.image.load(f"./src/assets/imagenes/fondos/{nombre_archivo}"), screen_size)

def get_sprite(sprite_sheet, frame, move, left, top, width, heigth, scale = 1):
    imagen = pygame.Surface((width, heigth), SRCALPHA)
    imagen.blit(sprite_sheet.subsurface(frame, move, width, heigth), (0,0))
    imagen = pygame.transform.scale(imagen, (scale * width, scale * heigth))
    return imagen
# def get_sprite(sprite_sheet, frame, move, left, top, width, heigth, scale = 1):
#     imagen = pygame.Surface((width, heigth), SRCALPHA)
#     imagen.blit(sprite_sheet.subsurface(frame * width, move * heigth, width, heigth), (left,top))
#     imagen = pygame.transform.scale(imagen, (width, heigth))
#     return imagen
def get_image(sprite_sheet, left, top, width, heigth):
    imagen = pygame.Surface((width, heigth), SRCALPHA)
    imagen.blit(sprite_sheet, (left,top))
    imagen = pygame.transform.scale(imagen, (width, heigth))
    return imagen