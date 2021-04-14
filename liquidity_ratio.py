# -*- coding: utf-8 -*-
from sqlalchemy import *
from datetime import datetime
import config


def get_highly_liquid_assets(name: str, date: datetime):
    highly_liquid_assets = 0
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f101', meta, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(select(bank.c.NUM_SC, bank.c.IITG).filter(and_(bank.c.NAME_B.contains(name),
                                                                             bank.c.DT == date, or_(bank.c.NUM_SC.contains(202), bank.c.NUM_SC == 30102,
                                                                                                    bank.c.NUM_SC == 30104, bank.c.NUM_SC == 30106, bank.c.NUM_SC == 30110,
                                                                                                    bank.c.NUM_SC == 30114, bank.c.NUM_SC == 30118, bank.c.NUM_SC == 30119,
                                                                                                    bank.c.NUM_SC == 30125, bank.c.NUM_SC == 30128, bank.c.NUM_SC == 31902,
                                                                                                    bank.c.NUM_SC == 32001, bank.c.NUM_SC == 32002, bank.c.NUM_SC == 32101,
                                                                                                    bank.c.NUM_SC == 32102, bank.c.NUM_SC == 32202, bank.c.NUM_SC == 32302,
                                                                                                    bank.c.NUM_SC == 60347, bank.c.NUM_SC == 60350, bank.c.NUM_SC == 60343,
                                                                                                    bank.c.NUM_SC == 60341, bank.c.NUM_SC == 60339, bank.c.NUM_SC == 60337,
                                                                                                    bank.c.NUM_SC == 60336, bank.c.NUM_SC == 60323, bank.c.NUM_SC == 60315,
                                                                                                    bank.c.NUM_SC == 60314, bank.c.NUM_SC == 60312, bank.c.NUM_SC == 60310,
                                                                                                    bank.c.NUM_SC == 60308, bank.c.NUM_SC == 60306, bank.c.NUM_SC == 60302,
                                                                                                    bank.c.NUM_SC == 60351))))
        rows = result.fetchall()
        negative_contribution = [30128, 60351]
        for count in rows:
            if int(count[0]) in negative_contribution:
                highly_liquid_assets -= count[1]
            else:
                highly_liquid_assets += count[1]
        return highly_liquid_assets


def get_on_call_liabilities(name: str, date: datetime):
    on_call_liabilities = 0
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f101', meta, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(select(bank.c.NUM_SC, bank.c.IITG).filter(and_(bank.c.NAME_B.contains(name),
                                                                             bank.c.DT == date, or_(bank.c.NUM_SC == 31210, bank.c.NUM_SC == 31213, bank.c.NUM_SC == 31310,
                                                                                                    bank.c.NUM_SC == 31410, bank.c.NUM_SC == 31501, bank.c.NUM_SC == 31601, bank.c.NUM_SC == 31501,
                                                                                                    bank.c.NUM_SC == 31601, bank.c.NUM_SC == 31210, bank.c.NUM_SC == 31213, bank.c.NUM_SC == 31310,
                                                                                                    bank.c.NUM_SC == 31410, bank.c.NUM_SC == 31501, bank.c.NUM_SC == 31601, bank.c.NUM_SC == 41001,
                                                                                                    bank.c.NUM_SC == 41101, bank.c.NUM_SC == 41201, bank.c.NUM_SC == 41301, bank.c.NUM_SC == 41401,
                                                                                                    bank.c.NUM_SC == 41501, bank.c.NUM_SC == 41601, bank.c.NUM_SC == 41701, bank.c.NUM_SC == 41801,
                                                                                                    bank.c.NUM_SC == 41901, bank.c.NUM_SC == 42001, bank.c.NUM_SC == 42101, bank.c.NUM_SC == 42108,
                                                                                                    bank.c.NUM_SC == 42201, bank.c.NUM_SC == 42301, bank.c.NUM_SC == 42309, bank.c.NUM_SC == 42501,
                                                                                                    bank.c.NUM_SC == 42601, bank.c.NUM_SC == 42609, bank.c.NUM_SC == 42701, bank.c.NUM_SC == 42801,
                                                                                                    bank.c.NUM_SC == 42901, bank.c.NUM_SC == 43001, bank.c.NUM_SC == 43101, bank.c.NUM_SC == 43201,
                                                                                                    bank.c.NUM_SC == 43301, bank.c.NUM_SC == 43401, bank.c.NUM_SC == 43501, bank.c.NUM_SC == 43601,
                                                                                                    bank.c.NUM_SC == 43701, bank.c.NUM_SC == 43801, bank.c.NUM_SC == 43901, bank.c.NUM_SC == 43901,
                                                                                                    bank.c.NUM_SC == 44001, bank.c.NUM_SC == 41001, bank.c.NUM_SC == 41101, bank.c.NUM_SC == 41201,
                                                                                                    bank.c.NUM_SC == 41301, bank.c.NUM_SC == 41401, bank.c.NUM_SC == 41501, bank.c.NUM_SC == 41601,
                                                                                                    bank.c.NUM_SC == 41701, bank.c.NUM_SC == 41801, bank.c.NUM_SC == 41901, bank.c.NUM_SC == 42001,
                                                                                                    bank.c.NUM_SC == 42101, bank.c.NUM_SC == 42108, bank.c.NUM_SC == 42701, bank.c.NUM_SC == 42801,
                                                                                                    bank.c.NUM_SC == 42901, bank.c.NUM_SC == 43001, bank.c.NUM_SC == 43101, bank.c.NUM_SC == 43201,
                                                                                                    bank.c.NUM_SC == 43301, bank.c.NUM_SC == 43401, bank.c.NUM_SC == 43501, bank.c.NUM_SC == 43601,
                                                                                                    bank.c.NUM_SC == 30109, bank.c.NUM_SC == 30111, bank.c.NUM_SC == 30116, bank.c.NUM_SC == 30117,
                                                                                                    bank.c.NUM_SC == 30122, bank.c.NUM_SC == 30123, bank.c.NUM_SC == 30126, bank.c.NUM_SC == 30129,
                                                                                                    bank.c.NUM_SC == 60301, bank.c.NUM_SC == 60305, bank.c.NUM_SC == 60307, bank.c.NUM_SC == 60309,
                                                                                                    bank.c.NUM_SC == 60311, bank.c.NUM_SC == 60313, bank.c.NUM_SC == 60320, bank.c.NUM_SC == 60322,
                                                                                                    bank.c.NUM_SC == 60324, bank.c.NUM_SC == 60335, bank.c.NUM_SC == 60338, bank.c.NUM_SC == 60340,
                                                                                                    bank.c.NUM_SC == 60342, bank.c.NUM_SC == 60344, bank.c.NUM_SC == 60349, bank.c.NUM_SC == 60352))))
        rows = result.fetchall()
        negative_contribution = [60324, 30126, 60352]
        for count in rows:
            if int(count[0]) in negative_contribution:
                on_call_liabilities -= count[1]
            else:
                on_call_liabilities += count[1]
        return on_call_liabilities


def get_capital_adequacy(name: str, date: datetime) -> int:
    """ Коэффициент мгновенной ликвидности
    Получает на вход имя банка и время, возвращает коэфициент, выраженный в целочисленных процентах  
    LRm = LAm / Lc 
    где: LAm - высоколиквидные активы
    Lc - обязательства до востребования """
    highly_liquid_assets = get_highly_liquid_assets(name, date)
    on_call_liabilities = get_on_call_liabilities(name, date)
    return int(highly_liquid_assets/on_call_liabilities*100)

#print(get_capital_adequacy('Тинькофф',datetime.strptime("01.01.2018", "%d.%m.%Y")))
