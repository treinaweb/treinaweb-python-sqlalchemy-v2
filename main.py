from sqlalchemy import text

from db import engine


with engine.connect() as conn:
    conn.execute(text("SELECT 'Hello World'"))
