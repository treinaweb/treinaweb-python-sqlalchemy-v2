from sqlalchemy import select

from db import engine
from models.imperative import client_table


with engine.connect() as conn:
    stmt = select(client_table).where(client_table.c.name == "Cleyson Lima")
    print(stmt)
    result = conn.execute(stmt)
    for row in result:
        print(row)
