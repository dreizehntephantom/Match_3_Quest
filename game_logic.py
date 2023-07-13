import random
import game_board



def check_matches(game_board):
    """Проверяет наличие совпадений на игровом поле и удаляет их.

    Args:
        game_board (GameBoard): Игровое поле.

    Returns:
        bool: True, если были найдены и удалены совпадения, иначе False.
    """
    matches = []

    # Поиск совпадений по горизонтали
    for row in range(game_board.GRID_HEIGHT):
        for col in range(game_board.GRID_WIDTH - 2):
            if game_board.grid[row][col] is not None:
                if game_board.grid[row][col] == game_board.grid[row][col+1] == game_board.grid[row][col+2]:
                    matches.append((row, col))
                    matches.append((row, col+1))
                    matches.append((row, col+2))

    # Поиск совпадений по вертикали
    for row in range(game_board.GRID_HEIGHT - 2):
        for col in range(game_board.GRID_WIDTH):
            if game_board.grid[row][col] is not None:
                if game_board.grid[row][col] == game_board.grid[row+1][col] == game_board.grid[row+2][col]:
                    matches.append((row, col))
                    matches.append((row+1, col))
                    matches.append((row+2, col))

    # Удаление совпадений
    for match in matches:
        row, col = match
        game_board.grid[row][col] = None

    return len(matches) > 0

def generate_objects(game_board):
    """Генерирует новые объекты на пустых ячейках игрового поля.

    Args:
        game_board (GameBoard): Игровое поле.
    """
    for row in range(game_board.GRID_HEIGHT):
        for col in range(game_board.GRID_WIDTH):
            if game_board.grid[row][col] is None:
                # Создание нового случайного объекта
                object_image = load_random_object_image()  # Функция загрузки случайного изображения объекта
                game_board.grid[row][col] = game_board.GameObject(object_image)

def update_score(game_board, points):
    """Обновляет счет игры.

    Args:
        game_board (GameBoard): Игровое поле.
        points (int): Количество очков для добавления к счету.
    """
    game_board.score += points

def load_random_object_image():
    """Загружает случайное изображение объекта.

    Returns:
        pygame.Surface: Изображение объекта.
    """
    image_path = f"C:\\Users\\sasamin4ik\\Desktop\\Match-3 Quest\\png\\object{random.randint(1, 5)}.png"
    return pygame.image.load(image_path)
