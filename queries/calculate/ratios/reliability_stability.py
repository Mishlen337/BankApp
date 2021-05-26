# -*- coding: utf-8 -*-
"""
Расчет коэффициентов надежности и устойчивости банка.
"""
from datetime import date
from sqlalchemy import engine, MetaData, select, and_

def _get_capital_adequacy(connection: engine.Connection, meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение коэффициента достаточности капитала на начало этой даты.
    Возвращает это значение.
    """
    #Ассоциация с таблицей f135
    bank = meta.tables['f135']
    #Извлечение данных из таблицы
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н1.0"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def _get_liquidity_ratio(connection: engine.Connection,meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение коэффициента мгновенной̆ ликвидности на начало этой даты.
    Возвращает это значение.
    """
    #Ассоциация с таблицей f135
    bank = meta.tables['f135']
    #Извлечение данных из таблицы
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н2"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def _get_current_ratio(connection: engine.Connection,meta: MetaData,
                        name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение коэффициента текущей ликвидности на начало этой даты.
    Возвращает это значение.
    """
    #Ассоциация с таблицей f135
    bank = meta.tables['f135']
    #Извлечение данных из таблицы
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н3"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def _get_longterm_ratio(connection: engine.Connection,meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение коэффициента долгосрочной ликвидности на начало этой даты.
    Возвращает это значение.
    """
    #Ассоциация с таблицей f135
    bank = meta.tables['f135']
    #Извлечение данных из таблицы
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н4"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def get_reliability_stability(connection: engine.Connection,meta: MetaData,
                                name: str, b_date: date)->list:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение коэффициентов надежности и устойчивости банка на начало этой даты.
    Возвращает список этих значений.
    """
    capital_adequacy = _get_capital_adequacy(connection, meta, name,b_date)
    liquidity_ratio = _get_liquidity_ratio(connection, meta, name,b_date)
    current_ratio = _get_current_ratio(connection, meta, name,b_date)
    longterm_ratio = _get_longterm_ratio(connection, meta, name,b_date)
    return [capital_adequacy, liquidity_ratio, current_ratio,longterm_ratio]
