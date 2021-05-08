# -*- coding: utf-8 -*-
"""
Module to connect to database and extract data.
"""
from sqlalchemy import create_engine, MetaData
from bank_analize import config
from bank_analize.data_mart.form_mart import form_bank_list, form_bank
from bank_analize.data_mart import get_mart
from bank_analize import db_names

def bank_query(bank: str, start_date: str, end_date: str)->list:
    """
    Recieves name of the bank, start and end date of report.
    Connects to database and returns report for one particular bank.
    """
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        form_bank(engine, conn, meta, bank, start_date, end_date)
        return get_mart.get_bank_mart(conn, meta, bank, start_date, end_date)

def bank_list_query(bank_list: list, b_date: str):
    """
    Recieves list of names of the bank and date of the report.
    Connects to database and returns report for list of banks on particular date.
    """
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        form_bank_list(engine, conn, meta, bank_list, b_date)
        return get_mart.get_bank_list_mart(conn, meta, bank_list, b_date)

def bank_names_query()->list:
    """Connects to database and returns list of bank names in database."""
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        return db_names.get_bank_names(conn, meta)
