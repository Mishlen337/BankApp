# -*- coding: utf-8 -*-
"""
Модуль для объявления виджета выбора настроек.
"""
import sys
sys.path.insert(0, '.')
from PyQt5 import QtWidgets, uic
from widgets import authorization
from widgets.admin_widgets.settings import change_settings, form_bank, form_bank_list


class AdminChooseSettings(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        """
        Виджет, позоляющий выбрать настройки
        (Сформировать витрины данных или изменить графические настройки и пути к файлам) админу.
        """
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui/admin_ui/AdminChooseSettingsWindow.ui', self)
        # Инициализация кнопок формы выбора настроек
        self.BackPushButton.clicked.connect(self.OnBackPushButton)
        self.BankPushButton.clicked.connect(self.OnBankPushButton)
        self.BankListPushButton.clicked.connect(self.OnBankListPushButton)
        self.ChangeSettingsPushButton.clicked.connect(
            self.OnChangeSettingsPushButton)

    def OnBackPushButton(self):
        """
        Обработка нажатия на кнопку "Назад".
        Остановка показа формы выбора настроек и переход к форме авторизации.
        """
        self.reject()
        authorization.Authorization(parent=self).show()

    def OnBankPushButton(self):
        """
        Обработка нажатия на кнопку "Отчет для одного банка"
        Остановка показа формы выбора настроек и переход к форме формирования отчета
        """
        self.reject()
        form_bank.FormBankReport(parent=self).show()

    def OnBankListPushButton(self):
        """
        Обработка нажатия на кнопку "Отчет для нескольких банков"
        Остановка показа формы выбора настроек и переход к форме формирования отчета
        """
        self.reject()
        form_bank_list.FormBankListReport(parent=self).show()

    def OnChangeSettingsPushButton(self):
        """
        Обработка нажатия на кнопку "Изменить настройки"
        Остановка показа формы выбора настроек и переход к форме изменения настроек
        """
        self.reject()
        change_settings.ChangeSettings(parent=self).show()
