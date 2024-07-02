import pygame
from pygame.locals import *
from colisiones import *
def salir_juego():
    pygame.quit()
    exit()

def wait_user(tecla:int):
    continuar = True
    while continuar:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()
            if event.type == KEYDOWN:
                if event.key == tecla:
                    continuar = False

def wait_user_click(rect: pygame.Rect):
    continuar = True
    while continuar:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if punto_en_rectangulo(event.pos,rect):
                        continuar = False