# -*- coding: utf-8 -*-
"""
Модуль для объявления виджета авторизации.
"""
import sys
sys.path.insert(0, '.')
import sqlalchemy
from PyQt5 import QtWidgets, uic
import config
from queries import authorization_db_query
from widgets.client_widgets import client_choose_report
from widgets.admin_widgets import admin_сhoose_settings


class Authorization(QtWidgets.QDialog):
    """
    Виджет для авторизации пользователя.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui/AuthorizationWindow.ui', self)
        # Инициализация кнопок, выходящих в форму
        self.AdminPushButton.clicked.connect(self.adminAuthorization)
        self.ClientPushButton.clicked.connect(self.clientAuthorization)
        self.QuitPushButton.clicked.connect(self.quitApp)

    def adminAuthorization(self):
        """Обработка события нажатия на кнопку Aдмин"""
        self.AuthorizationHeadingLabel.setText("Введите пароль админа")
        # Поменять цвет кнопки Клиента на дефолтный
        self.ClientPushButton.setStyleSheet(f"background-color: \
                                                {config.background_color}")
        # Поменять цвет кнопки Админа на красный
        self.AdminPushButton.setStyleSheet("background-color: red")
        # Инициализация кнопки "Войти"
        self.EnterPushButton.clicked.connect(self.checkAdminAuthorization)

    def checkAdminAuthorization(self):
        """
        Обработка события нажатия на кнопку Войти.
        Проверка логина и пароля Админа в базе данных пользователей
        """
        username = self.UsernameLineEdit.text()
        password = self.PasswordLineEdit.text()
        # Обработка потери соединения с БД
        try:
            # Проверка нахождения логина и пароля в базе данных админов
            if authorization_db_query.admin_verification(username, password):
                # Остановка показа формы авторизации
                self.reject()
                # Создание объекта виджета выбора настроек и отображении формы
                # пользователю
                admin_сhoose_settings.AdminChooseSettings(parent=self).show()
            else:
                self.AuthorizationHeadingLabel.setText(
                    "Неверный пароль админа. Попробуйте еще раз")
        except (sqlalchemy.exc.OperationalError):
            self.AuthorizationHeadingLabel.setText("Соединение с БД потеряно")

    def clientAuthorization(self):
        """Обработка события нажатия на кнопку Клиент"""
        self.AuthorizationHeadingLabel.setText("Введите пароль клиента")
        # Поменять цвет кнопки Админа на дефолтный
        self.AdminPushButton.setStyleSheet(f"background-color: \
                                        {config.background_color}")
        # Поменять цвет кнопки Клиента на красный
        self.ClientPushButton.setStyleSheet("background-color: red")
        # Инициализация кнопки "Войти"
        self.EnterPushButton.clicked.connect(self.checkClientAuthorization)

    def checkClientAuthorization(self):
        """
        Обработка события нажатия на кнопку Войти.
        Проверка логина и пароля Клиента в базе данных пользователей
        """
        username = self.UsernameLineEdit.text()
        password = self.PasswordLineEdit.text()
        # Обработка потери соединения с БД
        try:
            # Проверка нахождения логина и пароля в базе данных клиентов
            if authorization_db_query.client_verification(username, password):
                # Остановка показа формы авторизации
                self.reject()
                # Создание объекта виджета выбора отчета и отображение формы
                # пользователю
                client_choose_report.ChooseReport(parent=self).show()
            else:
                self.AuthorizationHeadingLabel.setText(
                    "Неверный пароль клиента. Попробуйте еще раз")
        except (sqlalchemy.exc.OperationalError):
            self.AuthorizationHeadingLabel.setText("Соединение с БД потеряно")

    def quitApp(self):
        """Выход из приложения"""
        raise SystemExit(1)
