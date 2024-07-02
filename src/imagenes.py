import pygame

def crear_fondo(nombre_archivo: str, screen_size: tuple[0,0]):
    return pygame.transform.scale(
        pygame.image.load(f"./src/assets/imagenes/{nombre_archivo}"), screen_size)