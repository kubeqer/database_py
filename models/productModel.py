from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductModel(Base):
    """Model for the products table in SQLite."""

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
