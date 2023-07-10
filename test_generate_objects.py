#test_generate_objects.py
import unittest
from game_board import GameBoard
from game_logic import generate_objects
from game_board import GRID_WIDTH, GRID_HEIGHT



class TestGameBoard(unittest.TestCase):
    def test_generate_objects(self):
        # Создание игрового поля
        game_board = GameBoard()

        # Генерация объектов на пустом поле
        game_board.generate_objects()

        # Проверка, что все ячейки содержат объекты
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                self.assertIsNotNone(game_board.grid[row][col])

if __name__ == "__main__":
    unittest.main()
