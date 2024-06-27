from creacion import *
from random import randrange,randint
def get_color(lista):
    return lista[randrange(len(lista))]

def get_new_color():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r,g,b)

def rect_aleatorio1(width:int,height:int,max:int):
    ancho = randint(0,max)
    largo = randint(0,max)
    dir = (1,3,7,9)
    
    return crear_rect(None,randint(0, width - ancho), randint(0, height - largo), 
                    ancho,largo, get_new_color(), dir[randrange(len(dir))],
                    randrange(31), randint(-1, 25))

def rect_aleatorio(width:int, height:int, max:int):
    ancho = randint(0,max)
    largo = randint(0,max)
    dir = (1,3,7,9)
    return crear_rect(None,randint(0, width - ancho), randint(0, height - largo),
                    ancho, largo, get_new_color(), dir[randrange(len(dir))])
