import pygame
from game_board import GameBoard, GRID_WIDTH, GRID_HEIGHT

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Определение размера ячейки на игровом поле
CELL_SIZE = 64

# Создание игрового поля
game_board = GameBoard()

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Генерация объектов на поле
    game_board.generate_objects()

    # Отрисовка игрового поля
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            object_image = game_board.get_object(row, col).image
            scaled_image = pygame.transform.scale(object_image, (CELL_SIZE, CELL_SIZE))
            screen.blit(scaled_image, (col * CELL_SIZE, row * CELL_SIZE))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

# Завершение работы Pygame
pygame.quit()
