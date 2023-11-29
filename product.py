class Product:
    def __init__(self, p_id, name, price, n_units):
        self.p_id = abs(int(p_id))
        self.name = name
        self.price = abs(int(price))
        self.n_units = int(n_units)

    def change_units(self, n_units):
        self.n_units = n_units
