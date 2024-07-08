import pygame
from pygame.locals import *
from funciones import *
from creacion import *
from random import randint, randrange
from colisiones import *
from imagenes import crear_fondo
from texto import mostrar_texto
from game_over import game_over_screen
from archivos import cargar_lista_json

# Imagenes
fondo_cancha_horizontal = crear_fondo("cancha_horizontal.jpg",SCREEN_SIZE)
# Sprites
referee = pygame.image.load(f"./src/assets/imagenes/sprites/referee.png")
sprite_jugador_red = pygame.image.load(f"./src/assets/imagenes/sprites/red.png")
sprite_jugador_blue = pygame.image.load(f"./src/assets/imagenes/sprites/boca.png")
imagen_cara_enojada = pygame.image.load(f"./src/assets/imagenes/cara_enojada.png")
imagen_cara_enojada = pygame.transform.scale(imagen_cara_enojada, (LIVE_WIDTH, LIVE_HEIGHT))
imagen_speed = pygame.image.load(f"./src/assets/imagenes/speed.png")
imagen_speed = pygame.transform.scale(imagen_speed, (LIVE_WIDTH, LIVE_HEIGHT))
imagen_tarjetas = pygame.image.load(f"./src/assets/imagenes/tarjetas.png")
imagen_tarjetas = pygame.transform.scale(imagen_tarjetas, (LIVE_WIDTH, LIVE_HEIGHT))





def game_loop(screen):

    # Fuente
    
    fuente = pygame.font.Font(None, FUENTE_GAME) # Fuente, tamaño

    # Tiempo
    clock = pygame.time.Clock()
    ultima_actualizacion = pygame.time.get_ticks()
    frame_time = 200
    
    # Inicializaciones
    # Sonido
    sonido_ambiente = pygame.mixer.Sound("./src/assets/sonidos/sonido_ambiente.mp3")
    sonido_silbato = pygame.mixer.Sound("./src/assets/sonidos/silbato.mp3")
    sonido_abucheo = pygame.mixer.Sound("./src/assets/sonidos/abucheo.mp3")
    volumenes = cargar_lista_json("volumenes.json")
    volumen_sonido = volumenes[0]["sonido"]
    sonido_ambiente.set_volume(TUPLE_VOLUMEN[volumen_sonido])
    sonido_silbato.set_volume(TUPLE_VOLUMEN[volumen_sonido])
    sonido_abucheo.set_volume(TUPLE_VOLUMEN[volumen_sonido])
    playing_sound = True

    sonido_ambiente.play(-1)
    
    # Eventos
    TIMERMOVE = USEREVENT + 1
    GAMETIMEOUT = USEREVENT + 2
    POWERUPTIME = USEREVENT + 3
    POWERUPTIMER = USEREVENT + 3
    tiempo_de_espera = 1000
    tiempo_de_power_up = 5000
    pygame.time.set_timer(TIMERMOVE, tiempo_de_espera)
    pygame.time.set_timer(GAMETIMEOUT, 45000)
    pygame.time.set_timer(POWERUPTIME, tiempo_de_power_up)
    bandera_movimiento = False
    bandera_power_up_pantalla = False
    power_up = None

    CARD_SPEED = 5
    vida_x = 50
    vida_y = 50

    # Players
    hitbox = False
    player_w = 50
    player_h = 50
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    move_left_a = False
    speed_player_x = 1
    speed_player_y = 1
    

    # Player
    score = 0
    frame = 0
    move = QUIETO
    TUPLA_COLOR_TARJETA = (YELLOW,RED)
    tarjeta = None
    pos_tarjeta_sacada = None
    color_tarjeta = YELLOW
    player = crear_bloque(referee.subsurface(frame * PLAYER_WIDTH, move *
                                             PLAYER_HEIGHT, PLAYER_WIDTH,
                                             PLAYER_HEIGHT), *SCREEN_CENTER,
                                             player_w, player_h, borde = 3,
                                             speed_x = speed_player_x, speed_y
                                             = speed_player_y)

    # Enemigos

    e_move = QUIETO
    enojo_hinchada = 0
    cant_jugadores_x_equipo = 1
    lista_enojo_pos = []
    jugadores_red = []
    jugadores_blue = []
    tarjeta_jug = None
    sprite_r = sprite_jugador_red.subsurface(frame *
                        PLAYER_WIDTH, e_move * PLAYER_HEIGHT, PLAYER_WIDTH,
                        PLAYER_HEIGHT)
    sprite_b = sprite_jugador_blue.subsurface(frame *
                        PLAYER_WIDTH, e_move * PLAYER_HEIGHT, PLAYER_WIDTH,
                        PLAYER_HEIGHT)
    for _ in range(cant_jugadores_x_equipo):
        left = randint(0, WIDTH - PLAYER_WIDTH)
        top = randint(0, HEIGHT - PLAYER_HEIGHT)
        color_tarjeta = TUPLA_COLOR_TARJETA[randrange(len(TUPLA_COLOR_TARJETA))]
        dir = TUPLE_DIR[randrange(len(TUPLE_DIR))]

        jugadores_red.append(crear_jugador(sprite_r, left, 
                        top, color_tarjeta = color_tarjeta, dir = dir,
                        speed_x = speed_player_x, speed_y = speed_player_y))
        
        left = randint(0, WIDTH - PLAYER_WIDTH)
        top = randint(0, HEIGHT - PLAYER_HEIGHT)
        color_tarjeta = TUPLA_COLOR_TARJETA[randrange(len(TUPLA_COLOR_TARJETA))]
        dir = TUPLE_DIR[randrange(len(TUPLE_DIR))]

        jugadores_blue.append(crear_jugador(sprite_b, left, 
                        top, color_tarjeta = color_tarjeta, dir = dir,
                        speed_x = speed_player_x, speed_y = speed_player_y))

    is_running = True
    while is_running:
        clock.tick(FPS)

        # Analizar eventos

        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()
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
                    
                if event.key == K_KP4:
                    sonido_silbato.play()
                    if not tarjeta:
                        tarjeta = crear_tarjeta(player["rect"].midleft, color_tarjeta, CARD_SPEED)
                        tarjeta_dir = L
                    
                if event.key == K_KP6:
                    sonido_silbato.play()
                    if not tarjeta:
                        tarjeta = crear_tarjeta(player["rect"].midright, color_tarjeta, CARD_SPEED)
                        tarjeta_dir = R
                    
                if event.key == K_KP8:
                    sonido_silbato.play()
                    if not tarjeta:
                        tarjeta = crear_tarjeta(player["rect"].midtop, color_tarjeta, CARD_SPEED)
                        tarjeta_dir = U
                    
                if event.key == K_KP2:
                    sonido_silbato.play()
                    if not tarjeta:
                        tarjeta = crear_tarjeta(player["rect"].midbottom, color_tarjeta, CARD_SPEED)
                        tarjeta_dir = D

                if event.key == K_KP5:
                    sonido_silbato.play()
                    pos_tarjeta_sacada = player["rect"]
                    # print(pos_tarjeta_sacada)
                    if color_tarjeta == YELLOW:
                        move = P_SACAR_AMARILLA
                    else:
                        move = P_SACAR_ROJA
                    
                if event.key == K_y:
                    color_tarjeta = YELLOW
                if event.key == K_h:
                    if hitbox:
                        hitbox = False
                    else:
                        hitbox = True
                if event.key == K_r:
                    color_tarjeta = RED
                if event.key == K_m:
                    if playing_sound:
                        sonido_ambiente.stop()
                        playing_sound = False
                    else:
                        sonido_ambiente.play(-1)
                        playing_sound = True
                if event.key == K_p:
                    mostrar_texto(SCREEN,"Pausa", fuente, MESSAGE_STAR_POS, RED, True)
                    pygame.mixer.music.pause()
                    wait_user(K_p)
                    move_left = False
                    move_right = False
                    move_up = False
                    move_down = False
                    if playing_sound:
                        sonido_ambiente.play(-1)
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
                bandera_movimiento = not bandera_movimiento
                pygame.time.set_timer(TIMERMOVE, tiempo_de_espera)
            if event.type == POWERUPTIME:
                bandera_power_up_pantalla = not bandera_movimiento
                pygame.time.set_timer(POWERUPTIME, tiempo_de_power_up)
            if event.type == POWERUPTIMER:
                player["speed_x"] = speed_player_x
                player["speed_y"] = speed_player_y
                
                # bandera_power_up_pantalla = not bandera_power_up_pantalla

            if event.type == GAMETIMEOUT or enojo_hinchada == 3:
                move = P_GAME_OVER
                is_running = False


        # Actualizar eventos

        player_v= pygame.transform.flip(player["img"], True, False)
        
        
        
        
        if not (move_left and move_right and move_up and move_down) and move != 3 \
        and move != 4 and move != 6:
            move = QUIETO

        if move_left and player["rect"].left > 0:
            move = MOVE_LADO
            if player["rect"].left - player["speed_x"] <= 0:
                player["rect"].left = 0
            else:
                player["rect"].left -= player["speed_x"]
        if move_right and player["rect"].right < WIDTH:
            move = MOVE_LADO
            if player["rect"].right + player["speed_x"] >= WIDTH:
                player["rect"].right = WIDTH
            else:
                player["rect"].right += player["speed_x"]
        if move_down and player["rect"].bottom < HEIGHT:
            move = MOVE_DOWN
            if player["rect"].bottom + player["speed_y"] >= HEIGHT:
                player["rect"].bottom = HEIGHT
            else:
                player["rect"].bottom += player["speed_y"]
        if move_up and player["rect"].top > 0:
            move = P_MOVE_UP
            if player["rect"].top - player["speed_y"] <= 0:
                player["rect"].top = 0
            else:
                player["rect"].top -= player["speed_y"]

        if tarjeta:
            if tarjeta_dir == U:
                tarjeta["rect"].move_ip(0, - tarjeta["speed"])
                if tarjeta["rect"].bottom < 0:
                    tarjeta = None
            if tarjeta_dir == D:
                tarjeta["rect"].move_ip(0, + tarjeta["speed"])
                if tarjeta["rect"].top > HEIGHT:
                    tarjeta = None
            if tarjeta_dir == R:
                tarjeta["rect"].move_ip(tarjeta["speed"], 0)
                if tarjeta["rect"].right > WIDTH:
                    tarjeta = None
            if tarjeta_dir == L:
                tarjeta["rect"].move_ip(- tarjeta["speed"], 0) 
                if tarjeta["rect"].left < 0:
                    tarjeta = None

        for jugador_red in jugadores_red[:]:
            if len(jugadores_red) > 0:
                if tarjeta:
                    if detectar_colision(tarjeta["rect"], jugador_red["rect"]):
                        if color_tarjeta == jugador_red["color"]:
                            tarjeta = None
                            score += 1
                            jugadores_red.remove(jugador_red)
                        else:
                            sonido_abucheo.play()
                            tarjeta = None
                            enojo_hinchada += 1
                            lista_enojo_pos.append((vida_x,vida_y))
                            vida_x += 50
                if pos_tarjeta_sacada:
                    if colision_circulos(pos_tarjeta_sacada, jugador_red["rect"]):
                        if color_tarjeta == jugador_red["color"]:
                            score += 1
                            jugadores_red.remove(jugador_red)
                            pos_tarjeta_sacada = None
                        else:
                            sonido_abucheo.play()
                            pos_tarjeta_sacada = None
                            enojo_hinchada += 1
                            lista_enojo_pos.append((vida_x,vida_y))
                            vida_x += 50
                    
        
        for jugador_blue in jugadores_blue[:]:
            if len(jugadores_blue) > 0:
                if tarjeta:
                    if detectar_colision(tarjeta["rect"], jugador_blue["rect"]):
                        if color_tarjeta == jugador_blue["color"]:
                            tarjeta = None
                            score += 1
                            jugadores_blue.remove(jugador_blue)
                        else:
                            sonido_abucheo.play()
                            tarjeta = None
                            enojo_hinchada += 1
                            lista_enojo_pos.append((vida_x,vida_y))
                            vida_x += 50
                if pos_tarjeta_sacada:
                    if colision_circulos(pos_tarjeta_sacada, jugador_blue["rect"]):
                        if color_tarjeta == jugador_blue["color"]:
                            score += 1
                            jugadores_blue.remove(jugador_blue)
                            pos_tarjeta_sacada = None
                        else:
                            sonido_abucheo.play()
                            pos_tarjeta_sacada = None
                            enojo_hinchada += 1
                            lista_enojo_pos.append((vida_x,vida_y))
                            vida_x += 50
                    
        pos_tarjeta_sacada = None

        if power_up:
            if detectar_colision_circulo_rect(player["rect"],power_up["rect"]):
                print("power")
                if name_pw == "speed":
                    player["speed_x"] = 3
                    player["speed_y"] = 3
                    power_up = None
                    pygame.time.set_timer(POWERUPTIMER, tiempo_de_power_up)
                else:
                    power_up = None
                    score += len(jugadores_red) + len(jugadores_blue)
                    jugadores_red = []
                    jugadores_blue = []


        if len(jugadores_red) == 0 and len(jugadores_blue) == 0:
            cant_jugadores_x_equipo += 1
            for _ in range(cant_jugadores_x_equipo):
                jugadores_red.append(crear_jugador(sprite_jugador_red.subsurface(
                frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, PLAYER_WIDTH,
                PLAYER_HEIGHT), randint(0, WIDTH
                - PLAYER_WIDTH), randint(0, HEIGHT - PLAYER_HEIGHT), 
                color_tarjeta = TUPLA_COLOR_TARJETA[randrange(len(
                    TUPLA_COLOR_TARJETA))], dir = TUPLE_DIR[randrange(len(
                        TUPLE_DIR))], speed_x = speed_player_x, speed_y = speed_player_y))
                
                jugadores_blue.append(crear_jugador(sprite_jugador_blue.subsurface(
                frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, PLAYER_WIDTH,
                PLAYER_HEIGHT), randint(0, WIDTH
                - PLAYER_WIDTH), randint(0, HEIGHT - PLAYER_HEIGHT), 
                color_tarjeta = TUPLA_COLOR_TARJETA[randrange(len(
                    TUPLA_COLOR_TARJETA))], dir = TUPLE_DIR[randrange(len(
                        TUPLE_DIR))], speed_x = speed_player_x, speed_y = speed_player_y))
        
        player["img"] = referee.subsurface(frame * PLAYER_WIDTH, move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT)
        player["img"] = pygame.transform.scale(player["img"],(player_w,player_h))  

        current_time = pygame.time.get_ticks()

        if bandera_movimiento:
            # print("hola")
            for jugador_red in jugadores_red:
                # print(jugador["dir"])
                if jugador_red["dir"] == U and jugador_red["rect"].top > 0 + PLAYER_HEIGHT:
                    e_move = MOVE_LADO
                    jugador_red["rect"].move_ip(0, - jugador_red["speed_y"])
                elif jugador_red["dir"] == D and jugador_red["rect"].bottom < HEIGHT:
                    e_move = MOVE_DOWN
                    jugador_red["rect"].move_ip(0, jugador_red["speed_y"])
                elif jugador_red["dir"] == R and jugador_red["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador_red["rect"].move_ip(jugador_red["speed_x"], 0)
                elif jugador_red["dir"] == L and jugador_red["rect"].left > 0:
                    e_move = MOVE_LADO
                    
                    jugador_red["rect"].move_ip(- jugador_red["speed_x"], 0)
                elif jugador_red["dir"] == UR and jugador_red["rect"].top > 0 + PLAYER_HEIGHT and jugador_red["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador_red["rect"].move_ip(jugador_red["speed_x"], - jugador_red["speed_y"])
                elif jugador_red["dir"] == UL and jugador_red["rect"].top > 0 + PLAYER_HEIGHT and jugador_red["rect"].left > 0:
                    e_move = MOVE_LADO
                    jugador_red["rect"].move_ip(- jugador_red["speed_x"], - jugador_red["speed_y"])
                elif jugador_red["dir"] == DR and jugador_red["rect"].bottom < HEIGHT and jugador_red["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador_red["rect"].move_ip(jugador_red["speed_x"], jugador_red["speed_y"])
                elif jugador_red["dir"] == DL and jugador_red["rect"].bottom < HEIGHT and jugador_red["rect"].left > 0:
                    e_move = MOVE_LADO
                    jugador_red["rect"].move_ip(- jugador_red["speed_x"], jugador_red["speed_y"])
                else:
                    e_move = QUIETO
                jugador_red["img"] = sprite_jugador_red.subsurface(frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT)
                jugador_red["img"] = pygame.transform.scale(jugador_red["img"],(player_w,player_h))
            for jugador_blue in jugadores_blue:
                # print(jugador["dir"])
                if jugador_blue["dir"] == U and jugador_blue["rect"].top > 0 + PLAYER_HEIGHT:
                    e_move = MOVE_LADO
                    jugador_blue["rect"].move_ip(0, - jugador_blue["speed_y"])
                elif jugador_blue["dir"] == D and jugador_blue["rect"].bottom < HEIGHT:
                    e_move = MOVE_DOWN
                    jugador_blue["rect"].move_ip(0, jugador_blue["speed_y"])
                elif jugador_blue["dir"] == R and jugador_blue["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador_blue["rect"].move_ip(jugador_blue["speed_x"], 0)
                elif jugador_blue["dir"] == L and jugador_blue["rect"].left > 0:
                    e_move = MOVE_LADO
                    
                    jugador_blue["rect"].move_ip(- jugador_blue["speed_x"], 0)
                elif jugador_blue["dir"] == UR and jugador_blue["rect"].top > 0 + PLAYER_HEIGHT and jugador_blue["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador_blue["rect"].move_ip(jugador_blue["speed_x"], - jugador_blue["speed_y"])
                elif jugador_blue["dir"] == UL and jugador_blue["rect"].top > 0 + PLAYER_HEIGHT and jugador_blue["rect"].left > 0:
                    e_move = MOVE_LADO
                    jugador_blue["rect"].move_ip(- jugador_blue["speed_x"], - jugador_blue["speed_y"])
                elif jugador_blue["dir"] == DR and jugador_blue["rect"].bottom < HEIGHT and jugador_blue["rect"].right < WIDTH:
                    e_move = MOVE_LADO
                    jugador_blue["rect"].move_ip(jugador_blue["speed_x"], jugador_blue["speed_y"])
                elif jugador_blue["dir"] == DL and jugador_blue["rect"].bottom < HEIGHT and jugador_blue["rect"].left > 0:
                    e_move = MOVE_LADO
                    jugador_blue["rect"].move_ip(- jugador_blue["speed_x"], jugador_blue["speed_y"])
                else:
                    e_move = QUIETO
                jugador_blue["img"] = sprite_jugador_blue.subsurface(frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT)
                jugador_blue["img"] = pygame.transform.scale(jugador_blue["img"],(player_w,player_h))
        else:
            
            for jugador_red in jugadores_red:
                e_move = QUIETO
                jugador_red["img"] = sprite_jugador_red.subsurface(frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT)
                jugador_red["img"] = pygame.transform.scale(jugador_red["img"],(player_w,player_h))
                jugador_red["dir"] = TUPLE_DIR[randrange(len(TUPLE_DIR))]
            for jugador_blue in jugadores_blue:
                e_move = QUIETO
                jugador_blue["img"] = sprite_jugador_blue.subsurface(frame * PLAYER_WIDTH, e_move * PLAYER_HEIGHT, 
                PLAYER_WIDTH, PLAYER_HEIGHT)
                jugador_blue["img"] = pygame.transform.scale(jugador_blue["img"],(player_w,player_h))
                jugador_blue["dir"] = TUPLE_DIR[randrange(len(TUPLE_DIR))]

        if bandera_power_up_pantalla:
            bandera_power_up_pantalla = False
            name_pw = TUPLA_POWERUP[randrange(len(TUPLA_POWERUP))]
            # name_pw = "all out"
            left = randint(0, WIDTH - PLAYER_WIDTH)
            top = randint(0, HEIGHT - PLAYER_HEIGHT)
            if name_pw == "speed":
                power_up = crear_bloque(imagen_speed, left, top, LIVE_WIDTH,
                                        LIVE_HEIGHT, borde = 3, radio = 
                                        LIVE_WIDTH // 2)
            else:
                power_up = crear_bloque(imagen_tarjetas, left, top, LIVE_WIDTH - 15 ,
                                        LIVE_HEIGHT - 15, borde = 3)

        
            
        if current_time - ultima_actualizacion >= frame_time:
            frame += 1
            if frame == 4 or move == P_GAME_OVER:
                frame = 0
            ultima_actualizacion = current_time
        
        # Dibujar pantalla

        screen.blit(fondo_cancha_horizontal,ORIGIN)
        
        mostrar_texto(SCREEN, f"{pygame.time.get_ticks()//1000}.{str(pygame.time.get_ticks())[-3:]}",
                    fuente, TIMER_POS, WHITE, color_fondo = BLACK)
        mostrar_texto(screen, f"Score: {score}", fuente, SCORE_POS, WHITE, color_fondo= BLACK)
        if not playing_sound:
            mostrar_texto(SCREEN,"mute", fuente, MUTE_POS, RED)
        for pos in lista_enojo_pos:
            screen.blit(imagen_cara_enojada,pos)
        if tarjeta:
            pygame.draw.rect(screen, tarjeta["color"], tarjeta["rect"])
        for jugador_red in jugadores_red:
            if hitbox:
                pygame.draw.rect(screen, jugador_red["color"], jugador_red["rect"],
                                    jugador_red["borde"], jugador_red["radio"])
                pygame.draw.circle(screen,WHITE,jugador_red["rect"].center,player_w//2,3)
            screen.blit(jugador_red["img"],jugador_red["rect"])
            tarjeta_jug = crear_tarjeta(jugador_red["rect"].midtop, 
                            jugador_red["color"])
            if jugador_red["color"] != WHITE:
                pygame.draw.rect(screen, tarjeta_jug["color"], tarjeta_jug["rect"])
        for jugador_blue in jugadores_blue:
            if hitbox:
                pygame.draw.rect(screen, jugador_blue["color"], jugador_blue["rect"],
                                    jugador_blue["borde"], jugador_blue["radio"])
                pygame.draw.circle(screen,WHITE,jugador_blue["rect"].center,player_w//2,3)
            screen.blit(jugador_blue["img"],jugador_blue["rect"])
            tarjeta_jug = crear_tarjeta(jugador_blue["rect"].midtop, 
                            jugador_blue["color"])
            # if jugador_blue["color"] != WHITE:
            pygame.draw.rect(screen, tarjeta_jug["color"], tarjeta_jug["rect"])

            pygame.draw.circle(screen,WHITE,player["rect"].center,player_w//2,3)
        # midbottom
        if move_left_a:
            screen.blit(player_v,player["rect"])
        else:
            screen.blit(player["img"],player["rect"])
        if power_up:
            screen.blit(power_up["img"],power_up["rect"])

        if hitbox:
            pygame.draw.rect(screen, player["color"], player["rect"],
                                player["borde"], player["radio"])
            if power_up:
                pygame.draw.rect(screen, power_up["color"], power_up["rect"],
                                power_up["borde"], power_up["radio"])
        # Actualizar pantalla

        pygame.display.flip()
    sonido_ambiente.stop()
    game_over_screen(screen, score)


# Finalizar
if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode(SCREEN_SIZE) # Tamaño pantalla
    game_loop(SCREEN)