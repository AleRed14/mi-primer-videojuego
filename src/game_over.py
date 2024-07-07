import pygame
from pygame.locals import *
from funciones import *
from settings import *
from texto import mostrar_texto

from archivos import *
# from main import main_menu

def game_over_screen(screen, score):
    # Fuente
    fuente = pygame.font.Font(None, FUENTE_GAME) # Fuente, tamaño
    
    name = input("Enter your initials: ")
    # Guardar el puntaje en el archivo
    puntaje = [new_puntaje(name, score)]
    append_archivo_csv("puntajes.csv", puntaje)
    is_runnig = True
    while is_runnig:

        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()
            if event.type == KEYDOWN:
                if event.type == K_SPACE:
                    is_runnig = False
                    from main import main_menu
                    main_menu()
        screen.fill(BLACK)
        mostrar_texto(screen,f"Score: {score}", fuente, MESSAGE_STAR_POS, WHITE)
        mostrar_texto(screen,f"SPACE PARA SALIR", fuente, SCREEN_CENTER_BOTTOM, WHITE)
        mostrar_texto(screen,f"GAME OVER", fuente, SCREEN_CENTER, WHITE, True)

        # Actualizar pantalla

        pygame.display.flip()

        



