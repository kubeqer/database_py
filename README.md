# Database

This project is a simple product management system implemented using Python. It supports both command-line and GUI interfaces for managing products in a database. The database can be either in-memory or SQLite.

## Features

- Add, delete, and update products.
- Change the number of units of a product.
- Sell products by reducing the number of units.
- Display all products in the database.
- Load and save the database from/to a file.
- Command-line interface (CLI) and graphical user interface (GUI) using Tkinter.

## Requirements

- Python 3.x
- SQLAlchemy
- Tkinter (comes with standard Python distribution)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/kubeqer/database_py.git
    cd database_py
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command-Line Interface (CLI)


1. **Modify the `main.py` file:**

    Change:
    ```python
    def main():
        app = TkinterController()
        app.run()
    ```

    To:
    ```python
    def main():
        app = TextController()
        app.controller()
    ```

2. **Run the CLI:**
    ```bash
    python main.py
    ```

3. **Follow the on-screen menu to manage products:**
    - 1. Create and add a product.
    - 2. Delete a product.
    - 3. Display the database.
    - 4. Change the number of units.
    - 5. Sell a product.
    - 6. Load the database from a file.
    - 7. Save the database to a file.
    - 8. Exit.

### Graphical User Interface (GUI)

1. **Run the GUI application:**
    ```bash
    python main.py
    ```

2. **Use the buttons on the GUI to manage products:**
    - **Add Product:** Opens a form to add a new product.
    - **Delete Product:** Opens a form to delete a product by ID.
    - **Change Number of Units:** Opens a form to update the units of a product.
    - **Sell Product:** Opens a form to sell units of a product.
    - **Display Database:** Displays all products in the database.
    - **Load File:** Loads the database from a specified file.
    - **Save to File:** Saves the database to a specified file.
    - **Exit:** Closes the application.

## Project Structure

- `main.py`: Entry point for the GUI application.
- `product.py`: Defines the `Product` class.
- `productModel.py`: Defines the SQLAlchemy model for `Product`.
- `database.py`: In-memory database implementation.
- `databaseSQLite.py`: SQLite database implementation using SQLAlchemy.
- `textController.py`: CLI controller for managing products.
- `tkinterController.py`: GUI controller using Tkinter.

## Example

### Adding a Product

1. **CLI:**
    ```plaintext
    MENU:
    1. CREATE AND ADD PRODUCT
    2. DELETE PRODUCT
    3. DISPLAY DATABASE
    4. CHANGE NUMBER OF UNITS
    5. SELL PRODUCT
    6. LOAD FILE
    7. SAVE FILE
    8. EXIT
    Enter your choice: 1
    ENTER PRODUCT ID: 101
    ENTER NAME: Laptop
    ENTER PRICE: 999.99
    ENTER NUMBER OF UNITS: 10
    ```

2. **GUI:**
    - Click on the "ADD PRODUCT" button.
    - Enter the product details in the form and click "Submit".