import pygame
from settings import *
from colisiones import punto_en_rectangulo

def mostrar_texto(superficie: pygame.Surface, texto: str, 
                  fuente: pygame.font.Font, posicion: tuple[int,int], 
                  color: tuple[int,int,int], flip: bool = False,
                  color_fondo: tuple[int,int,int] = None) -> None:
    sup_texto = fuente.render(texto, True, color, color_fondo) 
    rect_texto = sup_texto.get_rect(center = posicion)
    superficie.blit(sup_texto, rect_texto)
    if flip:
        pygame.display.flip()

def mostrar_texto_con_rect(superficie: pygame.Surface, texto: str, 
                  fuente: pygame.font.Font, posicion: tuple[int,int], 
                  color: tuple[int,int,int], flip: bool = False,
                  color_fondo: tuple[int,int,int] = None) -> None:
    sup_texto = fuente.render(texto, True, color, color_fondo) 
    rect_texto = sup_texto.get_rect(center = posicion)
    superficie.blit(sup_texto, rect_texto)
    if flip:
        pygame.display.flip()
    return rect_texto

def agrandar_rect(rect: pygame.Rect):
    rect = list(rect)
    rect[0], rect[1], rect[2],rect[3] = rect[0] - (rect[2] // 2), rect[1] - (rect[3] // 2), rect[2] * 2, rect[3] * 2
    return pygame.Rect(rect)

def opcion_menu(screen: pygame.Surface, texto:str, fuente: pygame.font.Font,
                posicion:tuple[int,int], color:tuple[int,int,int], 
                mouse_position:tuple[int,int]):
    rect_opcion = mostrar_texto_con_rect(screen, texto,
                                        fuente, posicion, WHITE, False)
    rect_opcion_grande = agrandar_rect(rect_opcion)
    if punto_en_rectangulo(mouse_position, rect_opcion_grande):
        pygame.draw.rect(screen, color, rect_opcion_grande,5)
    #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    # else:
    #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    return rect_opcion_grande