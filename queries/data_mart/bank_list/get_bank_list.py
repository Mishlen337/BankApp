# -*- coding: utf-8 -*-
"""
Извлекает данные из витрины данных для списка банков.
"""
import sys
sys.path.insert(0, '.')
import config
from datetime import date, datetime
from sqlalchemy import engine, MetaData, select, and_


def _parse_date(b_date: str) -> date:
    """
    Аргумент: дата(месяц) в виде строки.
    Проеобразование в объект date,
    преобразование ее на начало следущего месяца для расчета коэффициентов.
    Возращает этот объект
    """
    formatted_date = datetime.strptime(b_date, "%m.%Y").date()
    # Преобразование ее на начало следущего месяца.
    db_date = date(formatted_date.year, formatted_date.month + 1, 1)
    return db_date


def get_bank_list_mart(connection: engine.Connection, meta: MetaData,
                       names: list, b_date: str) -> list:
    """
    Аргументы: соединение с бд, метаданные бд, список банков и дата(месяц)
    в виде строк.
    Возвращает сортированный по времени список с датами, названием банка и коэффициентами из витрины данных.
    """
    # Преобразование даты(месяца) в виде строки в дату начала след месяца
    db_date = _parse_date(b_date)
    table_mart = meta.tables[config.mart_name]
    table_req = meta.tables['req']
    select_statement = select(table_mart.c.date, table_req.c.NAME_B,
                              table_mart.c.CA, table_mart.c.LR,
                              table_mart.c.CR, table_mart.c.LTR,
                              table_mart.c.CP, table_mart.c.ROA).\
        filter(and_(table_mart.c.date == db_date,
                    table_req.c.index == table_mart.c.bank_index,
                    table_req.c.NAME_B.in_(names)))
    report = connection.execute(select_statement).fetchall()
    # Удаление повторений в наименованиях банков
    uniqued_report = list(set(report))
    # Преобразование списка кортежей в список
    converted_report = [list(i) for i in uniqued_report]
    # Конвертация дат обратно в строки
    for line in converted_report:
        line[0] = date(
            line[0].year,
            line[0].month - 1,
            line[0].day).strftime('%m.%Y')
    sorted_report = sorted(converted_report)
    return sorted_report
