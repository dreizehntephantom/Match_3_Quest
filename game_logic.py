import random

def check_matches(grid):
    # Проверка совпадений на игровом поле и их удаление
    matches = []

    # Проверка совпадений по горизонтали
    for row in range(len(grid)):
        for col in range(len(grid[0]) - 2):
            if grid[row][col] is not None:
                if grid[row][col] == grid[row][col+1] == grid[row][col+2]:
                    matches.append((row, col))
                    matches.append((row, col+1))
                    matches.append((row, col+2))

    # Проверка совпадений по вертикали
    for row in range(len(grid) - 2):
        for col in range(len(grid[0])):
            if grid[row][col] is not None:
                if grid[row][col] == grid[row+1][col] == grid[row+2][col]:
                    matches.append((row, col))
                    matches.append((row+1, col))
                    matches.append((row+2, col))

    # Удаление совпадений
    for match in matches:
        row, col = match
        grid[row][col] = None

    return len(matches) > 0

def generate_objects(grid):
    # Генерация новых объектов на пустых ячейках поля
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] is None:
                # Создание нового случайного объекта
                object_image = load_random_object_image()  # Функция загрузки случайного изображения объекта
                grid[row][col] = GameObject(object_image)

def update_score(score, points):
    # Обновление счета
    score += points
    return score

def load_random_object_image():
    # Загрузка случайного изображения объекта
    object_images = [
        pygame.image.load("png/object1.png"),
        pygame.image.load("png/object2.png"),
        pygame.image.load("png/object3.png"),
        pygame.image.load("png/object4.png"),
        pygame.image.load("png/object5.png")
    ]
    return random.choice(object_images)
