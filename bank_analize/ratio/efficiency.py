# -*- coding: utf-8 -*-
#!/usr/bin/env/ python3
"""
Calculating effeciency ratios.
"""
from datetime import date
from sqlalchemy import engine, MetaData, select, and_
from bank_analize.ratio.reliability_stability import _get_capital_adequacy

def _get_net_income_quater(connection: engine.Connection, meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns net income in particular quater.
    """
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
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns net income in month
    """
    net_income = 0.0
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
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns capital of the bank in particular month.
    """
    bank = meta.tables['f123']
    select_statement = select(bank.c.C3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1 == 000))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def _get_net_assets(connection: engine.Connection, meta: MetaData,
                    name: str, b_date: date)->float:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns net assets of the bank in particular month.
    """
    capital = _get_capital(connection, meta, name,b_date)
    capital_adequacy = _get_capital_adequacy(connection, meta, name, b_date)
    value = capital / capital_adequacy
    return value

def _get_capital_profitability(connection: engine.Connection, meta: MetaData,
                                name: str, b_date: date)->float:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns capital profitability ratio of the bank in particular month.
    """
    capital  = _get_capital(connection, meta, name,b_date)
    net_income = _get_net_income_month(connection, meta, name,b_date)
    day_in_year = b_date.timetuple().tm_yday
    value = net_income * 360 * 100 / (capital * day_in_year)
    return value

def _get_return_on_assets(connection: engine.Connection, meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns return on assets ratio of the bank in particular month.
    """
    net_assets = _get_net_assets(connection, meta, name,b_date)
    net_income = _get_net_income_month(connection, meta, name,b_date)
    day_in_year = date(b_date.year, b_date.month + 1, b_date.day).timetuple().tm_yday
    value = net_income * 360 * 100 / (net_assets * day_in_year)
    return value

def get_efficiency(connection: engine.Connection,meta: MetaData, name: str, b_date: date)->list:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns list of efficiency ratios of the bank in particular month:
    capital profitability and return on assets.
    """
    capital_profitability = _get_capital_profitability(connection, meta, name,b_date)
    return_on_assets =  _get_return_on_assets(connection, meta, name,b_date)
    return [capital_profitability, return_on_assets]

