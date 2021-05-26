# -*- coding: utf-8 -*-
"""
Извлекает данные из витрины данных для банка.
"""
import sys
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
import config
from datetime import date, datetime
from sqlalchemy import engine, MetaData, select, and_

def _parse_date(b_date:str)->date:
    """
    Аргумент: дата(месяц) в виде строки.
    Проеобразование в объект date,
    преобразование ее на начало следущего месяца для расчета коэффициентов.
    Возращает этот объект
    """
    formatted_date = datetime.strptime(b_date,"%m.%Y").date()
    #Преобразование ее на начало следущего месяца.
    db_date = date(formatted_date.year, formatted_date.month + 1, 1)
    return db_date

def _parse_gap_dates(start_date:str, end_date: str)->list:
    """
    Аргументы: начальная и конечная дата(месяцев) в виде строк.
    Проеобразование в объект date,
    преобразование их на начало следущего месяца для расчета коэффициентов,
    Возвращает список промежутка начальной и конечной даты.
    """
    dates_list = []
    #Проеобразование в объект date, на начало следущего месяца.
    start_db_date = _parse_date(start_date)
    end_db_date = _parse_date(end_date)
    #Преобразование начальной и конечной даты в список дат между ними
    b_date = start_db_date
    dates_list.append(b_date)
    delta = 1
    #b_date = date(b_date.year, b_date.month + delta, b_date.day)
    while b_date < end_db_date:
        b_date = date(b_date.year, b_date.month + delta, b_date.day)
        dates_list.append(b_date)
    return dates_list

def get_bank_mart(connection: engine.Connection, meta: MetaData,
                    name: str, start_date: str, end_date: str):
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и начальная и конечная дата(месяцев)
    в виде строк.
    Возвращает сортированный по времени список с датами, названием банка и коэффициентами из витрины данных.
    """
    #Преобразование начальной и конечной даты(месяця) в виде строки в список дат за этот промежуток
    db_dates = _parse_gap_dates(start_date, end_date)
    #Ассоциация с таблицей витрины данных
    table_mart = meta.tables[config.mart_name]
    #Ассоциация с таблицей req
    table_req = meta.tables['req']
    #Извлечение данных из витрины данных
    select_statement = select(table_mart.c.date, table_req.c.NAME_B,
                                table_mart.c.CA, table_mart.c.LR,
                                table_mart.c.CR, table_mart.c.LTR,
                                table_mart.c.CP,table_mart.c.ROA).\
                        filter(and_(table_mart.c.date.in_(db_dates),
                                    table_req.c.index == table_mart.c.bank_index,
                                    table_req.c.NAME_B == name))
    report = connection.execute(select_statement).fetchall()
    #Удаление повторений в наименованиях банка
    uniqued_report = list(set(report))
    #Преобразование списка кортежей в список списков
    converted_report = [list(i) for i in uniqued_report]
    #Конвертация дат обратно в строки
    for line in converted_report:
        line[0] = date(line[0].year, line[0].month - 1, line[0].day).strftime('%m.%Y')
    sorted_report = sorted(converted_report)
    return sorted_report
