# -*- coding: utf-8 -*-
"""
Модуль для соединения с базой данной и формирования и извелечения витрины данных.
"""
import sys
sys.path.insert(0, '.')
from sqlalchemy import create_engine, MetaData
import config
from queries.data_mart.bank_list import form_bank_list, get_bank_list
from queries.data_mart.bank import form_bank, get_bank
from queries.calculate import get_names


def bank_query(bank: str, start_date: str, end_date: str) -> list:
    """
    Аргументы: имя банка и начальная и конечная дата(месяцев) в виде строк.
    Подсоединяется к бд, формирует витрину бд и возвращает
    сортированный по времени список с датами, названием банка и коэффициентами
    из витрины данных.
    """
    # Подсоединение к бд
    engine = create_engine(
        config.bank_db_connection)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        # Формирует витрину
        form_bank.form_bank_mart(
            engine, conn, meta, bank, start_date, end_date)
        # Берет из витрины дынные
        return get_bank.get_bank_mart(conn, meta, bank, start_date, end_date)


def bank_list_query(bank_list: list, b_date: str):
    """
    Аргументы: соединение с бд, метаданные бд, список банков и дата(месяц)
    в виде строк.
    Возвращает сортированный по времени список с датами, названием банка и
    коэффициентами из витрины данных.
    """
    # Подсоединение к бд
    engine = create_engine(
        config.bank_db_connection)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        # Формирует витрину
        form_bank_list.form_bank_list_mart(
            engine, conn, meta, bank_list, b_date)
        # Берет из витрины дынные
        return get_bank_list.get_bank_list_mart(conn, meta, bank_list, b_date)


def bank_names_query() -> list:
    """
    Подсоединяется к бд и берет от туда список наименований банков
    """
    # Подсоединение к бд
    engine = create_engine(
        config.bank_db_connection)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        # Берет список наименований банков
        return get_names.get_bank_names(conn, meta)
