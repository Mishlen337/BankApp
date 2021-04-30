"""
Gets mart from database
"""
from datetime import date
from sqlalchemy import engine, MetaData, select, and_
from bank_analize import config
from bank_analize.data_mart.form_mart import _parse_date, _parse_gap_dates

def _convert_report(report: list)->list:
    """
    Recieves list report from database, which items are tuples.
    Return list of converted to list items.
    """
    list_report = []
    for line in report:
        list_report.append(list(line))
    return list_report

def _convert_dates(list_report: list)->list:
    """
    Recieves list report from database, which items are lists.
    Return list of converted dates for report.
    """
    for line in list_report:
        line[0] = date(line[0].year, line[0].month-1, line[0].day).strftime('%m.%Y')
    return list_report

def _report_bank_list_mart(connection: engine.Connection, meta: MetaData,
                            names: list, db_date: date):
    """
    Recieves database engine, connection, meta data, ratios, list of banks and
    particular date of the ratio.
    Returns mart from database.
    """
    table_mart = meta.tables[config.mart_name]
    table_req = meta.tables['req']
    select_statement = select(table_mart.c.date, table_req.c.NAME_B,
                                table_mart.c.CA, table_mart.c.LR,
                                table_mart.c.CR, table_mart.c.LTR,
                                table_mart.c.CP,table_mart.c.ROA).\
                        filter(and_(table_mart.c.date == db_date,
                                    table_req.c.index == table_mart.c.bank_index,
                                    table_req.c.NAME_B.in_(names)))
    report = connection.execute(select_statement).fetchall()
    return report

def _report_bank_mart(connection: engine.Connection, meta: MetaData,
                        name: str, db_dates: list):
    """
    Recieves database engine, connection, meta data, ratios, bank name and
    start and end dates of the ratio.
    Returns mart from database.
    """
    table_mart = meta.tables[config.mart_name]
    table_req = meta.tables['req']
    select_statement = select(table_mart.c.date, table_req.c.NAME_B,
                                table_mart.c.CA, table_mart.c.LR,
                                table_mart.c.CR, table_mart.c.LTR,
                                table_mart.c.CP,table_mart.c.ROA).\
                        filter(and_(table_mart.c.date.in_(db_dates),
                                    table_req.c.index == table_mart.c.bank_index,
                                    table_req.c.NAME_B == name))
    report = connection.execute(select_statement).fetchall()
    return report
def _sort_report_date(report: list)->list:
    """
    Recieves report list.
    Returns sorted list by date.
    """
    sorted_report = sorted(report, key = lambda x: x[0])
    return sorted_report

def _sort_report_name(report:list)->list:
    """
    Recieves report list.
    Returns sorted list by name.
    """
    sorted_report = sorted(report, key = lambda x: x[1])
    return sorted_report

def get_bank_list_mart(connection: engine.Connection, meta: MetaData,
                        names: list, b_date: str)->list:
    """
    Recieves database engine, connection, meta data, ratios, list of banks and
    particular date of the ratio.
    Returns transformed to acceptable form mart from database.
    """
    db_date = _parse_date(b_date)
    report = _report_bank_list_mart(connection, meta, names, db_date)
    #Deleting dublicates
    uniqued_report = list(set(report))
    converted_report = _convert_report(uniqued_report)
    converted_date_report = _convert_dates(converted_report)
    return _sort_report_name(converted_date_report)

def get_bank_mart(connection: engine.Connection, meta: MetaData,
                    name: str, start_date: str, end_date: str):
    """
    Recieves database engine, connection, meta data, ratios, list of banks and
    particular date of the ratio.
    Returns transformed to acceptable form mart from database.
    """
    db_dates = _parse_gap_dates(start_date, end_date)
    report = _report_bank_mart(connection, meta, name, db_dates)
    #Deleting dublicates
    uniqued_report = list(set(report))
    converted_report = _convert_report(uniqued_report)
    converted_date_report = _convert_dates(converted_report)
    return _sort_report_date(converted_date_report)
