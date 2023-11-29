from product import Product
from database import Database


class TextController:
    def __init__(self):
        self.database = Database()

    def create_product(self):
        usr_id = 0
        h = int(input("ENTER PRODUCT ID: "))
        while usr_id == 0:
            for prod in self.database.list:
                if h == prod.p_id:
                    print(f"THERE IS ALREADY PRODUCT WITH ID: {h}")
                    break
            else:
                usr_id = h
            name = input("ENTER NAME: ")
            price = int(input("ENTER PRICE: "))
            n_units = int(input("ENTER NUMBER OF UNITS: "))
            product = Product(usr_id, name, price, n_units)
            self.database.add_product(product)

    def display_database(self):
        self.database.debug_display()

    def controller(self):
        h = 0
        while h != 9:
            h = int(input("""MENU:
1. CREATE AND ADD PRODUCT
2. DELETE DATABASE
3. DISPLAY DATABASE
4. DELETE PRODUCT
5. CHANGE NUMBER OF UNITS
6. SELL PRODUCT
7. LOAD FILE
8. SAVE FILE
9. EXIT
"""))
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
                    self.database.delete_product(prod_id)
                case 5:
                    prod_id = abs(int(input("ENTER PRODUCT ID: ")))
                    new_units = int(input("ENTER NEW NUMBER OF UNITS: "))
                    self.database.change_n_units(prod_id, new_units)
                case 6:
                    prod_id = abs(int(input("ENTER PRODUCT ID: ")))
                    sell = int(input("ENTER HOW MANY YOU WANT TO SELL: "))
                    self.database.change_n_units(prod_id, sell)
                case 7:
                    file_path = input("ENTER PATH TO THE FILE YOU WANT TO LOAD: ")
                    self.database.load_file(file_path)
                case 8:
                    file_path = input("ENTER PATH TO THE FILE YOU WANT TO SAVE THE DATABASE: ")
                    self.database.save_file(file_path)
                case 9:
                    break

