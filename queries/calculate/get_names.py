# -*- coding: utf-8 -*-
"""
Модуль для получения имен наименований банков из бд.
"""
from sqlalchemy import engine, MetaData, select


def get_bank_names(connection: engine.Connection, meta: MetaData) -> list:
    """
    Аргументы: соединение с бд, метаданные бд.
    Возвращает наименования банков из бд.
    """
    # Ассоциация с таблицей req бд
    table_req = meta.tables['req']
    select_statement = select(table_req.c.NAME_B)
    result = connection.execute(select_statement)
    bank_names = result.fetchall()
    # Преобразование списка кортежей в список
    bank_names_list = [i[0] for i in bank_names]
    # Удаление повторяющихся наименований банков
    unique_bank_names = list(set(bank_names_list))
    # Сортировка элементов в лексографическом порядке
    sorted_bank_names = sorted(unique_bank_names)
    return sorted_bank_names
