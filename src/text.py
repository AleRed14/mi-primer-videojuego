import pygame
from settings import *
pygame.init()

fuente_titulo = pygame.font.Font(None, FUENTETITULO) # Fuente, tamaño
fuente_opciones = pygame.font.Font(None, FUENTEOPCIONES) # Fuente, tamaño

titulo = fuente_titulo.render("Titulo del juego", True, WHITE)

texto_jugar = fuente_opciones.render("JUGAR", True, WHITE)
texto_opciones = fuente_opciones.render("OPCIONES", True, WHITE)
texto_puntaje = fuente_opciones.render("PUNTAJES", True, WHITE)
texto_salir = fuente_opciones.render("SALIR", True, WHITE)

def get_text_rect(text = None, pos:tuple = (0,0)):
    rect_text = text.get_rect()
    rect_text.center = pos
    return rect_text

def agrandar_rect(rect):
    rect = list(rect)
    rect[0], rect[1], rect[2],rect[3] = rect[0] - (rect[2] // 2), rect[1] - (rect[3] // 2), rect[2] * 2, rect[3] * 2
    return pygame.Rect(rect)

rect_titulo = get_text_rect(titulo, (SCREEN_CENTER_UP[0],SCREEN_CENTER_UP[1]-50))

rect_jugar = get_text_rect(texto_jugar,(SCREEN_CENTER[0],SCREEN_CENTER[1]-50))
rect_jugar_grande = agrandar_rect(rect_jugar)

rect_puntajes = get_text_rect(texto_puntaje,(SCREEN_CENTER[0],SCREEN_CENTER[1]+25))
rect_puntaje_grande = agrandar_rect(rect_puntajes)

rect_opciones = get_text_rect(texto_opciones,(SCREEN_CENTER[0],SCREEN_CENTER[1]+100))
rect_opciones_grande = agrandar_rect(rect_opciones)

rect_salir = get_text_rect(texto_salir,(SCREEN_CENTER_BOTTOM[0],SCREEN_CENTER_BOTTOM[1]+25))
rect_salir_grande = agrandar_rect(rect_salir)

