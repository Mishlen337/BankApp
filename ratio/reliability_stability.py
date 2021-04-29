# -*- coding: utf-8 -*-
import ratio.reliability_stability as reliability_stability
from datetime import date
from sqlalchemy import engine, MetaData, select, and_

def get_reliability_stability(connection: engine.Connection,meta: MetaData, name: str, b_date: date)->list:
    """Расчет коэффициентов надежности и устойчивости банка""" 
    capital_adequacy = get_capital_adequacy(connection, meta, name,b_date)
    liquidity_ratio = get_liquidity_ratio(connection, meta, name,b_date)
    current_ratio = get_current_ratio(connection, meta, name,b_date)
    longterm_ratio = get_longterm_ratio(connection, meta, name,b_date)
    return [capital_adequacy, liquidity_ratio, current_ratio,longterm_ratio]

def get_capital_adequacy(connection: engine.Connection, meta: MetaData, name: str, b_date: date)->float:
    """Коэффициент достаточности капитала"""
    bank = meta.tables['f135']
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н1.0"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def get_liquidity_ratio(connection: engine.Connection,meta: MetaData, name: str, b_date: date)->float:
    """Коэффициент достаточности капитала"""
    bank = meta.tables['f135']
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н2"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def get_current_ratio(connection: engine.Connection,meta: MetaData, name: str, b_date: date)->float:
    """Коэффициент текущей ликвидности"""
    bank = meta.tables['f135']
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н3"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def get_longterm_ratio(connection: engine.Connection,meta: MetaData, name: str, b_date: date)->float:
    """Коэффициент долгосрочной ликвидности"""
    bank = meta.tables['f135']
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н4"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value
#print(get_reliability_stability('ПАО Сбербанк', datetime.strptime("01.01.2018", "%d.%m.%Y")))