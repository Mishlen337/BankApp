# -*- coding: utf-8 -*-
"""
Расчет коэффициентов надежности и эффективности.
"""
import sys
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
from datetime import date
from sqlalchemy import engine, MetaData
from queries.calculate.ratios import reliability_stability, efficiency

def get_bank_ratios(connection: engine.Connection, meta: MetaData,
                        name: str, b_dates: list)->list:
    """
    Аргументы: соединение с бд, метаданные бд, имя банка и промежуток дат в виде списка на начало месяца.
    Расчитывает коэффициенты надежности и эффективности для банка. 
    Возвращает словарь. Ключи - даты из промежутка.
    Значения - список расчитанных коэффициентов за эту дату.
    """
    bank_ratios = {}
    #Расчитывает коэффициенты для каждой даты
    for b_date in b_dates:
        bank_ratios[b_date] = reliability_stability.get_reliability_stability(connection, meta, name, b_date) +\
                            efficiency.get_efficiency(connection, meta, name, b_date)
    return bank_ratios

def get_bank_list_ratios(connection: engine.Connection, meta: MetaData,
                            names:list, b_date:date)->dict:
    """
    Аргументы: соединение с бд, метаданные бд, список имен банков и дата на начало месяца.
    Расчитывает коэффициенты надежности и эффективности для списка банков. 
    Возвращает словарь. Ключи - банки из списка.
    Значения - список расчитанных коэффициентов за дату.
    """
    bank_list_ratios = {}
    #Расчитывает коэффициенты для каждого банка
    for name in names:
        bank_list_ratios[name] = reliability_stability.get_reliability_stability(connection, meta, name, b_date) +\
                                efficiency.get_efficiency(connection, meta, name, b_date)
    return bank_list_ratios
