# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
from PyQt5 import QtWidgets, uic
from widgets.common_widgets import table_view

class BankReport(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        """
        Виджет, позоляющий просматривать отчет админу
        """
        super().__init__(*args, kwargs['parent'])
        uic.loadUi('./ui/admin_ui/AdminReportWindow.ui', self)
        #Данные таблицы с банками и расчитанными для них коэффициентами
        data = kwargs['data']
        #Инициализация кнопок формы просмотра отчета
        self.QuitPushButton.clicked.connect(self.quitApp)
        #Запись данных в просматриваемую таблицу
        self.TableView.setModel(table_view.TableModel(data))

    def quitApp(self):
        """Выход из приложения"""
        raise SystemExit(1)