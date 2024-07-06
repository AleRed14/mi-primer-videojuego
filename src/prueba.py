import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Evento alternante en Pygame')

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir el evento personalizado
EVENTO_REPETITIVO = pygame.USEREVENT + 1

# Variables para controlar el estado del evento
evento_activado = False
mostrar_rectangulo = False
tiempo_espera = 1000  # 1 segundo en milisegundos

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not evento_activado:
                # Configurar el temporizador para que el evento se repita cada segundo
                pygame.time.set_timer(EVENTO_REPETITIVO, tiempo_espera)
                evento_activado = True
        elif event.type == EVENTO_REPETITIVO:
            # Alternar el estado de mostrar_rectangulo
            mostrar_rectangulo = not mostrar_rectangulo
            if mostrar_rectangulo:
                # Si ahora se debe mostrar el rectángulo, esperar 1 segundo
                pygame.time.set_timer(EVENTO_REPETITIVO, tiempo_espera)
            else:
                # Si ahora se debe esperar, mostrar el rectángulo durante 1 segundo
                pygame.time.set_timer(EVENTO_REPETITIVO, tiempo_espera)

    # Rellenar la pantalla con un color de fondo
    screen.fill(BLACK)

    # Dibujar el rectángulo si mostrar_rectangulo es True
    if mostrar_rectangulo:
        print("hola")
        pygame.draw.rect(screen, RED, (350, 250, 100, 100))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()