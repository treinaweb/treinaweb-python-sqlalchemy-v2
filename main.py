from sqlalchemy import select, func

from db import Session
from models.declarative import Client, Order, Product

# Consulta simples
with Session() as session:
    # Listar todos os clientes
    stmt = select(Client)
    clients = session.execute(stmt).scalars().all()
    print(clients)

# Consulta com filtro
with Session() as session:
    # Buscar cliente com id = 1
    stmt = select(Client).where(Client.id == 1)
    client = session.execute(stmt).scalar()
    print(type(client))

# Consulta com join
with Session() as session:
    # Buscar todos os pedidos de um cliente
    stmt = select(Order).join(Order.client).where(Client.email == "alice@example.com")
    orders = session.execute(stmt).scalars().all()
    print(orders)

# Ordenação, limitação e offset
with Session() as session:
    # Listar os 5 produtos mais caros, começando do terceiro
    stmt = select(Product).order_by(Product.price.desc()).limit(5).offset(2)
    products = session.execute(stmt).scalars().all()
    print(products)

# Consulta com agregação
with Session() as session:
    # Listar o total de pedidos por cliente
    stmt = (
        select(Client.name, func.count(Order.id))
        .join(Order.client)
        .group_by(Client.name)
    )
    result = session.execute(stmt).all()
    for name, count in result:
        print(f"Cliente: {name}, Total de Pedidos: {count}")

# Consulta com subquery
with Session() as session:
    # Listar clientes que fizeram mais de um pedido
    subquery = (
        select(Order.client_id, func.count(Order.id).label("total_orders"))
        .group_by(Order.client_id)
        .subquery()
    )
    stmt = (
        select(Client)
        .join(subquery, Client.id == subquery.c.client_id)
        .where(subquery.c.total_orders > 1)
    )
    clients = session.execute(stmt).scalars().all()
    print(clients)
