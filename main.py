from sqlalchemy import delete

from db import engine
from models.imperative import client_table


with engine.connect() as conn:
    stmt = delete(client_table).where(client_table.c.id == 2)
    print(stmt)
    result = conn.execute(stmt)
    print(result.rowcount)
    conn.commit()
