# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Calculating reliability and stability ratios.
"""
from datetime import date
from sqlalchemy import engine, MetaData, select, and_

def _get_capital_adequacy(connection: engine.Connection, meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns capital adequacy ratio of the bank in particular time.
    """
    bank = meta.tables['f135']
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н1.0"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def _get_liquidity_ratio(connection: engine.Connection,meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns instant liquidy ratio of the bank in particular time.
    """
    bank = meta.tables['f135']
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н2"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def _get_current_ratio(connection: engine.Connection,meta: MetaData,
                        name: str, b_date: date)->float:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns current liquidy ratio of the bank in particular time.
    """
    bank = meta.tables['f135']
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н3"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def _get_longterm_ratio(connection: engine.Connection,meta: MetaData,
                            name: str, b_date: date)->float:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns longterm liquidy ratio of the bank in particular time.
    """
    bank = meta.tables['f135']
    select_statement = select(bank.c.C2_3).filter(and_(bank.c.NAME_B == name,
                                bank.c.DT == b_date, bank.c.C1_3 == "Н4"))
    result = connection.execute(select_statement)
    value = result.fetchone()[0]
    return value

def get_reliability_stability(connection: engine.Connection,meta: MetaData,
                                name: str, b_date: date)->list:
    """
    Recieves database connection, meta data, name of the bank, and date of the ratio.
    Returns list of reliability and stability ratios of the bank in particular month:
    capital_adequacy, liquidity_ratio, current_ratio and longterm_ratio.
    """
    capital_adequacy = _get_capital_adequacy(connection, meta, name,b_date)
    liquidity_ratio = _get_liquidity_ratio(connection, meta, name,b_date)
    current_ratio = _get_current_ratio(connection, meta, name,b_date)
    longterm_ratio = _get_longterm_ratio(connection, meta, name,b_date)
    return [capital_adequacy, liquidity_ratio, current_ratio,longterm_ratio]

