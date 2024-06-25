from database.database import Database
from models.product import Product


class TextController:
    """Controller class for handling product database operations via CLI."""

    def __init__(self):
        """Initialize the TextController with an instance of the Database class."""
        self.database = Database()

    def create_product(self):
        """Create and add a new product to the database.

        Prompts the user for product details such as ID, name, price, and number of units.
        If a product with the entered ID already exists, an error message is displayed.
        """
        usr_id = int(input("ENTER PRODUCT ID: "))
        if self.database.search_product(usr_id) is not None:
            print("THERE IS ALREADY PRODUCT WITH ID: " + str(usr_id))
        else:
            name = input("ENTER NAME: ")
            price = int(input("ENTER PRICE: "))
            n_units = int(input("ENTER NUMBER OF UNITS: "))
            product = Product(usr_id, name, price, n_units)
            self.database.add_product(product)

    def display_database(self):
        """Display all products in the database.

        This method calls the debug_display method of the Database class to print
        the details of all products.
        """
        self.database.debug_display()

    def controller(self):
        """Run the command-line interface for managing the product database.

        Displays a menu with options to create, delete, display, update, and sell products,
        as well as to load and save the database from/to a file. The loop continues until
        the user selects the exit option.
        """
        h = 0
        while h != 8:
            h = int(
                input(
                    """MENU:
1. CREATE AND ADD PRODUCT
2. DELETE PRODUCT
3. DISPLAY DATABASE
4. CHANGE NUMBER OF UNITS
5. SELL PRODUCT
6. LOAD FILE
7. SAVE FILE
8. EXIT
"""
                )
            )
            match h:
                case 1:
                    self.create_product()
                case 2:
                    prod_id = abs(int(input("ENTER PRODUCT ID: ")))
                    self.database.delete_product(prod_id)
                case 3:
                    self.database.debug_display()
                case 4:
                    prod_id = abs(int(input("ENTER PRODUCT ID: ")))
                    new_units = int(input("ENTER NEW NUMBER OF UNITS: "))
                    self.database.change_n_units(prod_id, new_units)
                case 5:
                    prod_id = abs(int(input("ENTER PRODUCT ID: ")))
                    sell = int(input("ENTER HOW MANY YOU WANT TO SELL: "))
                    self.database.sell_units(prod_id, sell)
                case 6:
                    file_path = input("ENTER PATH TO THE FILE YOU WANT TO LOAD: ")
                    self.database.load_file(file_path)
                case 7:
                    file_path = input(
                        "ENTER PATH TO THE FILE YOU WANT TO SAVE THE DATABASE: "
                    )
                    self.database.save_file(file_path)
                case 8:
                    break
