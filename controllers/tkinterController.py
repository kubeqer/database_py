from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from database.databaseSQLite import DatabaseSQLite, ProductModel


class TkinterController:
    """Controller class for handling product database operations via a Tkinter GUI."""

    def __init__(self):
        """Initialize the TkinterController with a GUI and an instance of the DatabaseSQLite class."""
        self.root = Tk()
        self.root.title("Database")
        self.root.geometry("1920x1080")
        self.database = DatabaseSQLite()

        self.flag = ""
        self.flag_is = False

        self.button_add = Button(
            self.root,
            text="ADD PRODUCT",
            padx=40,
            pady=40,
            command=self.button_add,
            width=20,
        )
        self.button_del = Button(
            self.root,
            text="DELETE PRODUCT",
            padx=40,
            pady=40,
            command=self.button_del,
            width=20,
        )
        self.button_change = Button(
            self.root,
            text="CHANGE NUMBER\n OF UNITS",
            padx=40,
            pady=40,
            command=self.button_change,
            width=20,
        )
        self.button_sell = Button(
            self.root,
            text="SELL PRODUCT",
            padx=40,
            pady=40,
            command=self.button_sell,
            width=20,
        )
        self.button_display = Button(
            self.root,
            text="DISPLAY\nDATABASE",
            padx=40,
            pady=40,
            command=self.button_displaydata,
            width=20,
        )
        self.button_loadfile = Button(
            self.root,
            text="LOAD FILE",
            padx=40,
            pady=40,
            command=self.button_loadfile,
            width=20,
        )
        self.button_savefile = Button(
            self.root,
            text="SAVE TO FILE",
            padx=40,
            pady=40,
            command=self.button_savefile,
            width=20,
        )
        self.button_exit = Button(
            self.root, text="EXIT", padx=40, pady=40, command=self.button_exit, width=20
        )

        self.id_label = Label(self.root, text="PRODUCT ID:")
        self.entry_id = Entry(self.root, width=10)

        self.name_label = Label(self.root, text="NAME:")
        self.entry_name = Entry(self.root, width=10)

        self.price_label = Label(self.root, text="PRICE:")
        self.entry_price = Entry(self.root, width=10)

        self.units_label = Label(self.root, text="UNITS:")
        self.entry_units = Entry(self.root, width=10)

        self.filepath_label = Label(self.root, text="FILE PATH:")
        self.entry_filepath = Entry(self.root, width=20)

        self.button_submit = Button(
            self.root, text="Submit", command=self.button_submit
        )

        self.tree = ttk.Treeview(
            self.root, columns=("ID", "Name", "Price", "Units"), show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Units", text="Units")
        self.tree.grid(row=0, column=1, rowspan=10, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the main buttons in the Tkinter window."""
        self.button_add.grid(row=0, column=0)
        self.button_del.grid(row=1, column=0)
        self.button_change.grid(row=2, column=0)
        self.button_sell.grid(row=3, column=0)
        self.button_display.grid(row=4, column=0)
        self.button_loadfile.grid(row=5, column=0)
        self.button_savefile.grid(row=6, column=0)
        self.button_exit.grid(row=7, column=0)

    def button_displaydata(self):
        """Display all products in the database in the Treeview widget."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        products = self.database.session.query(ProductModel).all()
        for product in products:
            values = (product.p_id, product.name, product.price, product.n_units)
            self.tree.insert("", "end", values=values)

    def button_submit(self):
        """Handle the submission of form data based on the current operation flag."""
        if self.flag == "ADD":
            product_id = self.entry_id.get()
            name = self.entry_name.get()
            price = self.entry_price.get()
            units = self.entry_units.get()

            price = float(price)
            units = int(units)

            if self.database.search_product(product_id) is None:
                self.database.add_product(ProductModel(product_id, name, price, units))

                self.entry_id.delete(0, "end")
                self.entry_name.delete(0, "end")
                self.entry_price.delete(0, "end")
                self.entry_units.delete(0, "end")

                self.id_label.grid_remove()
                self.entry_id.grid_remove()
                self.name_label.grid_remove()
                self.entry_name.grid_remove()
                self.price_label.grid_remove()
                self.entry_price.grid_remove()
                self.units_label.grid_remove()
                self.entry_units.grid_remove()
                self.button_submit.grid_remove()
                self.flag = ""
            else:
                messagebox.showerror("Error", "There is already a product with this ID")

        elif self.flag == "DEL":
            product_id = self.entry_id.get()

            if self.database.search_product(product_id) is None:
                messagebox.showerror("Error", "There is no product with this ID")
            else:
                self.database.delete_product(product_id)

                self.entry_id.delete(0, "end")

                self.id_label.grid_remove()
                self.entry_id.grid_remove()
                self.button_submit.grid_remove()
                self.flag = ""

        elif self.flag == "CHANGE":
            product_id = self.entry_id.get()
            units = int(self.entry_units.get())
            if self.database.search_product(product_id) is None:
                messagebox.showerror("Error", "There is no product with this ID")
            elif units < 0:
                messagebox.showerror("Error", "You have to pass more than 0 units")
            else:
                self.database.change_n_units(product_id, units)

                self.entry_id.delete(0, "end")
                self.entry_units.delete(0, "end")

                self.id_label.grid_remove()
                self.entry_id.grid_remove()
                self.units_label.grid_remove()
                self.entry_units.grid_remove()
                self.button_submit.grid_remove()
                self.flag = ""

        elif self.flag == "SELL":
            product_id = self.entry_id.get()
            units = abs(int(self.entry_units.get()))
            product = self.database.search_product(product_id)
            if product:
                new_units = product.n_units - units
                if new_units >= 0:
                    self.database.change_n_units(product_id, new_units)
                    self.entry_id.delete(0, "end")
                    self.entry_units.delete(0, "end")
                    self.id_label.grid_remove()
                    self.entry_id.grid_remove()
                    self.units_label.grid_remove()
                    self.entry_units.grid_remove()
                    self.button_submit.grid_remove()
                    self.flag = ""
                else:
                    messagebox.showerror(
                        "Error", "You don't have that many units to sell!"
                    )
            else:
                messagebox.showerror("Error", "There is no product with this ID")

        elif self.flag == "LOAD":
            filepath = self.entry_filepath.get()
            try:
                self.database.load_file(filepath)
            except FileNotFoundError:
                messagebox.showerror("Error", "There is no file in this path")
            else:
                self.entry_filepath.delete(0, "end")

                self.filepath_label.grid_remove()
                self.entry_filepath.grid_remove()
                self.button_submit.grid_remove()

                self.flag = ""

        elif self.flag == "SAVE":
            filepath = self.entry_filepath.get()
            self.database.save_file(filepath)

            self.entry_filepath.delete(0, "end")

            self.filepath_label.grid_remove()
            self.entry_filepath.grid_remove()
            self.button_submit.grid_remove()

        self.flag_is = False

    def button_add(self):
        """Set up the form for adding a new product."""
        if self.flag_is is False:
            self.id_label.grid(row=0, column=2)
            self.entry_id.grid(row=0, column=3)

            self.name_label.grid(row=1, column=2)
            self.entry_name.grid(row=1, column=3)

            self.price_label.grid(row=2, column=2)
            self.entry_price.grid(row=2, column=3)

            self.units_label.grid(row=3, column=2)
            self.entry_units.grid(row=3, column=3)

            self.button_submit.grid(row=4, column=3)
            self.flag = "ADD"
            self.flag_is = True

    def button_del(self):
        """Set up the form for deleting a product."""
        if self.flag_is is False:
            self.id_label.grid(row=0, column=2)
            self.entry_id.grid(row=0, column=3)
            self.button_submit.grid(row=1, column=3)
            self.flag = "DEL"
            self.flag_is = True

    def button_change(self):
        """Set up the form for changing the number of units of a product."""
        if self.flag_is is False:
            self.id_label.grid(row=0, column=2)
            self.entry_id.grid(row=0, column=3)

            self.units_label.grid(row=1, column=2)
            self.entry_units.grid(row=1, column=3)

            self.button_submit.grid(row=2, column=3)
            self.flag = "CHANGE"
            self.flag_is = True

    def button_sell(self):
        """Set up the form for selling units of a product."""
        if self.flag_is is False:
            self.id_label.grid(row=0, column=2)
            self.entry_id.grid(row=0, column=3)

            self.units_label.grid(row=1, column=2)
            self.entry_units.grid(row=1, column=3)

            self.button_submit.grid(row=2, column=3)
            self.flag = "SELL"
            self.flag_is = True

    def button_loadfile(self):
        """Set up the form for loading the database from a file."""
        if self.flag_is is False:
            self.filepath_label.grid(row=0, column=2)
            self.entry_filepath.grid(row=0, column=3)
            self.button_submit.grid(row=1, column=3)

            self.flag = "LOAD"
            self.flag_is = True

    def button_savefile(self):
        """Set up the form for saving the database to a file."""
        if self.flag_is is False:
            self.filepath_label.grid(row=0, column=2)
            self.entry_filepath.grid(row=0, column=3)
            self.button_submit.grid(row=1, column=3)

            self.flag = "SAVE"
            self.flag_is = True

    def button_exit(self):
        """Close the application."""
        self.root.quit()

    def run(self):
        """Run the Tkinter main loop to start the application."""
        self.root.mainloop()
