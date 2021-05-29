# -*- coding: utf-8 -*-
"""
Модуль для объявления виджета соединения с бд.
"""
import sys
sys.path.insert(0, '.')
import sqlalchemy
from PyQt5 import QtWidgets, uic
import config
from widgets import authorization


class Connection(QtWidgets.QDialog):
    """
    Виджет для подключении к бд.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui/ConnectionWindow.ui', self)
        # Инициализация кнопок, выходящих в форму
        self.EnterPushButton.clicked.connect(self.OnEnterPushButton)

    def OnEnterPushButton(self):
        """
        Обработка события нажатия на кнопку подтвердить
        """
        db_connection = self.ConnInput.text()
        try:
            # Проверка существования соединения
            sqlalchemy.create_engine(f"mysql+pymysql://{db_connection}").\
                connect().close()
            config.bank_db_connection = f"mysql+pymysql://{db_connection}"
            # Остановка показа формы соединения
            self.reject()
            # Создание объекта виджета авторизации и начало показа формы
            # авторизации
            authorization.Authorization(parent=self).show()
        except (sqlalchemy.exc.OperationalError):
            self.StatusLabel.setText("Неверное название соединения.")
