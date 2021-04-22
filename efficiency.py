# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, select, and_
import config
import reliability_stability

def get_net_income(name: str, date: datetime)->float:
    """Расчет балансовой прибыли"""
    engine = create_engine(
       config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f102', meta, autoload_with=engine)
    with engine.connect() as conn:
        #Поиск доходов
        select_statement = select(bank.c.SIM_ITOGO).filter(and_(bank.c.NAME_B == name,
                                    bank.c.DT == date, bank.c.CODE == 19999))
        result = conn.execute(select_statement)
        incomes = result.fetchone()[0]
        #Поиск расходов
        select_statement = select(bank.c.SIM_ITOGO).filter(and_(bank.c.NAME_B == name,
                                    bank.c.DT == date, bank.c.CODE == 29999))
        result = conn.execute(select_statement)
        consumptions = result.fetchone()[0]
        return incomes - consumptions

def get_capital(name: str, date: datetime)->float:
    """Капитал банка"""
    engine = create_engine(
       config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f123', meta, autoload_with=engine)
    with engine.connect() as conn:
        select_statement = select(bank.c.C3).filter(and_(bank.c.NAME_B == name,
                                    bank.c.DT == date, bank.c.C1 == 000))
        result = conn.execute(select_statement)
        value = result.fetchone()[0]
        return value

def get_net_assets(name: str, date: datetime)->float:
    """Чистые активы банка"""
    capital = get_capital(name, date)
    capital_adequacy = reliability_stability.get_capital_adequacy(name, date)
    value = capital / capital_adequacy
    return value

def get_capital_profitability(name: str, date: datetime)->float:
    """Коэффициент достаточности капитала"""
    #TODO рассчитать коэффициент достаточности капитала
    pass

def get_return_on_assets(name: str, date: datetime)->float:
    """Коэффициент рентабельности активов"""
    #TODO рассчитать коэффициент достаточности капитала
    pass

#print(get_net_income('ПАО Сбербанк', datetime.strptime("01.07.2018", "%d.%m.%Y")))
#print(get_capital('АО ЮниКредит Банк', datetime.strptime("01.02.2018", "%d.%m.%Y")))
#print(get_net_assets('ПАО Сбербанк', datetime.strptime("01.02.2018", "%d.%m.%Y")))