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

def ordenar_listas_de_dicts(lista_dicts:list,target:str,asc:bool = True)->None:
    auxiliar = None
    tam = len(lista_dicts)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if (asc and lista_dicts[i][target] < lista_dicts[j][target]or
            (not asc and lista_dicts[i][target] > lista_dicts[j][target])):
                swap_lista(lista_dicts,i,j)

def swap_lista(lista:list, i:int, j:int)->None:
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar