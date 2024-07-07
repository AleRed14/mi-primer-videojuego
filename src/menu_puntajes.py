import pygame
from pygame.locals import *
from funciones import salir_juego, ordenar_listas_de_dicts
from colisiones import punto_en_rectangulo
from texto import *
from archivos import cargar_lista_csv
from imagenes import crear_fondo
from settings import *


def menu_puntajes(screen, mouse_position):

    fondo_copas1 = crear_fondo("fondo_copas1.jpg",SCREEN_SIZE)

    # Fuente
    fuente_titulo = pygame.font.Font(None, FUENTE_TITULO) # Fuente, tamaño
    fuente_opciones = pygame.font.Font(None, FUENTEO_PCIONES) # Fuente, tamaño

    lista_puntajes = cargar_lista_csv("puntajes.csv")
    ordenar_listas_de_dicts(lista_puntajes,"score")

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()
            if event.type == MOUSEMOTION:
                mouse_position = event.pos
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_position = event.pos
                    if punto_en_rectangulo(click_position, rect_salir_grande):
                        is_running = False


        # Actualizar pantalla

        screen.blit(fondo_copas1,ORIGIN)
        mostrar_texto(screen, "Mejores puntajes", fuente_titulo, TITULO_POS,
                   WHITE)
        y_last = SCREEN_CENTER[1] - 100
        for i in range(5):
            mostrar_texto(screen, f"{lista_puntajes[i]["nombre"][:3]}:    {lista_puntajes[i]["score"]} PTS", fuente_opciones,(SCREEN_CENTER[0],
                            y_last), WHITE, color_fondo = BLACK)
            y_last += 50

        rect_salir_grande = opcion_menu(screen, "SALIR", fuente_opciones,
                                            SALIR_POS, WHITE, mouse_position)

        # Actualizar pantalla

        pygame.display.flip()




