# -*- coding: utf-8 -*-
"""
Модуль для авторизации админа и клиента.
"""
import sys
from sqlalchemy import create_engine, MetaData, Table, select
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
import config

def client_verification(username:str, password:str)->bool:
    """
    Аргументы: имя и пароль.
    Проверяет нахождение имени и пароля в таблице клиентов в бд.
    Возвращает булевское значение от этого тезиса.
    """
    engine = create_engine(config.bank_db_connection)
    meta = MetaData()
    client = Table('Client', meta, autoload_with = engine)
    with engine.connect() as conn:
        result = conn.execute(select(client.c.username, client.c.password).\
                where(client.c.username == username, client.c.password == password))
        row = result.fetchone()
        if row:
            return True
        return False

def admin_verification(username:str, password:str)->bool:
    """
    Аргументы: имя и пароль.
    Проверяет нахождение имени и пароля в таблице админов в бд.
    Возвращает булевское значение от этого тезиса.
    """
    engine = create_engine(config.bank_db_connection)
    meta = MetaData()
    client = Table('Admin', meta, autoload_with = engine)
    with engine.connect() as conn:
        result = conn.execute(select(client.c.username, client.c.password).\
                where(client.c.username == username, client.c.password == password))
        row = result.fetchone()
        if row:
            return True
        return False
