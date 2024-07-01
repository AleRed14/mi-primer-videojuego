# Ideas:
# - El juego va a tratar de (arbitro de futbol que sanciona jugadores? o el juego de stardew valley)
# - al perder, que haya una animacion, se espera 5 segundos y se pone la pantalla
# de game over, pidiendo que ingreses tu nombre con un maximo de tres digitos
# si entra dentro de los 5 maximos puntajes guardar en el archivo
# Agregar un boton que muestre las colisiones


# - Puntajes
# Mostrar los 5 mayores puntajes del juego
# se debe mostrar primero el nombre, depues el puntaje con un "pts"
# ver que otras cosas se pueden agregar
# - menu opciones
# opciones para subir y bajar el volumen de los sonidos y la musica
# ver si se puede tambien de la resolucion
# agregar opcion de guardar, avisar si los cambios no estan guardados


# Importamos
import pygame
from settings import *
from pygame.locals import *
from imagenes import *
from players import *
from text import *
from colisiones import *
from aleatorios import *

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

cant = 5
lista_puntajes = puntajes_aleatorios(cant)


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
                if menu == PR:
                    if punto_en_rectangulo(click_position,rect_jugar_grande):
                        print("JUGAR")
                        fondo = fondo_ruinas
                    if punto_en_rectangulo(click_position,rect_puntaje_grande):
                        fondo = fondo_medallas
                        menu = PU
                    if punto_en_rectangulo(click_position,rect_opciones_grande):
                        fondo = fondo_casquillos
                        menu = OP
                    if punto_en_rectangulo(click_position,rect_salir_grande):
                        is_running = False
                elif menu == PU:
                    if punto_en_rectangulo(click_position,rect_salir_grande):
                        menu = PR
                        fondo = fondo_ruinas
                elif menu == OP:
                    if punto_en_rectangulo(click_position,rect_salir_grande):
                        menu = PR
                        fondo = fondo_ruinas

                
        
                

    # Actualizar eventos

    

    # Dibujar pantalla

    SCREEN.blit(fondo,ORIGIN)
    
    if menu == PR:
        SCREEN.blit(texto_jugar, rect_jugar)
        SCREEN.blit(titulo, rect_titulo)
        SCREEN.blit(texto_puntaje, rect_puntajes)
        SCREEN.blit(texto_opciones, rect_opciones)
        SCREEN.blit(texto_salir, rect_salir)
        if punto_en_rectangulo(mouse_position,rect_jugar_grande):
            pygame.draw.rect(SCREEN,WHITE,rect_jugar_grande,10)
        if punto_en_rectangulo(mouse_position,rect_puntaje_grande):
            pygame.draw.rect(SCREEN,WHITE,rect_puntaje_grande,10)
        if punto_en_rectangulo(mouse_position,rect_opciones_grande):
            pygame.draw.rect(SCREEN,WHITE,rect_opciones_grande,10)
        if punto_en_rectangulo(mouse_position,rect_salir_grande):
            pygame.draw.rect(SCREEN,WHITE,rect_salir_grande,10)
    elif menu == PU:
        y_last = SCREEN_CENTER[1] - 100
        SCREEN.blit(texto_salir, rect_salir)
        if punto_en_rectangulo(mouse_position,rect_salir_grande):
            pygame.draw.rect(SCREEN,RED,rect_salir_grande,10)
        for puntaje in lista_puntajes:
            text_puntaje = fuente_opciones.render(puntaje,True,RED,WHITE)
            rect_puntaje = get_text_rect(text_puntaje,(SCREEN_CENTER[0], y_last))
            y_last += 50
            SCREEN.blit(text_puntaje, rect_puntaje)
    else:
        # Opciones con dos flechas para cambiar: volumen sonidos y volumen
        # musica
        SCREEN.blit(texto_salir, rect_salir)
        if punto_en_rectangulo(mouse_position,rect_salir_grande):
            pygame.draw.rect(SCREEN,RED,rect_salir_grande,10)

            

            

    # Actualizar pantalla

    pygame.display.flip()

# Finalizar

pygame.quit()