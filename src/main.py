# Area de accion del jugador, poder lanzar tarjetas
# enemigos: hitbox, area de accion, que se vayan dsp accion
# sistema de vidas, pantalla de game over
# Guardar puntajes en archivo
# Que se pueda guardar las opciones en un archivo

# Importamos
import pygame
from settings import *
from pygame.locals import *
from funciones import *
from imagenes import *
from texto import *
from aleatorios import *
from random import randrange, randint

# Iniciamos pygame
pygame.init()

# Pantalla
SCREEN = pygame.display.set_mode(SCREEN_SIZE) # Tamaño pantalla
pygame.display.set_caption("Primer juego") # Titulo en ventana
fondo_estadio = crear_fondo("fondo_estadio.jpg",SCREEN_SIZE)
fondo_copas = crear_fondo("fondo_copas.jpg",SCREEN_SIZE)
fondo_copas1 = crear_fondo("fondo_copas1.jpg",SCREEN_SIZE)
fondo_cancha_horizontal = crear_fondo("cancha_horizontal.jpg",SCREEN_SIZE)
fondo_cancha_cam = crear_fondo("cancha_cam.jpg",SCREEN_SIZE)

referee = pygame.image.load(f"./src/assets/imagenes/sprites/referee.png")
jugadores_red = pygame.image.load(f"./src/assets/imagenes/sprites/red.png")
jugadores_blue = pygame.image.load(f"./src/assets/imagenes/sprites/boca.png")

# Fuente
fuente_titulo = pygame.font.Font(None, FUENTE_TITULO) # Fuente, tamaño
fuente_opciones = pygame.font.Font(None, FUENTEO_PCIONES) # Fuente, tamaño

# Tiempo
clock = pygame.time.Clock()
ultima_actualizacion = pygame.time.get_ticks()
frame_time = 200
TIMERMOVE = USEREVENT + 1
tiempo_de_espera = 1000

# Cargo sonido
sonido_ambiente = pygame.mixer.Sound("./src/assets/sonidos/sonido_ambiente.mp3")
pygame.mixer.music.load("./src/assets/sonidos/Muchachos 8-bit.wav")
pygame.mixer.music.play(-1)

# Inicializaciones
fondo = fondo_estadio
menu = MENU_PR
cant = 5
lista_puntajes = puntajes_aleatorios(cant)
player_w = 50
player_h = 50
mostrar_rectangulo = False

jugadores = []
lista_equipos = [jugadores_red, jugadores_blue]
cant_jugadores = 2

frame = 0
move = QUIETO
e_move = QUIETO


player = crear_bloque(referee.subsurface(frame * PLAYER_WIDTH, move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT),*SCREEN_CENTER,player_w,player_h, speed_x = 5)
for _ in range(cant_jugadores):
    jugadores.append(crear_jugador(lista_equipos[0].subsurface(
                    frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, PLAYER_WIDTH,
                    PLAYER_HEIGHT), randint(0, WIDTH
                    - PLAYER_WIDTH), randint(0, HEIGHT - PLAYER_HEIGHT), dir = TUPLE_DIR[randrange(len(TUPLE_DIR))],
                    speed_x = 3, speed_y = 3))
# enemie_v= pygame.transform.flip(jugadores[0]["img"], True, False)
    
is_running = True
while is_running:
    clock.tick(FPS)

    # Analizar eventos

    for event in pygame.event.get():
        if event.type == QUIT:
            salir_juego()
        if event.type == MOUSEMOTION:
            mouse_position = event.pos
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click_position = event.pos
                if menu == MENU_PR:
                    if punto_en_rectangulo(click_position, rect_jugar_grande):
                        print("JUGAR")
                        pygame.mixer.music.pause()
                        menu = MENU_JUGAR
                        fondo = fondo_cancha_horizontal
                        sonido_ambiente.play(-1)
                        pygame.time.set_timer(TIMERMOVE, tiempo_de_espera)
                    if punto_en_rectangulo(click_position, rect_puntajes_grande):
                        menu = MENU_PU
                        fondo = fondo_copas1
                    if punto_en_rectangulo(click_position, rect_opciones_grande):
                        menu = MENU_OP
                    if punto_en_rectangulo(click_position, rect_salir_grande):
                        salir_juego()
                elif menu == MENU_PU:
                    if punto_en_rectangulo(click_position, rect_salir_grande):
                        menu = MENU_PR
                elif menu == MENU_OP:
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

                    if punto_en_rectangulo(click_position, rect_salir_grande):
                        menu = MENU_PR
        if menu == MENU_JUGAR:
            
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_left = True
                    move_left_a = True
                    move_right = False
                    
                if event.key == K_RIGHT:
                    move_left_a = False
                    move_right = True
                    move_left = False
                    
                if event.key == K_UP:
                    move_up = True
                    move_down = False
                    
                if event.key == K_DOWN:
                    move_down = True
                    move_up = False
                    
                if event.key == K_y:
                    move = P_SACAR_AMARILLA
                if event.key == K_r:
                    move = P_SACAR_ROJA
                # if event.key == K_6:
                #     move = GAME_OVER
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False

            if event.type == TIMERMOVE:
                print("evento tiempo")
                mostrar_rectangulo = not mostrar_rectangulo
                # if mostrar_rectangulo:
                pygame.time.set_timer(TIMERMOVE, tiempo_de_espera)

    # Actualizar eventos
    if menu == MENU_JUGAR:    

        player_v= pygame.transform.flip(player["img"], True, False)
        
        

        if not (move_left and move_right and move_up and move_down) and move != 3 \
        and move != 4 and move != 6:
            move = QUIETO

        if move_left and player["rect"].left > 0:
            move = MOVE_LADO
            # Voltear la imagen horizontalmente
            if player["rect"].left - speed_player_x <= 0:
                player["rect"].left = 0
            else:
                player["rect"].left -= speed_player_x
        if move_right and player["rect"].right < WIDTH:
            move = MOVE_LADO
            if player["rect"].right + speed_player_x >= WIDTH:
                player["rect"].right = WIDTH
            else:
                player["rect"].right += speed_player_x
        if move_down and player["rect"].bottom < HEIGHT:
            move = MOVE_DOWN
            if player["rect"].bottom + speed_player_x >= HEIGHT:
                player["rect"].bottom = HEIGHT
            else:
                player["rect"].bottom += speed_player_x
        if move_up and player["rect"].top > 0:
            move = P_MOVE_UP
            if player["rect"].top - speed_player_x <= 0:
                player["rect"].top = 0
            else:
                player["rect"].top -= speed_player_x

        # player = crear_bloque(referee.subsurface(frame * PLAYER_WIDTH, move * PLAYER_HEIGHT, 
        #                 PLAYER_WIDTH, PLAYER_HEIGHT),player["rect"].left,player["rect"].top,player_w,player_h,radio = 2)
        player["img"] = referee.subsurface(frame * PLAYER_WIDTH, move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT)
        player["img"] = pygame.transform.scale(player["img"],(player_w,player_h))
        # for jugador in jugadores:
            
        
        

        sonido_ambiente.set_volume(lista_volumen[volumen_sonido])
        pygame.mixer.music.set_volume(lista_volumen[volumen_musica])

        current_time = pygame.time.get_ticks()


        
        
        if mostrar_rectangulo:
            # print("hola")
            for jugador in jugadores:
                print(jugador["dir"])
                if jugador["dir"] == U and jugador["rect"].top > 0:
                    e_move = MOVE_LADO
                    jugador["rect"].move_ip(0, - jugador["speed_y"])
                elif jugador["dir"] == D and jugador["rect"].bottom < HEIGHT:
                    e_move = MOVE_DOWN
                    jugador["rect"].move_ip(0, jugador["speed_y"])
                elif jugador["dir"] == R and jugador["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador["rect"].move_ip(jugador["speed_x"], 0)
                elif jugador["dir"] == L and jugador["rect"].left > 0:
                    e_move = MOVE_LADO
                    
                    jugador["rect"].move_ip(- jugador["speed_x"], 0)
                elif jugador["dir"] == UR and jugador["rect"].top > 0 and jugador["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador["rect"].move_ip(jugador["speed_x"], - jugador["speed_y"])
                elif jugador["dir"] == UL and jugador["rect"].top > 0 and jugador["rect"].left > 0:
                    e_move = MOVE_LADO
                    jugador["rect"].move_ip(- jugador["speed_x"], - jugador["speed_y"])
                elif jugador["dir"] == DR and jugador["rect"].bottom < HEIGHT and jugador["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador["rect"].move_ip(jugador["speed_x"], jugador["speed_y"])
                elif jugador["dir"] == DL and jugador["rect"].bottom < HEIGHT and jugador["rect"].left > 0:
                    e_move = MOVE_LADO
                    jugador["rect"].move_ip(- jugador["speed_x"], jugador["speed_y"])
                else:
                    e_move = QUIETO
                jugador["img"] = lista_equipos[0].subsurface(frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT)
                jugador["img"] = pygame.transform.scale(jugador["img"],(player_w,player_h))
        else:
            
            for jugador in jugadores:
                e_move = QUIETO
                jugador["img"] = lista_equipos[0].subsurface(frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT)
                jugador["img"] = pygame.transform.scale(jugador["img"],(player_w,player_h))
                jugador["dir"] = TUPLE_DIR[randrange(len(TUPLE_DIR))]
            
        if current_time - ultima_actualizacion >= frame_time:
            frame += 1
            if frame == 4 or move == 6:
                frame = 0
            ultima_actualizacion = current_time
    



    # Dibujar pantalla

    SCREEN.blit(fondo,ORIGIN)
    
    if menu == MENU_PR:
        mostrar_texto(SCREEN, "A referee's day", fuente_titulo, TITULO_POS,
                   WHITE)
        
        rect_jugar = mostrar_texto_con_rect(SCREEN, "JUGAR",
                                        fuente_opciones, JUGAR_POS, WHITE)
        rect_jugar_grande = agrandar_rect(rect_jugar)
        if punto_en_rectangulo(mouse_position, rect_jugar_grande):
            pygame.draw.rect(SCREEN, WHITE, rect_jugar_grande,5)

        rect_puntajes = mostrar_texto_con_rect(SCREEN, "PUNTAJES",
                                        fuente_opciones, PUNTAJES_POS, WHITE)
        rect_puntajes_grande = agrandar_rect(rect_puntajes)
        if punto_en_rectangulo(mouse_position, rect_puntajes_grande):
            pygame.draw.rect(SCREEN, WHITE, rect_puntajes_grande,5)

        rect_opciones = mostrar_texto_con_rect(SCREEN, "OPCIONES",
                                        fuente_opciones, OPCIONES_POS, WHITE)
        rect_opciones_grande = agrandar_rect(rect_opciones)
        if punto_en_rectangulo(mouse_position, rect_opciones_grande):
            pygame.draw.rect(SCREEN, WHITE, rect_opciones_grande,5)

    elif menu == MENU_PU:
        mostrar_texto(SCREEN, "Mejores puntajes", fuente_titulo, TITULO_POS,
                   WHITE)
        y_last = SCREEN_CENTER[1] - 100
        for puntaje in lista_puntajes:
            mostrar_texto(SCREEN, puntaje, fuente_opciones,(SCREEN_CENTER[0],
                            y_last), WHITE, color_fondo = BLACK)
            y_last += 50

    elif menu == MENU_OP:
        mostrar_texto(SCREEN, "Opciones", fuente_titulo, TITULO_POS,
                   WHITE)
        mostrar_texto(SCREEN, f"VOLUMEN SONIDO:", fuente_opciones,VOL_SON_POS, WHITE)
        mostrar_texto(SCREEN, f"{volumen_sonido}", fuente_opciones,VOL_SON_NUM_POS, WHITE)
        mostrar_texto(SCREEN, f"VOLUMEN MUSICA:", fuente_opciones,VOL_MUSIC_POS, WHITE)
        mostrar_texto(SCREEN, f"{volumen_musica}", fuente_opciones,VOL_MUSIC_NUM_POS, WHITE)

        rect_menos_sonido = mostrar_texto_con_rect(SCREEN, "<",
                                        fuente_opciones, MENOS_SONIDO_POS, WHITE)
        rect_menos_sonido_grande = agrandar_rect(rect_menos_sonido)
        if punto_en_rectangulo(mouse_position, rect_menos_sonido_grande):
            pygame.draw.rect(SCREEN, WHITE, rect_menos_sonido_grande,5)
        
        rect_mas_sonido = mostrar_texto_con_rect(SCREEN, ">",
                                        fuente_opciones, MAS_SONIDO_POS, WHITE)
        rect_mas_sonido_grande = agrandar_rect(rect_mas_sonido)
        if punto_en_rectangulo(mouse_position, rect_mas_sonido_grande):
            pygame.draw.rect(SCREEN, WHITE, rect_mas_sonido_grande,5)
        
        rect_menos_musica = mostrar_texto_con_rect(SCREEN, "<",
                                        fuente_opciones, MENOS_MUSIC_POS, WHITE)
        rect_menos_musica_grande = agrandar_rect(rect_menos_musica)
        if punto_en_rectangulo(mouse_position, rect_menos_musica_grande):
            pygame.draw.rect(SCREEN, WHITE, rect_menos_musica_grande,5)
        
        rect_mas_musica = mostrar_texto_con_rect(SCREEN, ">",
                                        fuente_opciones, MAS_MUSIC_POS, WHITE)
        rect_mas_musica_grande = agrandar_rect(rect_mas_musica)
        if punto_en_rectangulo(mouse_position, rect_mas_musica_grande):
            pygame.draw.rect(SCREEN, WHITE, rect_mas_musica_grande,5)

    else:
        for jugador in jugadores:
            SCREEN.blit(jugador["img"],jugador["rect"])
            # if jugador["dir"] == L or jugador["dir"] == UL or jugador["dir"] == DL:
            #     SCREEN.blit(enemie_v,jugador["rect"])
            # else:
            #     SCREEN.blit(jugador["img"],jugador["rect"])
        # pygame.draw.rect(SCREEN, player["color"], player["rect"],
        #                     player["borde"], player["radio"])
        if move_left_a:
            SCREEN.blit(player_v,player["rect"])
        else:
            SCREEN.blit(player["img"],player["rect"])
        
    if menu != MENU_JUGAR:
        rect_salir = mostrar_texto_con_rect(SCREEN, "SALIR",
                                        fuente_opciones, SALIR_POS, WHITE)
        rect_salir_grande = agrandar_rect(rect_salir)
        if punto_en_rectangulo(mouse_position, rect_salir_grande):
            pygame.draw.rect(SCREEN, WHITE, rect_salir_grande,5)

    # Actualizar pantalla

    pygame.display.flip()

# Finalizar

pygame.quit()