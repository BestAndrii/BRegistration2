"""Модуль интерфейса программы."""


from PyQt5 import QtCore, QtGui, QtWidgets

from functions import get_file_text


class Interface:
    """Класс создаёт интерфейс программы."""

    def __init__(self, window):
        """Создание интерфейса."""
        # Настройки окна
        window.setWindowTitle("BRegistration")
        window.setObjectName("MainWindow")
        window.resize(330, 150)
        window.setStyleSheet(get_file_text("css/main_window.css")) # CSS

        # Центральный виджет со всем интерфейсом
        self.centralwidget = QtWidgets.QWidget(window)

        # region Иконки
        # Иконка регистрации
        sing_up_icon = QtGui.QIcon()
        sing_up_icon.addPixmap(QtGui.QPixmap("icons/зарегестрироваться.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Иконка входа
        sing_in_icon = QtGui.QIcon()
        sing_in_icon.addPixmap(QtGui.QPixmap("icons/войти.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # endregion

        # Кнопка регистрации
        self.sing_up = QtWidgets.QPushButton(self.centralwidget)
        self.sing_up.setGeometry(QtCore.QRect(30, 10, 110, 110))
        self.sing_up.setIcon(sing_up_icon)
        self.sing_up.setIconSize(QtCore.QSize(70, 70))

        # Кнопка входа
        self.sing_up = QtWidgets.QPushButton(self.centralwidget)
        self.sing_up.setGeometry(QtCore.QRect(190, 10, 110, 110))
        self.sing_up.setIcon(sing_in_icon)
        self.sing_up.setIconSize(QtCore.QSize(70, 70))

        # Текст под кнопкой регистрации
        self.sing_up_label = QtWidgets.QLabel(self.centralwidget)
        self.sing_up_label.setGeometry(QtCore.QRect(20, 125, 130, 16))

        # Текст под кнопкой входа
        self.sing_in_label = QtWidgets.QLabel(self.centralwidget)
        self.sing_in_label.setGeometry(QtCore.QRect(230, 125, 40, 16))

        window.setCentralWidget(self.centralwidget)

        # Добавляем текст объектам QLabel
        self.sing_up_label.setText("Зарегестрироваться")
        self.sing_in_label.setText("Войти")
