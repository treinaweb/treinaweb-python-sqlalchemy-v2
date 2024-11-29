import logging
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from db import Session
from models.declarative import Client, Order

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


with Session() as session:
    stmt = select(Client).options(
        joinedload(Client.address),
        selectinload(Client.orders).selectinload(Order.products),
    )
    clients = session.execute(stmt).scalars().all()

    for client in clients:
        print(client, client.address, client.orders)
        for order in client.orders:
            print("\t", order.products)
