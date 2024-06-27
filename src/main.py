# Importamos
import pygame
from settings import *
from pygame.locals import *

# Iniciamos pygame
pygame.init()

# Pantalla

SCREEN = pygame.display.set_mode(SCREEN_SIZE) # Tamaño pantalla
pygame.display.set_caption("Primer juego") # Titulo en ventana
clock = pygame.time.Clock() 

is_running = True

while is_running:
    clock.tick(FPS)

    # Analizar eventos

    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False

    # Actualizar eventos

    # Dibujar pantalla

    # Actualizar pantalla

    pygame.display.flip()

# Finalizar

pygame.quit()