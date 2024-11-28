from datetime import datetime

from db import Session
from models.declarative import Client, Order

# Add Order
with Session() as session:
    client = session.get(Client, 1)

    client.orders.append(
        Order(
            description="Order 1",
            datetime=datetime.now(),
        )
    )

    client.orders.append(
        Order(
            description="Order 2",
            datetime=datetime.now(),
        )
    )

    session.commit()


# Remove Order
with Session() as session:
    client = session.get(Client, 1)

    client.orders.pop()

    session.commit()


# Update Order
with Session() as session:
    client = session.get(Client, 1)

    order = client.orders[0]
    order.description = "Order 1 Updated"

    session.commit()


# Delete Client
with Session() as session:
    client = session.get(Client, 1)

    session.delete(client)

    session.commit()
