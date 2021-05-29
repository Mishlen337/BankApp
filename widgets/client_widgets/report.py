# -*- coding: utf-8 -*-
"""
Модуль для объявления виджета просмотра отчета.
"""
import sys
sys.path.insert(0, '.')
import pandas as pd
import datetime
from PyQt5 import QtWidgets, uic
import config
from widgets.common_widgets import table_view


class BankReport(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        """
        Виджет, позволяющий просматривать отчет и сохранять в Excel файл отчет
        """
        super().__init__(*args, kwargs['parent'])
        uic.loadUi('./ui/client_ui/ReportWindow.ui', self)
        # Данные таблицы с банками и расчитанными для них коэффициентами
        data = kwargs['data']
        # Инициализация кнопок формы просмотра отчета
        self.QuitPushButton.clicked.connect(self.quitApp)
        self.ExportPushButton.clicked.connect(lambda: self.exportReport(data))
        # Запись данных в просматриваемую таблицу
        self.TableView.setModel(table_view.TableModel(data))

    def exportReport(self, data: pd.DataFrame):
        """
        Recieves data in dataframe format.
        Exports data to excel file in particular folder.
        """
        current_time = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
        report_name = f"БО {current_time}.xlsx"
        data.to_excel(f"{config.excel_path}/{report_name}")
        self.StatusLabel.setText(f"Экспорт данных произошел успешно в папку \
                                            {config.excel_path}")

    def quitApp(self):
        """Выход из приложения"""
        raise SystemExit(1)
