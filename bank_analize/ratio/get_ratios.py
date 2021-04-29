# -*- coding: utf-8 -*-
"""
Getting calculated ratios
"""
from datetime import date
from sqlalchemy import engine, MetaData
from bank_analize.ratio.efficiency import get_efficiency
from bank_analize.ratio.reliability_stability import get_reliability_stability

def get_bank_ratios(connection: engine.Connection, meta: MetaData,
                        name: str, b_dates: list)->list:
    """
    Recieves database connection, meta data, name of the bank, and list of dates of the ratio.
    Returns list of ratios of the bank in list of times.
    """
    bank_ratios = {}
    for b_date in b_dates:
        bank_ratios[b_date] = get_reliability_stability(connection, meta, name, b_date) +\
                            get_efficiency(connection, meta, name, b_date)
    return bank_ratios

def get_bank_list_ratios(connection: engine.Connection, meta: MetaData,
                            names:list, b_date:date)->dict:
    """
    Recieves database connection, meta data, list of names of the bank, and date of the ratio.
    Returns list of ratios of list of banks in paticular time.
    """
    bank_list_ratios = {}
    for name in names:
        bank_list_ratios[name] = get_reliability_stability(connection, meta, name, b_date) +\
                                    get_efficiency(connection, meta, name, b_date)
    return bank_list_ratios
