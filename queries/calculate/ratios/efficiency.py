# -*- coding: utf-8 -*-
"""
Расчет коэффициентов эффективности
"""
import sys
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
from datetime import date
from sqlalchemy import engine, MetaData, select, and_
from queries.calculate.ratios import reliability_stability

def _get_net_income_quater(connection: engine.Connection, meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дату начала квартала.
    Расчитывает значение балансовой прибыли, нарастающим итогом
    Возвращает это значение на начало квартала.
    """
    #Ассоциация с таблицей f102
    bank = meta.tables['f102']
    #Поиск доходов
    select_statement = select(bank.c.SIM_ITOGO).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.CODE == 19999))
    result = connection.execute(select_statement)
    incomes = result.fetchone()[0]
    #Поиск расходов
    select_statement = select(bank.c.SIM_ITOGO).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.CODE == 29999))
    result = connection.execute(select_statement)
    consumptions = result.fetchone()[0]
    return incomes - consumptions

def _get_net_income_month(connection: engine.Connection, meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дату(месяц).
    Расчитывает значение балансовой прибыли, нарастающим итогом.
    Возвращает это значение на начало этой даты(месяца).
    """
    net_income = 0.0
    #Определение к какому кварталу относится дата(месяц)
    #TODO проверить правильность расчета
    if b_date >= date(b_date.year,1, 1) and b_date < date(b_date.year,4, 1):
        net_income = _get_net_income_quater(connection, meta, name, date(b_date.year, 1, 1)) / 4
    if b_date >= date(b_date.year,4, 1) and b_date < date(b_date.year,7, 1):
        net_income = _get_net_income_quater(connection, meta, name, date(b_date.year, 4, 1)) / 4
    if b_date >= date(b_date.year,7, 1) and b_date < date(b_date.year,11, 1):
        net_income = _get_net_income_quater(connection, meta, name, date(b_date.year, 7, 1)) / 4
    if b_date >= date(b_date.year,10, 1) and b_date < date(b_date.year + 1,1, 1):
        net_income=  _get_net_income_quater(connection, meta, name, date(b_date.year, 10, 1)) / 4
    return net_income

def _get_capital(connection: engine.Connection, meta: MetaData,
                    name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение капитала банка на начало этой даты.
    Возвращает это значение.
    """
    #Ассоциация с таблицей f123
    bank = meta.tables['f123']
    #Поиск значения капитала банка
    select_statement = select(bank.c.C3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1 == 000))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def _get_net_assets(connection: engine.Connection, meta: MetaData,
                    name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение чистых активов банка на начало этой даты.
    Возвращает это значение.
    """
    #Расчет капитала банка
    capital = _get_capital(connection, meta, name, b_date)
    #Расчет коэффициента достаточности капитала
    capital_adequacy = reliability_stability._get_capital_adequacy(connection, meta, name, b_date)
    #Расчет значения чистых активов
    value = capital / capital_adequacy
    return value

def _get_capital_profitability(connection: engine.Connection, meta: MetaData,
                                name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение коэффициента рентабельности капитала на начало этой даты.
    Возвращает это значение.
    """
    #Расчет капитала банка.
    capital  = _get_capital(connection, meta, name,b_date)
    #Расчет балансовой прибыли.
    net_income = _get_net_income_month(connection, meta, name,b_date)
    #Расчет кол-во дней прошедших с начала года на начало этой даты.
    day_in_year = b_date.timetuple().tm_yday
    #Расчет коэффициента рентабельности капитала.
    value = net_income * 360 * 100 / (capital * day_in_year)
    return value

def _get_return_on_assets(connection: engine.Connection, meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение коэффициент рентабельности активов на начало этой даты.
    Возвращает это значение.
    """
    #Расчет значения чистых активов
    net_assets = _get_net_assets(connection, meta, name,b_date)
    #Расчет значения балансовой прибыли
    net_income = _get_net_income_month(connection, meta, name,b_date)
    #Расчет кол-во дней прошедших с начала года на начало этой даты.
    day_in_year = b_date.timetuple().tm_yday
    #Расчет коэффициента рентабельности активов.
    value = net_income * 360 * 100 / (net_assets * day_in_year)
    return value

def get_efficiency(connection: engine.Connection,meta: MetaData, name: str, b_date: date)->list:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и дата(месяц).
    Расчитывает значение коэффициентов эффективности на начало этой даты.
    Возвращает список этих значений
    """
    capital_profitability = _get_capital_profitability(connection, meta, name,b_date)
    return_on_assets =  _get_return_on_assets(connection, meta, name,b_date)
    return [capital_profitability, return_on_assets]
