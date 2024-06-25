import os

from models.product import Product


class Database:
    """In-memory database for managing products."""

    def __init__(self):
        """Initialize an empty list to store products."""
        self.list = []

    def add_product(self, a_product):
        """Add a product to the database.

        Args:
            a_product (Product): The product to add.
        """
        self.list.append(a_product)

    def search_product(self, p_id):
        """Search for a product in the database by its ID.

        Args:
            p_id (int): The ID of the product to search for.

        Returns:
            Product: The product with the specified ID, or None if not found.
        """
        for prod in self.list:
            if p_id == prod.p_id:
                return prod
        return None

    def delete_product(self, p_id):
        """Delete a product from the database by its ID.

        Args:
            p_id (int): The ID of the product to delete.
        """
        product_to_remove = self.search_product(p_id)
        if product_to_remove is not None:
            self.list.remove(product_to_remove)
            print(f"Product with id {p_id} deleted.\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def change_n_units(self, p_id, new_units):
        """Change the number of units of a product.

        Args:
            p_id (int): The ID of the product.
            new_units (int): The new number of units.
        """
        product = self.search_product(p_id)
        if product is not None:
            index = self.list.index(product)
            product.change_units(new_units)
            self.list[index] = product
            print(f"Units for product with id {p_id} changed to {new_units}.\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def sell_units(self, p_id, how_many):
        """Sell a specified number of units of a product.

        Args:
            p_id (int): The ID of the product.
            how_many (int): The number of units to sell.
        """
        product = self.search_product(p_id)
        if product is not None:
            index = self.list.index(product)
            new_units = product.n_units - how_many
            print(new_units)
            if new_units >= 0:
                product.change_units(new_units)
                self.list[index] = product
                print(f"Units for product with id {p_id} changed to {new_units}.\n")
            else:
                print("You dont have that much units to sell!\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def debug_display(self):
        """Display all products in the database on the CLI."""
        for prod in self.list:
            print(f"ID: {prod.p_id}")
            print(f"NAME: {prod.name}")
            print(f"PRICE: {prod.price}")
            print(f"NUMBER OF UNITS: {prod.n_units}")
            print(f"-------------------------------")

    def load_file(self, filepath):
        """Load products from a file into the database.

        Args:
            filepath (str): The path to the file to load.
        """
        try:
            with open(filepath, "r") as file:
                for line in file:
                    parts = line.strip().split("-")
                    p_id, name, price, n_units = map(str.strip, parts)
                    self.add_product(Product(p_id, name, price, n_units))
        except FileNotFoundError:
            print(f"ERROR: File: {filepath} not found.")
        except Exception as e:
            print(f"UNEXPECTED ERROR: {e}")

    def save_file(self, filepath):
        """Save all products in the database to a file.

        Args:
            filepath (str): The path to the file to save.
        """
        try:
            if not os.path.exists(filepath):
                parent_path = os.path.dirname(filepath)
                os.makedirs(parent_path)
            with open(filepath, "w") as file:
                for product in self.list:
                    file.write(
                        f"{product.p_id}-{product.name}-{product.price}-{product.n_units}\n"
                    )
        except Exception as e:
            print(f"UNEXPECTED ERROR: {e}")
