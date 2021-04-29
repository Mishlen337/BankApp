from datetime import datetime
from sqlalchemy import engine, Table, Column, String, Float, MetaData, select, and_
def form_bank_mart(connection: engine.Connection, meta: MetaData, names: list, date: str):
    connection.