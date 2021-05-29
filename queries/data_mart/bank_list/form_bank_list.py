# -*- coding: utf-8 -*-
"""
Извлекает данные из витрины данных для списка банков.
"""
import sys
sys.path.insert(0, '.')
from sqlalchemy import engine, MetaData, select, and_
from datetime import date, datetime
import config
from queries.data_mart import existance
from queries.calculate import get_ratios


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


def _insert_bank_list(
        connection: engine.Connection,
        meta: MetaData,
        ratios: dict,
        b_date: date):
    """
    Аргументы: соединение с бд, метаданные бд, дата и 
    словарь, ключи - именования банков, значения - 
    списки, рассчитанных коэффициентов для банков, за
    данную дату.
    Вставляет данные в витрину данных
    """
    # Ассоциация с таблицой витрины данных
    table_mart = meta.tables[config.mart_name]
    # Ассоциация с таблицей req
    table_req = meta.tables['req']
    for name in ratios:
        # Нахождение индекса банка в таблице req
        select_statement = select(
            table_req.c.index).filter(
            table_req.c.NAME_B == name)
        result = connection.execute(select_statement)
        bank_index = result.fetchone()[0]
        # Вставка данных в витрину данных
        insert_statement = table_mart.\
            insert().values(bank_index=bank_index, date=b_date,
                            CA=ratios[name][0], LR=ratios[name][1],
                            CR=ratios[name][2], LTR=ratios[name][3],
                            CP=ratios[name][4], ROA=ratios[name][5])
        connection.execute(insert_statement)


def _mart_bank_list(connection: engine.Connection, meta: MetaData,
                    names: list, b_date: date) -> dict:
    """
    Аргументы: соединение с бд, метаданные бд, список банков и дата (месяц)
    Расчитывает коэффициенты надежности и эффективности для списка банков, не включая уже
    расчитанных.
    Возвращает словарь. Ключи - наименование банков из списка.
    Значения - список расчитанных коэффициентов за дату.
    """
    # Ассоциация с таблицой витрины данных
    table_mart = meta.tables[config.mart_name]
    # Ассоциация с таблицей req
    table_req = meta.tables['req']
    # Нахождение банков уже расчитанных коэффициентов для этой даты
    select_statement = select(table_req.c.NAME_B).\
        filter(and_(table_mart.c.date == b_date,
                    table_req.c.index == table_mart.c.bank_index,
                    table_req.c.NAME_B.in_(names)))
    result = connection.execute(select_statement)
    query = result.fetchall()
    # Преобрахование списка дат в список
    parsed_query = [i[0] for i in query]
    # Расчет коэффициентов не входящих в витрину данных бд
    ratios = get_ratios.get_bank_list_ratios(
        connection, meta, list(
            set(names).difference(parsed_query)), b_date)
    return ratios


def form_bank_list_mart(
        db_engine: engine,
        connection: engine.Connection,
        meta: MetaData,
        names: list,
        b_date: str):
    """
    Аргументы: соединение с бд, метаданные бд, список банков и дата(месяц)
    в виде строк. Расчитывает значения коэффициентов для списка банков за определенное времени
    (месяц) и дополняет витрину данных.
    """
    # Преобразование даты(месяца) в виде строки в дату начала след месяца
    db_date = _parse_date(b_date)
    # Расчитывает значения коэффициентов
    existance.check_mart_existence(db_engine, meta)
    ratios = _mart_bank_list(connection, meta, names, db_date)
    print("Calculated ratios")
    print(ratios)
    # Дополнение витрины данными
    _insert_bank_list(connection, meta, ratios, db_date)
