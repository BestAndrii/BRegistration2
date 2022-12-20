"""Модуль для запуска программы."""


import sys

import des

from PyQt5.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow):
    """Класс создаёт главное окно."""

    def __init__(self):
        """Инициализация окна."""
        super().__init__()

        # Загрузка дизайна
        self.ui = des.Interface(self)


def run_app():
    """Запускает программу."""
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
