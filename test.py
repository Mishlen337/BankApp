"""from datetime """
from datetime import date
from sqlalchemy import create_engine, MetaData, Table, select,Column,Float, String, UniqueConstraint, DATETIME, and_
import config
from ratio.get_ratios import get_bank_ratios, get_bank_list_ratios
from data_mart.form_mart import form_bank_list, form_bank
engine = create_engine(
    config.bank_db_path)
meta = MetaData()
meta.reflect(engine)
with engine.connect() as conn:
    #print(get_bank_ratios(conn, meta, 'ПАО Сбербанк', datetime.strptime("01.01.2018", "%d.%m.%Y"), datetime.strptime("01.02.2018", "%d.%m.%Y")))
    #print(get_bank_list_ratios(conn, meta, ['ПАО Сбербанк', 'АО ЮниКредит Банк'], datetime.strptime("01.01.2018","%d.%m.%Y")))
    form_bank_list(engine, conn, meta, ['АО "БКС Банк"','ПАО "Торжокуниверсалбанк"'], "01.2018")
    
    #form_bank(engine, conn, meta, 'АО "БКС Банк"', "01.2018", "07.2018")
    #['АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"', 'АО "БКС Банк"']
    #print(set([date(2018, 2, 1), date(2018, 3, 1), date(2018, 4, 1), date(2018, 5, 1), date(2018, 6, 1)]).difference([date(2018, 2, 1),date(2018, 6, 1)]))
