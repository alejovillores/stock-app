from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(255), nullable=False)
    last_name = Column("last_name", String(255), nullable=False)
    email = Column("email", String(255), nullable=False)
    password = Column("password", String(255), nullable=False)
