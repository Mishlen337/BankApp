"""from datetime """
from datetime import date
from sqlalchemy import create_engine, MetaData, Table, select,Column,Float, String, UniqueConstraint, DATETIME, and_
from bank_analize import config
from bank_analize.ratio.get_ratios import get_bank_ratios, get_bank_list_ratios
from bank_analize.data_mart.form_mart import form_bank_list, form_bank
from bank_analize.data_mart import get_mart
engine = create_engine(
    config.bank_db_path)
meta = MetaData()
meta.reflect(engine)
with engine.connect() as conn:
    #print(get_bank_ratios(conn, meta, 'ПАО Сбербанк', datetime.strptime("01.01.2018", "%d.%m.%Y"), datetime.strptime("01.02.2018", "%d.%m.%Y")))
    #print(get_bank_list_ratios(conn, meta, ['ПАО Сбербанк', 'АО ЮниКредит Банк'], datetime.strptime("01.01.2018","%d.%m.%Y")))
    form_bank_list(engine, conn, meta, ['АО "Тинькофф Банк"', 'АО ЮниКредит Банк'], "05.2018")
    print("Report")
    print(get_mart.get_bank_list_mart(conn, meta, ['АО "Тинькофф Банк"', 'АО ЮниКредит Банк'], "05.2018"))

    #form_bank(engine, conn, meta, 'АО "МАЙКОПБАНК"', "01.2018", "07.2018")
    #print("Report")
    #print(get_mart.get_bank_mart(conn, meta, 'АО "МАЙКОПБАНК"', "01.2018", "07.2018"))