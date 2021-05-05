"""from datetime """
from datetime import date
from sqlalchemy import create_engine, MetaData, Table, select,Column,Float, String, UniqueConstraint, DATETIME, and_
from bank_analize import config
from bank_analize.ratio.get_ratios import get_bank_ratios, get_bank_list_ratios
from bank_analize.data_mart.form_mart import form_bank_list, form_bank
from bank_analize.data_mart import get_mart
from bank_analize import db_names
def bank_query(bank: str, start_date: str, end_date: str):
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        #print(get_bank_ratios(conn, meta, 'ПАО Сбербанк', datetime.strptime("01.01.2018", "%d.%m.%Y"), datetime.strptime("01.02.2018", "%d.%m.%Y")))
        #print(get_bank_list_ratios(conn, meta, ['ПАО Сбербанк', 'АО ЮниКредит Банк'], datetime.strptime("01.01.2018","%d.%m.%Y")))
        #form_bank_list(engine, conn, meta, ['АО "Тинькофф Банк"', 'АО ЮниКредит Банк'], "05.2018")
        #print("Report")
        #return get_mart.get_bank_list_mart(conn, meta, ['АО "Тинькофф Банк"', 'АО ЮниКредит Банк'], "05.2018")

        form_bank(engine, conn, meta, bank, start_date, end_date)
        #print("Report")
        return get_mart.get_bank_mart(conn, meta, bank, start_date, end_date)

def bank_list_query(bank_list: list, b_date: str):
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        #print(get_bank_ratios(conn, meta, 'ПАО Сбербанк', datetime.strptime("01.01.2018", "%d.%m.%Y"), datetime.strptime("01.02.2018", "%d.%m.%Y")))
        #print(get_bank_list_ratios(conn, meta, ['ПАО Сбербанк', 'АО ЮниКредит Банк'], datetime.strptime("01.01.2018","%d.%m.%Y")))
        form_bank_list(engine, conn, meta, bank_list, b_date)
        #print("Report")
        return get_mart.get_bank_list_mart(conn, meta, bank_list, b_date)

def bank_names_query():
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData()
    meta.reflect(engine)
    with engine.connect() as conn:
        names = db_names.get_bank_names(conn, meta)
        names_list = [i[0] for i in names]
        return list(set(names_list))