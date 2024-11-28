from db import Session
from models.declarative import Order, Product


with Session() as session:
    order = session.get(Order, 1)

    order.products.append(Product(name="Product 1", price=100))
    order.products.append(Product(name="Product 2", price=120))
    order.products.append(Product(name="Product 3", price=200))

    session.commit()


with Session() as session:
    order = session.get(Order, 1)
    print(order.products)

    product = session.get(Product, 1)
    print(product.orders)


with Session() as session:
    order = session.get(Order, 1)

    order.products.pop()
    session.commit()
