import pygame
from pygame.locals import *


def handle_input(game_board):
    """Обрабатывает пользовательский ввод.

    Args:
        game_board (GameBoard): Игровое поле.

    Returns:
        bool: Флаг, указывающий, нужно ли завершить игру.
    """
    quit_game = False

    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            quit_game = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit_game = True
            elif event.key == K_UP:
                game_board.move_up()
            elif event.key == K_DOWN:
                game_board.move_down()
            elif event.key == K_LEFT:
                game_board.move_left()
            elif event.key == K_RIGHT:
                game_board.move_right()

    return quit_game
