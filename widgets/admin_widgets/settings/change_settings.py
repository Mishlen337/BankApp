# -*- coding: utf-8 -*-
"""
Модуль объявления виджета изменения натсроек.
"""
import sys
sys.path.insert(0, '.')
from PyQt5 import QtWidgets, uic
import config
from widgets.admin_widgets import admin_сhoose_settings


class ChangeSettings(QtWidgets.QDialog):
    """
    Виджет, позоляющий изменять настройки
    (изменение графических настроек и путей к файлам) админу.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui/admin_ui/ChangeSettingsWindow.ui', self)
        # Инициализация кнопок формы
        self.BackPushButton.clicked.connect(self.OnBackPushButton)
        self.PathPushButton.clicked.connect(self.OnPathPushButton)
        self.ApplyDesignPushButton.clicked.connect(
            self.OnApplyDesignPushButton)
        # Инициализация списков выборов размера шрифта и цвета фона
        self.SizeComboBox.addItems(config.size_list)
        self.BackgoundComboBox.addItems(config.background_color_list)

    def OnBackPushButton(self):
        """
        Обработка события нажатия на кнопку "Назад".
        Остановка показа формы изменения настроек и переход к форме выбора
        настроек.
        """
        self.reject()
        admin_сhoose_settings.AdminChooseSettings(parent=self).show()

    def OnPathPushButton(self):
        """
        Обработка события нажатия на кнопку "Выбрать папку".
        Выбор директории для сохранения отчетов.
        """
        # Выбор директории через файловый виджет
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select a directory', '.')
        self.PathLine.setText(directory)
        self.ApplyPathPushButton.clicked.connect(self.OnApplyPathPushButton)

    def OnApplyPathPushButton(self):
        """
        Обработка события нажатия на кнопку "Применить новый путь к папке".
        Сохранение результата в конфиг файле.
        """
        config.excel_path = self.PathLine.text()

    def OnApplyDesignPushButton(self):
        """
        Обработка события нажатия на кнопку
        "Применить новый дизайн приложения".
        Сохранение результата в конфиг файле и изменение параметров
        """
        config.size = int(self.SizeComboBox.currentText())
        config.background_color = self.BackgoundComboBox.currentText()
        # Изменение шрифта и цвета заднего фона
        self.setStyleSheet(
            f"background-color: {config.background_color};font-size: \
                                {config.size}px;")
