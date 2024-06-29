import pygame
from settings import *

fondo_ruinas = pygame.transform.scale(
    pygame.image.load("./src/assets/fondos/fondo_ruinas.jpg"), SCREEN_SIZE)
fondo_casquillos = pygame.transform.scale(
    pygame.image.load("./src/assets/fondos/fondo_casquillos.jpg"), SCREEN_SIZE)
fondo_medallas = pygame.transform.scale(
    pygame.image.load("./src/assets/fondos/fondo_medallas.jpg"), SCREEN_SIZE)

