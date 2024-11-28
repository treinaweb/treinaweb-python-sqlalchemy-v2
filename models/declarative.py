from datetime import datetime
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from db import engine
from models.uf import UF


class Base(DeclarativeBase): ...


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))

    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))
    address: Mapped["Address"] = relationship(
        back_populates="client",
        single_parent=True,
        cascade="save-update, merge, delete, delete-orphan",
    )

    orders: Mapped[list["Order"]] = relationship(
        back_populates="client",
        cascade="save-update, merge, delete, delete-orphan",
    )

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.name}, email={self.email})>"


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    state: Mapped[UF]
    city: Mapped[str] = mapped_column(String(100))
    neighborhood: Mapped[str] = mapped_column(String(100))
    street: Mapped[str] = mapped_column(String(100))
    number: Mapped[str] = mapped_column(String(10))

    client: Mapped["Client"] = relationship(
        back_populates="address", single_parent=True
    )

    def __repr__(self):
        return f"<Address(id={self.id}, state={self.state}, city={self.city}, neighborhood={self.neighborhood}, street={self.street}, number={self.number})>"


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    datetime: Mapped[datetime]

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    client: Mapped["Client"] = relationship(back_populates="orders")

    def __repr__(self):
        return f"<Order(id={self.id}, description={self.description}, datetime={self.datetime})>"


Base.metadata.create_all(engine)
