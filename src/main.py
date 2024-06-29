# Importamos
import pygame
from settings import *
from pygame.locals import *
from imagenes import *
from players import *
from text import *
from colisiones import *

# Iniciamos pygame
pygame.init()

# Pantalla
SCREEN = pygame.display.set_mode(SCREEN_SIZE) # Tamaño pantalla
pygame.display.set_caption("Primer juego") # Titulo en ventana

# Tiempo
clock = pygame.time.Clock()

# inicializaciones
mouse_position = (0,0)

PR = "A"
PU = "B"
OP = "C"


fondo = fondo_ruinas
menu = PR

is_running = True

while is_running:
    clock.tick(FPS)

    # Analizar eventos

    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        if event.type == MOUSEMOTION:
            mouse_position = event.pos
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click_position = event.pos
                if punto_en_rectangulo(click_position,rect_jugar_grande):
                    print("JUGAR")
                    fondo = fondo_ruinas
                if punto_en_rectangulo(click_position,rect_puntaje_grande):
                    fondo = fondo_medallas
                    menu = PU
                if punto_en_rectangulo(click_position,rect_opciones_grande):
                    fondo = fondo_casquillos
                    menu = OP
                if menu == PR and punto_en_rectangulo(click_position,rect_salir_grande):
                   is_running = False
                
        
                

    # Actualizar eventos

    

    # Dibujar pantalla

    SCREEN.blit(fondo,ORIGIN)
    if punto_en_rectangulo(mouse_position,rect_jugar_grande):
        pygame.draw.rect(SCREEN,WHITE,rect_jugar_grande,10)
    if punto_en_rectangulo(mouse_position,rect_puntaje_grande):
        pygame.draw.rect(SCREEN,WHITE,rect_puntaje_grande,10)
    if punto_en_rectangulo(mouse_position,rect_opciones_grande):
        pygame.draw.rect(SCREEN,WHITE,rect_opciones_grande,10)
    if punto_en_rectangulo(mouse_position,rect_salir_grande):
        pygame.draw.rect(SCREEN,WHITE,rect_salir_grande,10)
    SCREEN.blit(texto_jugar, rect_jugar)
    SCREEN.blit(titulo, rect_titulo)
    SCREEN.blit(texto_salir, rect_salir)
    SCREEN.blit(texto_puntaje, rect_puntajes)
    SCREEN.blit(texto_opciones, rect_opciones)

    # Actualizar pantalla

    pygame.display.flip()

# Finalizar

pygame.quit()