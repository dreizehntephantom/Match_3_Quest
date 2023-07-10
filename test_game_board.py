#test_game_board.py
import unittest
from game_board import GameBoard

class TestGameBoard(unittest.TestCase):
    def test_move_object(self):
        # Создание игрового поля
        game_board = GameBoard()
        
        # Установка объекта в исходную ячейку
        game_board.set_object(0, 0, "A")
        
        # Перемещение объекта
        game_board.move_object(0, 0, 1, 0)
        
        # Проверка, что объект переместился в новую ячейку
        self.assertEqual(game_board.get_object(1, 0), "A")
        self.assertIsNone(game_board.get_object(0, 0)) # Проверка, что исходная ячейка стала пустой

if __name__ == "__main__":
    unittest.main()
