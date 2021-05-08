# -*- coding: utf-8 -*-
from sqlalchemy import engine, MetaData, select

def _bank_names_list(names:list)->list:
    """
    Recieves list of taples of bank names.
    Returns list of bank names.
    """
    names_list = [i[0] for i in names]
    return names_list

def _sort_bank_names(names:list)->list:
    """
    Recieves list of bank names.
    Returns list of sorted bank names.
    """
    sorted_names = sorted(names)
    return sorted_names

def get_bank_names(connection: engine.Connection, meta: MetaData):
    """
    Recieves database connection and metadata.
    Returns ascending sorted bank names from database.
    """
    table_req = meta.tables['req']
    select_statement = select(table_req.c.NAME_B)
    result = connection.execute(select_statement)
    bank_names = result.fetchall()
    bank_names_list = _bank_names_list(bank_names)
    #Deleting dublicates
    unique_bank_names = list(set(bank_names_list))
    sorted_bank_names = _sort_bank_names(unique_bank_names)
    return sorted_bank_names