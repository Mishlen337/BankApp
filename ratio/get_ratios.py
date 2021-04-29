# -*- coding: utf-8 -*-
from ratio.efficiency import get_efficiency
from ratio.reliability_stability import get_reliability_stability
from sqlalchemy import engine, MetaData
from datetime import date

def get_bank_ratios(connection: engine.Connection, meta: MetaData, name: str, b_dates: list)->list:
    """Получает на вход имя банка, начальную и конечную дату.
        Возвращает список коэффициентов надежности и эффективности"""
    bank_ratios = {}
    for b_date in b_dates:
        bank_ratios[b_date] = get_reliability_stability(connection, meta, name, b_date) +\
                            get_efficiency(connection, meta, name, b_date)
    return bank_ratios

def get_bank_list_ratios(connection: engine.Connection, meta: MetaData, names:list, b_date:date)->dict:
    bank_list_ratios = {}
    for name in names:
        bank_list_ratios[name] = get_reliability_stability(connection, meta, name, b_date) +\
                                    get_efficiency(connection, meta, name, b_date)
    return bank_list_ratios
#print(get_bank_ratio('ПАО Сбербанк', datetime.strptime("01.01.2018", "%d.%m.%Y"), datetime.strptime("01.02.2018", "%d.%m.%Y")))