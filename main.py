from sqlalchemy import insert

from db import engine
from models.imperative import client_table


with engine.connect() as conn:
    stmt = insert(client_table).values(name="Elton Fonseca", email="elton@mail.com")
    result = conn.execute(stmt)
    print(result.inserted_primary_key)
    print(result.inserted_primary_key_rows)
    print(result.last_inserted_params())
    conn.commit()
