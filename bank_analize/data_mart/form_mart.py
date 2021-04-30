# -*- coding: utf-8 -*-
#!/usr/bin/env/ python3
"""
Forms mart in database.
"""
from datetime import date, datetime
from sqlalchemy import engine, Table, Column, Float, INT, Date, MetaData, select,\
                        UniqueConstraint, and_
from bank_analize import config
from bank_analize.ratio.get_ratios import get_bank_list_ratios, get_bank_ratios

def _check_mart_existence(db_engine: engine, meta: MetaData)->bool:
    """
    Recieves engine and metadate.
    Creates table in database if it is not excisted.
    """
    if not config.mart_name in meta.tables:
        b_date = Column('date', Date)
        bank_index = Column('bank_index', INT)
        capital_adequacy = Column('CA', Float)
        liquidity_ratio = Column('LR', Float)
        current_ratio = Column('CR', Float)
        longterm_ratio = Column('LTR', Float)
        capital_profitability = Column('CP', Float)
        return_on_assets = Column ('ROA', Float)
        unique_fields = UniqueConstraint(b_date, bank_index)
        Table(config.mart_name, meta, b_date, bank_index, capital_adequacy,\
                liquidity_ratio, current_ratio,longterm_ratio, capital_profitability,\
                return_on_assets, unique_fields)
        meta.create_all(db_engine)

def _insert_bank_list(connection: engine.Connection, meta: MetaData, ratios: dict, b_date: date):
    """
    Recieves database connection, meta data, ratios, and particular date of the ratio.
    Inserts data of bank list to database mart.
    """
    table_mart = meta.tables[config.mart_name]
    table_req = meta.tables['req']
    for name in ratios:
        select_statement = select(table_req.c.index).filter(table_req.c.NAME_B == name)
        result = connection.execute(select_statement)
        bank_index = result.fetchone()[0]
        insert_statement = table_mart.\
                            insert().values(bank_index = bank_index, date = b_date,
                                            CA = ratios[name][0], LR = ratios[name][1],
                                            CR = ratios[name][2], LTR = ratios[name][3],
                                            CP = ratios[name][4], ROA = ratios[name][5])
        connection.execute(insert_statement)

def _insert_bank(connection: engine.Connection, meta: MetaData, ratios: dict, name: str):
    """
    Recieves database connection, meta data, ratios, and name of the bank.
    Inserts data of the bank to database mart.
    """
    table_mart = meta.tables[config.mart_name]
    table_req = meta.tables['req']
    select_statement = select(table_req.c.index).filter(table_req.c.NAME_B == name)
    result = connection.execute(select_statement)
    bank_index = result.fetchone()[0]
    for b_date in ratios:
        insert_statement = table_mart.\
                                    insert().values(bank_index = bank_index, date = b_date,
                                                    CA = ratios[b_date][0], LR = ratios[b_date][1],
                                                    CR = ratios[b_date][2], LTR = ratios[b_date][3],
                                                    CP = ratios[b_date][4], ROA = ratios[b_date][5])
        connection.execute(insert_statement)

def _parse_query(query: list):
    """
    Recieves query from database.
    Returns list of parsed query.
    """
    parsed_query = [i[0] for i in query]
    return parsed_query

def _mart_bank_list(connection: engine.Connection, meta: MetaData,
                        names: list, b_date: date)->dict:
    """
    Recieves database connection, meta data, ratios, list of banks and
    particular date of the ratio. Returns dict - key: bank name, value: calculated ratios for
    particular date, excluding data from database.
    """
    table_mart = meta.tables[config.mart_name]
    table_req = meta.tables['req']
    select_statement = select(table_req.c.NAME_B).\
                        filter(and_(table_mart.c.date == b_date,
                                    table_req.c.index == table_mart.c.bank_index,
                                    table_req.c.NAME_B.in_(names)))
    result = connection.execute(select_statement)
    query = result.fetchall()
    parsed_query = _parse_query(query)
    ratios = get_bank_list_ratios(connection, meta, list(set(names).difference(parsed_query)),
                                                                                b_date)
    return ratios

def _mart_bank(connection: engine.Connection, meta: MetaData, name: str, b_dates: list)->dict:
    """
    Recieves database connection, meta data, ratios, bank and list of dates of the ratio.
    Returns dict - key: date, value: calculated ratios for particular bank,
    excluding data from database.
    """
    table_mart = meta.tables[config.mart_name]
    table_req = meta.tables['req']
    select_statement = select(table_mart.c.date).\
                        filter(and_(table_mart.c.date.in_(b_dates),
                                    table_req.c.index == table_mart.c.bank_index,
                                    table_req.c.NAME_B == name))
    result = connection.execute(select_statement)
    query = result.fetchall()
    parsed_query = _parse_query(query)
    ratios = get_bank_ratios(connection, meta, name, list(set(b_dates).\
                                                        difference(parsed_query)))
    return ratios

def _parse_date(b_date:str)->date:
    """
    Recieves query from database.
    Returns parsed date for database from string.
    """
    formatted_date = datetime.strptime(b_date,"%m.%Y").date()
    db_date = date(formatted_date.year, formatted_date.month + 1, 1)
    return db_date

def _parse_gap_dates(start_date:str, end_date: str)->list:
    """
    Recieves start date and end date.
    Returns list of dates for database
    """
    dates_list = []
    start_db_date = _parse_date(start_date)
    end_db_date = _parse_date(end_date)
    b_date = start_db_date
    delta = 1
    dates_list.append(b_date)
    b_date = date(b_date.year, b_date.month + delta, b_date.day)
    while b_date <= end_db_date:
        dates_list.append(b_date)
        b_date = date(b_date.year, b_date.month + delta, b_date.day)
    return dates_list

def form_bank_list(db_engine: engine, connection: engine.Connection, meta: MetaData,
                    names: list, b_date: str):
    """
    Recieves database engine, connection, meta data, ratios, list of banks and
    particular date of the ratio.
    Forms mart in database.
    """
    db_date = _parse_date(b_date)
    _check_mart_existence(db_engine, meta)
    ratios = _mart_bank_list(connection, meta, names, db_date)
    print("Calculated ratios")
    print(ratios)
    _insert_bank_list(connection, meta, ratios, db_date)

def form_bank(db_engine: engine, connection: engine.Connection, meta: MetaData,
                name: str, start_date: str, end_date: str):
    """Recieves database engine, connection, meta data, ratios,
    bank and list of dates of the ratio.
    Forms mart in database.
    """
    b_dates = _parse_gap_dates(start_date, end_date)
    _check_mart_existence(db_engine, meta)
    ratios = _mart_bank(connection, meta, name, b_dates)
    print("Calculated ratios")
    print(ratios)
    _insert_bank(connection, meta, ratios, name)
        