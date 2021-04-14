# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import *
import config

def get_bank_own_capital(name: str, date: datetime):
    bank_own_capital = 0
    engine = create_engine(
        config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f101', meta, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(select(bank.c.NUM_SC, bank.c.IITG).filter
                              (and_(bank.c.NAME_B.contains(name),
                                    bank.c.DT == date, or_(bank.c.NUM_SC == 10207, bank.c.NUM_SC == 10208, bank.c.NUM_SC == 10501,
                                                           bank.c.NUM_SC == 10502, bank.c.NUM_SC == 10601, bank.c.NUM_SC == 10602,
                                                           bank.c.NUM_SC == 10603, bank.c.NUM_SC == 10605, bank.c.NUM_SC == 10701,
                                                           bank.c.NUM_SC == 10801, bank.c.NUM_SC == 10901, bank.c.NUM_SC == 70612,
                                                           bank.c.NUM_SC == 70611, bank.c.NUM_SC == 70712, bank.c.NUM_SC == 70711,
                                                           bank.c.NUM_SC == 70601, bank.c.NUM_SC == 70602, bank.c.NUM_SC == 70603,
                                                           bank.c.NUM_SC == 70604, bank.c.NUM_SC == 70605, bank.c.NUM_SC == 70606,
                                                           bank.c.NUM_SC == 70607, bank.c.NUM_SC == 70608, bank.c.NUM_SC == 70609,
                                                           bank.c.NUM_SC == 70610, bank.c.NUM_SC == 70701, bank.c.NUM_SC == 70702,
                                                           bank.c.NUM_SC == 70703, bank.c.NUM_SC == 70704, bank.c.NUM_SC == 70705,
                                                           bank.c.NUM_SC == 70706, bank.c.NUM_SC == 70707, bank.c.NUM_SC == 70708,
                                                           bank.c.NUM_SC == 70709, bank.c.NUM_SC == 70710, bank.c.NUM_SC == 70801,
                                                           bank.c.NUM_SC == 70802))))
    rows = result.fetchall()
    positive_contribution = [10207, 10208, 10601, 10602, 10603, 10701, 10801, 70601, 70602, 70603, 70604,
                             70605, 70701, 70702, 70703, 70704, 70705, 70801]
    negative_contribution = [10501, 10502, 10605, 10901, 70612, 70611, 70712, 70711, 70606, 70607,
                             70608, 70609, 70610, 70706, 70707, 70708, 70709, 70710, 70802]

    for count in rows:
        if int(count[0]) in positive_contribution:
            bank_own_capital += count[1]
        elif int(count[0]) in negative_contribution:
            bank_own_capital -= count[1]
    return bank_own_capital


def get_working_assets(name: str, date: datetime):
    working_assets = 0
    engine = create_engine(
       config.bank_db_path)
    meta = MetaData(schema="bank")
    bank = Table('f101', meta, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(select(bank.c.NUM_SC, bank.c.IITG).filter
                              (and_(bank.c.NAME_B.contains(name),
                                    bank.c.DT == date, or_(bank.c.NUM_SC == 20311, bank.c.NUM_SC == 20312, bank.c.NUM_SC == 20315,
                                                           bank.c.NUM_SC == 20316, bank.c.NUM_SC == 30110, bank.c.NUM_SC == 30114,
                                                           bank.c.NUM_SC == 30118, bank.c.NUM_SC == 30119, bank.c.NUM_SC.contains(
                                                               319),
                                                           bank.c.NUM_SC.contains(320), bank.c.NUM_SC.contains(
                                                               321), bank.c.NUM_SC.contains(322),
                                                           bank.c.NUM_SC.contains(323), bank.c.NUM_SC.contains(
                                                               441), bank.c.NUM_SC.contains(442),
                                                           bank.c.NUM_SC.contains(442), bank.c.NUM_SC.contains(
                                                               444), bank.c.NUM_SC.contains(445),
                                                           bank.c.NUM_SC.contains(446), bank.c.NUM_SC.contains(
                                                               447), bank.c.NUM_SC.contains(448),
                                                           bank.c.NUM_SC.contains(449), bank.c.NUM_SC.contains(
                                                               450), bank.c.NUM_SC.contains(451),
                                                           bank.c.NUM_SC.contains(452), bank.c.NUM_SC.contains(
                                                               453), bank.c.NUM_SC.contains(545),
                                                           bank.c.NUM_SC.contains(455), bank.c.NUM_SC.contains(
                                                               456), bank.c.NUM_SC.contains(457),
                                                           bank.c.NUM_SC.contains(460), bank.c.NUM_SC.contains(
                                                               461), bank.c.NUM_SC.contains(462),
                                                           bank.c.NUM_SC.contains(463), bank.c.NUM_SC.contains(
                                                               464), bank.c.NUM_SC.contains(465),
                                                           bank.c.NUM_SC.contains(466), bank.c.NUM_SC.contains(
                                                               467), bank.c.NUM_SC.contains(468),
                                                           bank.c.NUM_SC.contains(469), bank.c.NUM_SC.contains(
                                                               470), bank.c.NUM_SC.contains(471),
                                                           bank.c.NUM_SC.contains(472), bank.c.NUM_SC.contains(
                                                               473), bank.c.NUM_SC.contains(501),
                                                           bank.c.NUM_SC.contains(502), bank.c.NUM_SC.contains(
                                                               503), bank.c.NUM_SC.contains(506),
                                                           bank.c.NUM_SC.contains(507), bank.c.NUM_SC.contains(
                                                               512), bank.c.NUM_SC.contains(513),
                                                           bank.c.NUM_SC.contains(514), bank.c.NUM_SC.contains(
                                                               515), bank.c.NUM_SC.contains(516),
                                                           bank.c.NUM_SC.contains(517), bank.c.NUM_SC.contains(518), bank.c.NUM_SC.contains(519)))))
    rows = result.fetchall()
    for count in rows:
        working_assets += count[1]
    return working_assets

def get_capital_adequacy(name: str, date: datetime) -> int:
    """ Коэффициент достаточности капитала
    Получает на вход имя банка и время, возвращает коэфициент, выраженный в целочисленных процентах
    Кд = Ск / Ар,  где Кд - коэффициент достаточности;
    Ск - величина собственного капитала банка;
    Ар -активы работающие (рисовые)."""
    bank_own_capital = get_bank_own_capital(name, date)
    working_assets = get_working_assets(name, date)
    return int(bank_own_capital/working_assets*100)
