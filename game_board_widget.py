from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import sys
import random


class GameBoardWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Создание сетки игрового поля
        layout = QGridLayout()
        self.setLayout(layout)

        # Создание игровых элементов и добавление их в сетку
        for row in range(8):
            for col in range(8):
                # Создание QLabel для отображения игрового элемента
                label = QLabel()
                label.setFixedSize(64, 64)  # Установка фиксированного размера для игрового элемента
                label.setFrameStyle(QLabel.Box)  # Оформление рамки вокруг элемента

                # Загрузка случайного изображения для игрового элемента
                image_path = "png/object{}.png".format(random.randint(1, 5))
                pixmap = QPixmap(image_path)

                # Масштабирование изображения до размера QLabel
                scaled_pixmap = pixmap.scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
                label.setPixmap(scaled_pixmap)

                # Добавление игрового элемента в сетку
                layout.addWidget(label, row, col)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    game_board = GameBoardWidget()
    game_board.show()

    sys.exit(app.exec_())
