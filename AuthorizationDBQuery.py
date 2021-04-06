from sqlalchemy import *

def client_verification(username:str, password:str)->bool:
    engine = create_engine('sqlite:///verification.db')
    meta = MetaData()
    client = Table('Client', meta, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(select(client.c.username, client.c.password).\
                where(client.c.username == username, client.c.password == password))
        row = result.fetchone()
        if row:
            return True
        return False

def admin_verification(username:str, password:str)->bool:
    engine = create_engine('sqlite:///verification.db')
    meta = MetaData()
    client = Table('Admin', meta, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(select(client.c.username, client.c.password).\
                where(client.c.username == username, client.c.password == password))
        row = result.fetchone()
        if row:
            return True
        return False

#print(client_verification('Mikhail','123'))
