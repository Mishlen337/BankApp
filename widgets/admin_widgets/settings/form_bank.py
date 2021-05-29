# -*- coding: utf-8 -*-
"""
Модуль для объявления виджета формирования отчета банка админу.
"""
import sys
sys.path.insert(0, '.')
import sqlalchemy
import pandas as pd
from PyQt5 import QtWidgets, uic
import config
from queries import bank_db_query
from widgets.admin_widgets import admin_сhoose_settings, report


class FormBankReport(QtWidgets.QDialog):
    """
    Виджет, позволяющий задавать параметры отчета (имя банка, начальная и
    конечная дата) для формирования витрины и просмотра данных для одного 
    банка админу.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui/common_ui/BankReportWindow.ui', self)
        # Инициализация кнопок, входящих в форму
        self.BackPushButton.clicked.connect(self.OnBackPushButton)
        self.FormPushButton.clicked.connect(self.calculateAdminBankReport)
        # Обработка потери соединения с БД
        try:
            # Вставка наименований банков в окно выбора
            self.BankNameComboBox.addItems(bank_db_query.bank_names_query())
        except (sqlalchemy.exc.OperationalError):
            self.StatusLabel.setText("Соединение с БД потеряно")

    def OnBackPushButton(self):
        """
        Обработка события нажатия на кнопку "Назад".
        Остановка показа формы формирования отчета для одного банка
        и переход к форме выбора настроек.
        """
        self.reject()
        admin_сhoose_settings.AdminChooseSettings(parent=self).show()

    def calculateAdminBankReport(self):
        """
        Обработка события нажатия на кнопку "Сформировать отчет"
        Берет расчитанные коэффициенты из витрины данных, при необходимости
        расчитывает коэффициенты и сохраняет их в витрине.
        Остановка показа формы формирования отчета для одного банка
        и переход к форме отображения отчета.
        """
        start_date = self.StartDateEdit.text()
        end_date = self.EndDateEdit.text()
        bank = self.BankNameComboBox.currentText()
        # Обработка потери соединения с БД
        try:
            # Получение данных из витрины данных
            data = pd.DataFrame(
                bank_db_query.bank_query(
                    bank,
                    start_date,
                    end_date),
                columns=config.columns)
            # Остановка показа формы формирования отчета для одного банка
            self.reject()
            # Переход к форме отображения отчета
            report.BankReport(parent=self, data=data).show()
        except (sqlalchemy.exc.OperationalError):
            self.StatusLabel.setText("Соединение с БД потеряно")
