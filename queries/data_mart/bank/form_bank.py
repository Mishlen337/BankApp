# -*- coding: utf-8 -*-
"""
Формирует витрину данных для банка.
"""
import sys
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
import config
from datetime import date, datetime
from sqlalchemy import engine, MetaData, select, and_
from queries.data_mart import existance
from queries.calculate import get_ratios

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

def _insert_bank(connection: engine.Connection, meta: MetaData, ratios: dict, name: str):
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и список дат.
    Вставляет данные в витрину данных
    """
    #Ассоциация с таблицой витрины данных
    table_mart = meta.tables[config.mart_name]
    #Ассоциация с таблицей req
    table_req = meta.tables['req']
    #Нахождение индекса банка в таблице req
    select_statement = select(table_req.c.index).filter(table_req.c.NAME_B == name)
    result = connection.execute(select_statement)
    bank_index = result.fetchone()[0]
    #Вставка данных в витрину данных
    for b_date in ratios:
        insert_statement = table_mart.\
                                    insert().values(bank_index = bank_index, date = b_date,
                                                    CA = ratios[b_date][0], LR = ratios[b_date][1],
                                                    CR = ratios[b_date][2], LTR = ratios[b_date][3],
                                                    CP = ratios[b_date][4], ROA = ratios[b_date][5])
        connection.execute(insert_statement)


def _mart_bank(connection: engine.Connection, meta: MetaData, name: str, b_dates: list)->dict:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и список дат.
    Расчитывает коэффициенты надежности и эффективности для банка, не включая уже
    расчитанных.
    Возвращает словарь. Ключи - дата из списка дат.
    Значения - список расчитанных коэффициентов для этого банка.
    """
    #Ассоциация с таблицей витрины
    table_mart = meta.tables[config.mart_name]
    #Ассоциация с таблицей req
    table_req = meta.tables['req']
    #Нахождение дат уже расчитанных коэффициентов для этого банк
    select_statement = select(table_mart.c.date).\
                        filter(and_(table_mart.c.date.in_(b_dates),
                                    table_req.c.index == table_mart.c.bank_index,
                                    table_req.c.NAME_B == name))
    result = connection.execute(select_statement)
    query = result.fetchall()
    #Преобразование списка кортежей в список
    parsed_query = [i[0] for i in query]
    #Расчет коэффициентов не входящих в витрину данных бд
    ratios = get_ratios.get_bank_ratios(connection, meta, name, list(set(b_dates).\
                                                        difference(parsed_query)))
    return ratios

def form_bank_mart(db_engine: engine, connection: engine.Connection, meta: MetaData,
                name: str, start_date: str, end_date: str):
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и начальная и конечная дата(месяцев)
    в виде строк. Расчитывает значения коэффициентов для банка за промежуток времени
    и дополняет витрину данных.
    """
    #Преобразование начальной и конечной даты(месяця) в виде строки в список дат за этот промежуток
    b_dates = _parse_gap_dates(start_date, end_date)
    existance.check_mart_existence(db_engine, meta)
    #Расчитывает значения коэффициентов
    ratios = _mart_bank(connection, meta, name, b_dates)
    print("Calculated ratios")
    print(ratios)
    #Дополнение витрины данными
    _insert_bank(connection, meta, ratios, name)
