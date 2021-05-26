# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
import pandas as pd
from PyQt5 import QtWidgets, uic
import config
from widgets.admin_widgets import admin_сhoose_settings, report
from queries import bank_db_query

class FormBankListReport(QtWidgets.QDialog):
    """
    Виджет, позволяющий задавать параметры отчета (список банков, и дата)
    для формирования витрины и просмотра данных для одного банка админу.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui/common_ui/BankListReportWindow.ui', self)
        #Инициализация кнопок, входящих в форму
        self.BackPushButton.clicked.connect(self.OnBackPushButton)
        self.FormPushButton.clicked.connect(self.calculateAdminBankListReport)
        #self.BankListWidget.addItems(bank_db_query.bank_names_query())

    def OnBackPushButton(self):
        """
        Обработка события нажатия на кнопку "Назад".
        Остановка показа формы формирования отчета для нескольких банков 
        и переход к форме выбора настроек.
        """
        self.reject()
        admin_сhoose_settings.AdminChooseSettings(parent = self).show()

    def calculateAdminBankListReport(self):
        """
        Обработка события нажатия на кнопку "Сформировать отчет"
        Берет расчитанные коэффициенты из витрины данных, при необходимости расчитывает
        коэффициенты и сохраняет их в витрине.
        Остановка показа формы формирования отчета для нескольких банков
        и переход к форме отображения отчета.
        """
        bank_list = [item.text() for item in self.BankListWidget.selectedItems()]
        b_date = self.DateEdit.text()
        #Получение данных из витрины данных
        data = pd.DataFrame(bank_db_query.bank_list_query(bank_list, b_date),
                                                            columns = config.columns)

        #Остановка показа формы формирования отчета для одного банка
        self.reject()
        #Переход к форме отображения отчета
        report.BankReport(parent = self, data = data).show()
