import pygame
import random
from game_logic import check_matches, generate_objects, update_score, load_random_object_image
from mouse_handler import MouseHandler


# Определение размеров поля
GRID_WIDTH = 8  # Количество ячеек по горизонтали
GRID_HEIGHT = 8  # Количество ячеек по вертикали
CELL_SIZE = 64  # Размер ячейки в пикселях
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE

class GameObject:
    """Класс для представления игрового объекта."""
    def __init__(self, image):
        self.image = image

class GameBoard:
    """Класс для представления игрового поля."""
    def __init__(self):
        self.grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]  # Инициализация пустой сетки
        self.score = 0  # Инициализация счета

    def set_object(self, row, col, object):
        """Установка объекта в определенную ячейку поля."""
        self.grid[row][col] = object

    def get_object(self, row, col):
        """Получение объекта из определенной ячейки поля."""
        return self.grid[row][col]

    def draw(self, screen):
        """Отрисовка игрового поля."""
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                # Рисование ячеек
                pygame.draw.rect(screen, (255, 255, 255), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                # Рисование объектов на поле
                if self.grid[row][col] is not None:
                    object_image = self.grid[row][col].image
                    screen.blit(object_image, (col * CELL_SIZE, row * CELL_SIZE))

    def move_object(self, row1, col1, row2, col2):
        """Перемещение объекта с одной позиции на другую."""
        if self.is_valid_position(row1, col1) and self.is_valid_position(row2, col2):
            temp_object = self.grid[row1][col1]
            self.grid[row1][col1] = self.grid[row2][col2]
            self.grid[row2][col2] = temp_object

    def is_valid_position(self, row, col):
        """Проверка, является ли позиция действительной на игровом поле."""
        return 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH

    def check_matches(self):
        """Поиск совпадений на игровом поле и их удаление."""
        matches = []

        # Поиск совпадений по горизонтали
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH - 2):
                if self.grid[row][col] is not None:
                    if self.grid[row][col] == self.grid[row][col+1] == self.grid[row][col+2]:
                        matches.append((row, col))
                        matches.append((row, col+1))
                        matches.append((row, col+2))

        # Поиск совпадений по вертикали
        for row in range(GRID_HEIGHT - 2):
            for col in range(GRID_WIDTH):
                if self.grid[row][col] is not None:
                    if self.grid[row][col] == self.grid[row+1][col] == self.grid[row+2][col]:
                        matches.append((row, col))
                        matches.append((row+1, col))
                        matches.append((row+2, col))

        # Удаление совпадений
        for match in matches:
            row, col = match
            self.grid[row][col] = None

        return len(matches) > 0

    def generate_objects(self):
        """Генерация новых объектов на пустых ячейках поля."""
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.grid[row][col] is None:
                    # Создание нового случайного объекта
                    object_image = load_random_object_image()  # Функция загрузки случайного изображения объекта
                    self.grid[row][col] = GameObject(object_image)

    def update_score(self, points):
        """Обновление счета."""
        self.score += points

    def check_win_condition(self):
        """Проверка условия победы."""
        # Здесь можно добавить свою логику для проверки условия победы
        pass

    def check_loss_condition(self):
        """Проверка условия поражения."""
        # Здесь можно добавить свою логику для проверки условия поражения
        pass

def load_random_object_image():
    """Загрузка случайного изображения объекта."""
    image_path = "png/object{}.png".format(random.randint(1, 5))
    return pygame.image.load(image_path)

# Остальной код остается без изменений
