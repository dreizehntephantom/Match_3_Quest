from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from menu1 import Ui_MainWindow

class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        
        # Инициализация главного меню
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Привязка обработчиков событий к кнопкам
        self.ui.Continue_Game_Button.clicked.connect(self.continue_game)
        self.ui.New_Gamee_Button.clicked.connect(self.new_game)
        self.ui.Gallery_Button.clicked.connect(self.open_gallery)
        self.ui.Settings_Button.clicked.connect(self.open_settings)
        self.ui.Exit_Button.clicked.connect(self.exit_game)
        
        # Установка фонового изображения
        bg_image = QPixmap(":/21.png")
        self.ui.Menu_bg.setPixmap(bg_image)
        
    def continue_game(self):
        # Обработчик события для кнопки "Continue Game"
        print("Continue Game")
        # Здесь можно добавить логику загрузки сохраненной игры
        
        # Переход к игровому полю
        game_field = GameField()
        game_field.show()
        self.hide()
        
    def new_game(self):
        # Обработчик события для кнопки "New Game"
        print("New Game")
        # Здесь можно добавить логику создания новой игры или профиля игрока
        
        # Переход к игровому полю
        game_field = GameField()
        game_field.show()
        self.hide()
        
    def open_gallery(self):
        # Обработчик события для кнопки "Gallery"
        print("Open Gallery")
        # Здесь можно добавить логику открытия галереи с достижениями или изображениями
        
    def open_settings(self):
        # Обработчик события для кнопки "Settings"
        print("Open Settings")
        # Здесь можно добавить логику открытия экрана настроек
        
    def exit_game(self):
        # Обработчик события для кнопки "Exit"
        print("Exit Game")
        # Здесь можно добавить логику выхода из игры или сохранения прогресса
        
        # Завершение работы приложения
        QtWidgets.qApp.quit()


class GameField(QtWidgets.QMainWindow):
    def __init__(self):
        super(GameField, self).__init__()
        
        # Инициализация игрового поля
        # ...

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())
