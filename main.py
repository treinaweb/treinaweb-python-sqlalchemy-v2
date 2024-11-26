from sqlalchemy import update

from db import engine
from models.imperative import client_table


with engine.connect() as conn:
    stmt = (
        update(client_table)
        .where(client_table.c.id == 2)
        .values(name="Amauri Blanco", email="amauri@mail.com")
    )
    print(stmt)
    result = conn.execute(stmt)
    print(result.rowcount)
    print(result.last_updated_params())
    conn.commit()
