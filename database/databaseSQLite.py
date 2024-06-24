from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.productModel import ProductModel
import os

Base = declarative_base()


class DatabaseSQLite:

    def __init__(self, db_url="sqlite:///products.db"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_product(self, a_product):
        product = ProductModel(
            a_product.p_id, a_product.name, a_product.price, a_product.n_units
        )
        self.session.add(product)
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"Error adding product: {e}")

    def search_product(self, p_id):
        product = self.session.query(ProductModel).filter_by(p_id=p_id).first()
        if product:
            return ProductModel(
                product.p_id, product.name, product.price, product.n_units
            )
        return None

    def delete_product(self, p_id):
        product = self.session.query(ProductModel).filter_by(p_id=p_id).first()
        if product:
            self.session.delete(product)
            self.session.commit()
            print(f"Product with id {p_id} deleted.\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def change_n_units(self, p_id, new_units):
        product = self.session.query(ProductModel).filter_by(p_id=p_id).first()
        if product:
            product.n_units = new_units
            self.session.commit()
            print(f"Units for product with id {p_id} changed to {new_units}.\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def sell_units(self, p_id, how_many):
        product = self.session.query(ProductModel).filter_by(p_id=p_id).first()
        if product:
            new_units = product.n_units - how_many
            if new_units >= 0:
                product.n_units = new_units
                self.session.commit()
                print(f"Units for product with id {p_id} changed to {new_units}.\n")
            else:
                print("You don't have that many units to sell!\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def debug_display(self):
        products = self.session.query(ProductModel).all()
        for prod in products:
            print(f"ID: {prod.p_id}")
            print(f"NAME: {prod.name}")
            print(f"PRICE: {prod.price}")
            print(f"NUMBER OF UNITS: {prod.n_units}")
            print(f"-------------------------------")

    def load_file(self, filepath):
        try:
            with open(filepath, "r") as file:
                for line in file:
                    parts = line.strip().split("-")
                    p_id, name, price, n_units = map(str.strip, parts)
                    self.add_product(
                        ProductModel(p_id, name, float(price), int(n_units))
                    )
        except FileNotFoundError:
            print(f"ERROR: File: {filepath} not found.")
        except Exception as e:
            print(f"UNEXPECTED ERROR: {e}")

    def save_file(self, filepath):
        try:
            if not os.path.exists(filepath):
                parent_path = os.path.dirname(filepath)
                if parent_path:
                    os.makedirs(parent_path)
            with open(filepath, "w") as file:
                products = self.session.query(ProductModel).all()
                for product in products:
                    file.write(
                        f"{product.p_id}-{product.name}-{product.price}-{product.n_units}\n"
                    )
        except Exception as e:
            print(f"UNEXPECTED ERROR: {e}")

    def __del__(self):
        self.session.close()
        self.engine.dispose()
