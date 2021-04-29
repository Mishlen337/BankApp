# -*- coding: utf-8 -*-
from ratio.reliability_stability import get_capital_adequacy
from datetime import date
from sqlalchemy import engine, MetaData, select, and_

def get_efficiency(connection: engine.Connection,meta: MetaData, name: str, b_date: date)->list:
    capital_profitability = get_capital_profitability(connection, meta, name,b_date)
    return_on_assets =  get_return_on_assets(connection, meta, name,b_date)  
    return [capital_profitability, return_on_assets]

def get_net_income_quater(connection: engine.Connection, meta: MetaData, name: str, b_date: date)->float:
    """Расчет балансовой прибыли за квартал"""
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

def get_net_income_month(connection: engine.Connection, meta: MetaData, name: str, b_date: date)->float:
    """Расчет балансовой прибыли за квартал"""

    """Возврат значения средней чистой прибыли за месяц для 1 квартала"""
    if b_date >= date(b_date.year,1, 1) and b_date < date(b_date.year,4, 1):
        return get_net_income_quater(connection, meta, name, date(b_date.year, 1, 1)) / 4 

    """Возврат значения средней чистой прибыли за месяц для 2 квартала"""
    if b_date >= date(b_date.year,4, 1) and b_date < date(b_date.year,7, 1):
        return get_net_income_quater(connection, meta, name, date(b_date.year, 4, 1)) / 4

    """Возврат значения средней чистой прибыли за месяц для 3 квартала"""
    if b_date >= date(b_date.year,7, 1) and b_date < date(b_date.year,11, 1):
        return get_net_income_quater(connection, meta, name, date(b_date.year, 7, 1)) / 4

    """Возврат значения средней чистой прибыли за месяц для 3 квартала"""
    if b_date >= date(b_date.year,10, 1) and b_date < date(b_date.year + 1,1, 1):
        return get_net_income_quater(connection, meta, name, date(b_date.year, 10, 1)) / 4

def get_capital(connection: engine.Connection, meta: MetaData, name: str, b_date: date)->float:
    """Капитал банка"""
    bank = meta.tables['f123']
    select_statement = select(bank.c.C3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1 == 000))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def get_net_assets(connection: engine.Connection, meta: MetaData, name: str, b_date: date)->float:
    """Чистые активы банка"""
    capital = get_capital(connection, meta, name,b_date)
    capital_adequacy = get_capital_adequacy(connection, meta, name, b_date)
    value = capital / capital_adequacy
    return value

def get_capital_profitability(connection: engine.Connection, meta: MetaData, name: str, b_date: date)->float:
    """Коэффициент рентабельности капитала"""
    capital  = get_capital(connection, meta, name,b_date)
    net_income = get_net_income_month(connection, meta, name,b_date)
    day_in_year = b_date.timetuple().tm_yday
    value = net_income * 360 * 100 / (capital * day_in_year)
    return value

def get_return_on_assets(connection: engine.Connection, meta: MetaData, name: str, b_date: date)->float:
    """Коэффициент рентабельности активов"""
    net_assets = get_net_assets(connection, meta, name,b_date)
    net_income = get_net_income_month(connection, meta, name,b_date)
    day_in_year = date(b_date.year, b_date.month + 1, b_date.day).timetuple().tm_yday
    value = net_income * 360 * 100 / (net_assets * day_in_year)
    return value
    
#print(get_return_on_assets('ПАО Сбербанк', datetime.strptime("01.01.2018", "%d.%m.%Y")))
#print(get_capital('АО ЮниКредит Банк', datetime.strptime("01.02.2018", "%d.%m.%Y")))
#print(get_net_assets('ПАО Сбербанк', datetime.strptime("01.02.2018", "%d.%m.%Y")))
