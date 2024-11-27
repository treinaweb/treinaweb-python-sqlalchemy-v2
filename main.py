from db import Session
from models.declarative import Client, Address
from models.uf import UF


# Create
with Session() as session:
    client = Client(
        name="Elton Fonseca",
        email="elton@mail.com",
        address=Address(
            state=UF.SP,
            city="São Paulo",
            neighborhood="Centro",
            street="Rua 1",
            number="1",
        ),
    )

    session.add(client)
    session.commit()

# Read
with Session() as session:
    client = session.get(Client, 1)
    print(client)
    print(client.address)

    address = session.get(Address, 2)
    print(address)
    print(address.client)

# Update
with Session() as session:
    client = session.get(Client, 1)

    client.address.state = UF.PI
    client.address.city = "Teresina"

    session.commit()

# Delete
with Session() as session:
    client = session.get(Client, 3)

    session.delete(client)

    session.commit()
