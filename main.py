from models.declarative import Client
from db import Session


# Create
with Session() as session:
    client = Client(name="Cleyson Lima", email="cleyson@mail.com")
    session.add(client)
    session.commit()

# Read
with Session() as session:
    client = session.get(Client, 1)
    print(client)


# Update
with Session() as session:
    client = session.get(Client, 1)
    client.name = "Elton Fonseca"
    client.email = "elton@mail.com"
    session.commit()

# Delete
with Session() as session:
    client = session.get(Client, 1)
    session.delete(client)
    session.commit()
