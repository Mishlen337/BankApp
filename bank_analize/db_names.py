from sqlalchemy import engine, MetaData, select

def get_bank_names(connection: engine.Connection, meta: MetaData):
    table_req = meta.tables['req']
    select_statement = select(table_req.c.NAME_B)
    result = connection.execute(select_statement)
    bank_names = result.fetchall()
    return bank_names