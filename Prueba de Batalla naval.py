import pygame
import numpy as np
import math

# Inicialización de pygame
pygame.init()

# Dimensiones del tablero
BOARD_SIZE = 10
CELL_SIZE = 40
MARGIN = 5

# Dimensiones de la ventana
WINDOW_SIZE = (BOARD_SIZE * CELL_SIZE + (BOARD_SIZE + 1) * MARGIN,
               BOARD_SIZE * CELL_SIZE + (BOARD_SIZE + 1) * MARGIN)

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Creación de la pantalla
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Batalla Naval")

# Tablero del juego
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

def place_ship(board, ship_size):
    placed = False
    while not placed:
        orientation = np.random.choice(['H', 'V'])
        if orientation == 'H':
            row = np.random.randint(0, BOARD_SIZE)
            col = np.random.randint(0, BOARD_SIZE - ship_size + 1)
            if np.all(board[row, col:col + ship_size] == 0):
                board[row, col:col + ship_size] = 1
                placed = True
        else:
            row = np.random.randint(0, BOARD_SIZE - ship_size + 1)
            col = np.random.randint(0, BOARD_SIZE)
            if np.all(board[row:row + ship_size, col] == 0):
                board[row:row + ship_size, col] = 1
                placed = True

def shoot(board, row, col):
    if board[row, col] == 1:
        board[row, col] = 2
        return "Hit"
    elif board[row, col] == 0:
        board[row, col] = 3
        return "Miss"
    return "Already Shot"

# Colocar barcos en el tablero
for ship_size in [5, 4, 3, 3, 2]:
    place_ship(board, ship_size)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (CELL_SIZE + MARGIN)
            row = pos[1] // (CELL_SIZE + MARGIN)
            if row < BOARD_SIZE and col < BOARD_SIZE:
                result = shoot(board, row, col)
                print(result)

    # Dibujar tablero
    screen.fill(BLACK)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE
            if board[row, col] == 1:
                color = BLUE
            elif board[row, col] == 2:
                color = GREEN
            elif board[row, col] == 3:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + CELL_SIZE) * col + MARGIN,
                              (MARGIN + CELL_SIZE) * row + MARGIN,
                              CELL_SIZE,
                              CELL_SIZE])

    pygame.display.flip()

pygame.quit()
