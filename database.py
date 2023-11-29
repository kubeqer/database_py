from product import Product


class Database:

    def __init__(self):
        self.list = []

    def add_product(self, a_product):
        self.list.append(a_product)

    def search_product(self, p_id):
        for prod in self.list:
            if p_id == prod.p_id:
                return prod
        return None

    def delete_product(self, p_id):
        product_to_remove = self.search_product(p_id)
        if product_to_remove is not None:
            self.list.remove(product_to_remove)
            print(f"Product with id {p_id} deleted.\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def change_n_units(self, p_id, new_units):
        product = self.search_product(p_id)
        if product is not None:
            index = self.list.index(product)
            product.change_units(new_units)
            self.list[index] = product
            print(f"Units for product with id {p_id} changed to {new_units}.\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def sell_units(self, p_id, how_many):
        product = self.search_product(p_id)
        if product is not None:
            index = self.list.index(product)
            new_units = product.n_units - how_many
            if new_units >= 0:
                product.change_units(new_units)
                self.list[index] = product
                print(f"Units for product with id {p_id} changed to {new_units}.\n")
            else:
                print("You dont have that much units to sell!\n")
        else:
            print(f"Product with id {p_id} not found.\n")

    def debug_display(self):
        for prod in self.list:
            print(f"ID: {prod.p_id}")
            print(f"NAME: {prod.name}")
            print(f"PRICE: {prod.price}")
            print(f"NUMBER OF UNITS: {prod.n_units}")
            print(f"-------------------------------")

    def load_file(self, filepath):
        try:
            with open(filepath, "r") as file:
                for line in file:
                    parts = line.strip().split('-')
                    p_id, name, price, n_units = map(str.strip, parts)
                    self.add_product(Product(p_id, name, price, n_units))
        except FileNotFoundError:
            print(f"ERROR: File: {filepath} not found.")
        except Exception as e:
            print(f"UNEXPECTED ERROR: {e}")

    def save_file(self, filepath):
        try:
            with open(filepath, "w") as file:
                for product in self.list:
                    file.write(f"{product.p_id}-{product.name}-{product.price}-{product.n_units}\n")
        except Exception as e:
            print(f"UNEXPECTED ERROR: {e}")
