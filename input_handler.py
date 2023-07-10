import pygame

def handle_input(events, game_board):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(event, game_board)
        elif event.type == pygame.MOUSEBUTTONUP:
            handle_mouse_release(event, game_board)

def handle_mouse_click(event, game_board):
    if event.button == 1:  # Левая кнопка мыши
        mouse_x, mouse_y = event.pos
        clicked_row, clicked_col = get_clicked_cell(mouse_x, mouse_y)
        
        # Передаем координаты клика в метод move_object игрового поля
        game_board.move_object(clicked_row, clicked_col)

def handle_mouse_release(event, game_board):
    if event.button == 1:  # Левая кнопка мыши
        mouse_x, mouse_y = event.pos
        released_row, released_col = get_clicked_cell(mouse_x, mouse_y)
        
        # Передаем координаты отпускания в метод release_object игрового поля
        game_board.release_object(released_row, released_col)

def get_clicked_cell(mouse_x, mouse_y):
    # Определение координат ячейки, в которую произошел клик мыши
    row = mouse_y // CELL_SIZE
    col = mouse_x // CELL_SIZE
    return row, col
