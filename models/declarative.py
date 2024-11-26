from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from db import engine


class Base(DeclarativeBase): ...


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.name}, email={self.email})>"


Base.metadata.create_all(engine)
