# -*- coding: utf-8 -*-
"""
Модуль для объявления класса таблицы.
"""
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    """
    Класс, позволяющий отобразить данные в виде таблицы в отчете
    """

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        """
        Отображает данные в таблице
        """
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        """
        Возвращает кол-во строк
        """
        return self._data.shape[0]

    def columnCount(self, index):
        """
        Возвращает кол-во столбцов
        """
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        """
        Возвращает названия строк и столбцов
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])
