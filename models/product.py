class Product:
    """Class representing a product."""

    def __init__(self, p_id, name, price, n_units):
        self.p_id = abs(int(p_id))
        self.name = name
        self.price = abs(int(price))
        self.n_units = int(n_units)

    def change_units(self, n_units):
        """Change the number of units for the product.

        Args:
            n_units (int): The new number of units.
        """
        self.n_units = n_units

    def get_units(self):
        """Get the number of units of the product.

        Returns:
            int: The number of units.
        """
        return self.n_units
