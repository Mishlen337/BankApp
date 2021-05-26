import sys
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
import config
from sqlalchemy import engine, Table, Column, Float, INT, Date, MetaData,\
                        UniqueConstraint

def check_mart_existence(db_engine: engine, meta: MetaData)->bool:
    """
    Аргументы: соединение с бд, метаданные бд,
    Создает витрину в бд, если она не создана.
    """
    if not config.mart_name in meta.tables:
        #Создание макета колонок
        b_date = Column('date', Date)
        bank_index = Column('bank_index', INT)
        capital_adequacy = Column('CA', Float)
        liquidity_ratio = Column('LR', Float)
        current_ratio = Column('CR', Float)
        longterm_ratio = Column('LTR', Float)
        capital_profitability = Column('CP', Float)
        return_on_assets = Column ('ROA', Float)
        unique_fields = UniqueConstraint(b_date, bank_index)
        #Создание макета таблицы
        Table(config.mart_name, meta, b_date, bank_index, capital_adequacy,\
                liquidity_ratio, current_ratio,longterm_ratio, capital_profitability,\
                return_on_assets, unique_fields)
        #Применение
        meta.create_all(db_engine)
