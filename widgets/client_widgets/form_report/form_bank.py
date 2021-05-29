# -*- coding: utf-8 -*-
"""
Модуль для объявления виджета параметров отчета банка.
"""
import sys
sys.path.insert(0, '.')
import sqlalchemy
import pandas as pd
from PyQt5 import QtWidgets, uic
from widgets.client_widgets import client_choose_report, report
from queries import bank_db_query
import config


class FormBankReport(QtWidgets.QDialog):
    """
    Виджет, позволяющий задавать параметры отчета (имя банка, начальная и
    конечная дата) для формирования витрины и просмотра данных для одного банка клиенту.
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
        и переход к форме выбора отчета.
        """
        self.reject()
        client_choose_report.ChooseReport(parent=self).show()

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
