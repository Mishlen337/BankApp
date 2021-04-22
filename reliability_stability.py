# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, select, and_
import config
def get_reliability_stability(name: str, date: datetime)->tuple:
    """Расчет коэффициентов надежности и устойчивости банка""" 
    capital_adequacy = get_capital_adequacy(name, date)
    liquidity_ratio = get_liquidity_ratio(name, date)
    current_ratio = get_current_ratio(name, date)
    longterm_ratio = get_longterm_ratio(name, date)
    #TODO рассчитать коэффициент интенсивности проведения платежей в РКЦ 
    return capital_adequacy, liquidity_ratio, current_ratio,longterm_ratio

def get_capital_adequacy(name: str, date: datetime)->float:
    """Коэффициент достаточности капитала"""
    engine = create_engine(
       config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f135', meta, autoload_with=engine)
    with engine.connect() as conn:
        select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                    bank.c.DT == date, bank.c.C1_3 == "Н1.0"))
        result = conn.execute(select_statement)
        value = result.fetchone()[0]
        return value

def get_liquidity_ratio(name: str, date: datetime)->float:
    """Коэффициент достаточности капитала"""
    engine = create_engine(
       config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f135', meta, autoload_with=engine)
    with engine.connect() as conn:
        select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                    bank.c.DT == date, bank.c.C1_3 == "Н2"))
        result = conn.execute(select_statement)
        value = result.fetchone()[0]
        return value

def get_current_ratio(name: str, date: datetime)->float:
    """Коэффициент текущей ликвидности"""
    engine = create_engine(
       config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f135', meta, autoload_with=engine)
    with engine.connect() as conn:
        select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                    bank.c.DT == date, bank.c.C1_3 == "Н3"))
        result = conn.execute(select_statement)
        value = result.fetchone()[0]
        return value

def get_longterm_ratio(name: str, date: datetime)->float:
    """Коэффициент долгосрочной ликвидности"""
    engine = create_engine(
       config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f135', meta, autoload_with=engine)
    with engine.connect() as conn:
        select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                    bank.c.DT == date, bank.c.C1_3 == "Н4"))
        result = conn.execute(select_statement)
        value = result.fetchone()[0]
        return value

#TODO функция коэффициента интенсивности проведения платежей в РКЦ
        
#print(get_reliability_stability('АО ЮниКредит Банк', datetime.strptime("01.01.2018", "%d.%m.%Y")))