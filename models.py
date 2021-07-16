from db import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Coin(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    currency = Column(String)
    price = Column(Integer)
    date = Column(Integer)
