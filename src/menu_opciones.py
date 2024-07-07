import pygame
from pygame.locals import *
from colisiones import punto_en_rectangulo
from funciones import *
from settings import *
from texto import opcion_menu, mostrar_texto
from archivos import *
from imagenes import crear_fondo







def menu_opciones(screen, mouse_position ):
    
    volumenes = cargar_lista_json("volumenes.json")
    volumen_sonido = volumenes[0]["sonido"]
    volumen_musica = volumenes[0]["musica"]

    # Pantalla
    fondo_estadio = crear_fondo("fondo_estadio.jpg",SCREEN_SIZE)

    # Fuente
    fuente_titulo = pygame.font.Font(None, FUENTE_TITULO) # Fuente, tamaño
    fuente_opciones = pygame.font.Font(None, FUENTEO_PCIONES) # Fuente, tamaño

    # Sonido
    sonido_ambiente = pygame.mixer.Sound("./src/assets/sonidos/sonido_ambiente.mp3")
    volumen = cargar_lista_json("volumenes.json")

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
    
                    if punto_en_rectangulo(click_position, rect_menos_sonido_grande):
                        if volumen_sonido > 0:
                            volumen_sonido -= 1
                    if punto_en_rectangulo(click_position, rect_mas_sonido_grande):
                        if volumen_sonido < 10:
                            volumen_sonido += 1
                        
                    if punto_en_rectangulo(click_position, rect_menos_musica_grande):
                        if volumen_musica > 0:
                            volumen_musica -= 1
                        
                    if punto_en_rectangulo(click_position, rect_mas_musica_grande):
                        if volumen_musica < 10:
                            volumen_musica += 1
                    
                    if punto_en_rectangulo(click_position, rect_mas_guardar_grande):
                        crear_archivo_json("volumenes.json", 
                        [{"sonido":volumen_sonido, "musica": volumen_musica}])
                    
                    if punto_en_rectangulo(click_position, rect_salir_grande):
                        is_running = False

        sonido_ambiente.set_volume(TUPLE_VOLUMEN[volumen_sonido])
        pygame.mixer.music.set_volume(TUPLE_VOLUMEN[volumen_musica])

        
        # Actualizar pantalla

        screen.blit(fondo_estadio,ORIGIN)
        
        mostrar_texto(screen, "Opciones", fuente_titulo, TITULO_POS,
                    WHITE)
        mostrar_texto(screen, f"VOLUMEN SONIDO:", fuente_opciones,VOL_SON_POS, WHITE)
        mostrar_texto(screen, f"{volumen_sonido}", fuente_opciones,VOL_SON_NUM_POS, WHITE)
        mostrar_texto(screen, f"VOLUMEN MUSICA:", fuente_opciones,VOL_MUSIC_POS, WHITE)
        mostrar_texto(screen, f"{volumen_musica}", fuente_opciones,VOL_MUSIC_NUM_POS, WHITE)

        rect_menos_sonido_grande = opcion_menu(screen, "<", fuente_opciones,
                                        MENOS_SONIDO_POS, WHITE, mouse_position)
        
        rect_mas_sonido_grande = opcion_menu(screen, ">", fuente_opciones,
                                        MAS_SONIDO_POS, WHITE, mouse_position)
        
        rect_menos_musica_grande = opcion_menu(screen, "<", fuente_opciones,
                                        MENOS_MUSIC_POS, WHITE, mouse_position)
        
        rect_mas_musica_grande = opcion_menu(screen, ">", fuente_opciones,
                                        MAS_MUSIC_POS, WHITE, mouse_position)
        
        rect_mas_guardar_grande = opcion_menu(screen, "GUARDAR", fuente_opciones,
                                        GUARDAR_POS, WHITE, mouse_position)
        
        rect_salir_grande = opcion_menu(screen, "SALIR", fuente_opciones,
                                            SALIR_POS, WHITE, mouse_position)

        pygame.display.flip()