# Importamos
import pygame
from pygame.locals import *
from settings import *
from imagenes import crear_fondo
from funciones import salir_juego
from colisiones import punto_en_rectangulo
from texto import *
from juego import game_loop
from game_over import game_over_screen
from archivos import cargar_lista_json
from menu_opciones import menu_opciones
from menu_puntajes import menu_puntajes

# Iniciamos pygame
pygame.init()

# Pantalla
SCREEN = pygame.display.set_mode(SCREEN_SIZE) # Tamaño pantalla
pygame.display.set_caption("Primer juego") # Titulo en ventana
fondo_estadio = crear_fondo("fondo_estadio.jpg",SCREEN_SIZE)

# Fuente
fuente_titulo = pygame.font.Font(None, FUENTE_TITULO) # Fuente, tamaño
fuente_opciones = pygame.font.Font(None, FUENTEO_PCIONES) # Fuente, tamaño

# Sonido
volumen = cargar_lista_json("volumenes.json")
pygame.mixer.music.load("./src/assets/sonidos/Muchachos 8-bit.wav")
pygame.mixer.music.set_volume(TUPLE_VOLUMEN[volumen[0]["musica"]])
pygame.mixer.music.play(-1)

def main_menu():
    while True:

        # Analizar eventos

        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()
            if event.type == MOUSEMOTION:
                mouse_position = event.pos
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_position = event.pos
                    if punto_en_rectangulo(click_position, rect_jugar_grande):
                        print("JUGAR")
                        pygame.mixer.music.pause()
                        game_loop(SCREEN)
                        pygame.mixer.music.unpause()
                    if punto_en_rectangulo(click_position, rect_puntajes_grande):
                        print("PUNTAJES")
                        menu_puntajes(SCREEN, mouse_position)
                    if punto_en_rectangulo(click_position, rect_opciones_grande):
                        print("OPCIONES")
                        menu_opciones(SCREEN, mouse_position)
                    if punto_en_rectangulo(click_position, rect_salir_grande):
                        salir_juego()

        # sonido_ambiente.set_volume(TUPLE_VOLUMEN[volumen[0]["sonido"]])
        # pygame.mixer.music.set_volume(TUPLE_VOLUMEN[volumen[0]["musica"]])

        # Dibujar pantalla

        SCREEN.blit(fondo_estadio,ORIGIN)
        mostrar_texto(SCREEN, "A referee's day", fuente_titulo, TITULO_POS,
                   WHITE)
        
        rect_jugar_grande = opcion_menu(SCREEN, "JUGAR", fuente_opciones,
                                        JUGAR_POS, WHITE, mouse_position)

        rect_puntajes_grande = opcion_menu(SCREEN, "PUNTAJES", fuente_opciones,
                                           PUNTAJES_POS, WHITE, mouse_position)
        
        rect_opciones_grande = opcion_menu(SCREEN, "OPCIONES", fuente_opciones,
                                           OPCIONES_POS, WHITE, mouse_position)        
        
        rect_salir_grande = opcion_menu(SCREEN, "SALIR", fuente_opciones,
                                           SALIR_POS, WHITE, mouse_position)

        # Actualizar pantalla

        pygame.display.flip()

    # Finalizar

    salir_juego()
if __name__ == '__main__':
    main_menu()