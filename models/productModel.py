from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductModel(Base):
    __tablename__ = "products"
    p_id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    n_units = Column(Integer)

    def __init__(self, p_id, name, price, n_units):
        self.p_id = p_id
        self.name = name
        self.price = price
        self.n_units = n_units
