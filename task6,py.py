import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()

    # Create Products table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL
                    )''')

    # Create Customers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        contact TEXT NOT NULL
                    )''')

    # Create Transactions table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        total_price REAL,
                        date TEXT,
                        FOREIGN KEY(customer_id) REFERENCES Customers(id),
                        FOREIGN KEY(product_id) REFERENCES Products(id)
                    )''')

    conn.commit()
    conn.close()

# GUI Design and Development
class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")

        # Initialize GUI components
        self.product_name_var = tk.StringVar()
        self.product_price_var = tk.DoubleVar()
        self.customer_name_var = tk.StringVar()
        self.customer_contact_var = tk.StringVar()
        self.transaction_quantity_var = tk.IntVar()

        # Add GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Product Section
        product_frame = tk.LabelFrame(self.root, text="Product Details")
        product_frame.pack(fill="both", expand="yes", padx=20, pady=10)

        tk.Label(product_frame, text="Product Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(product_frame, textvariable=self.product_name_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(product_frame, text="Product Price:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(product_frame, textvariable=self.product_price_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(product_frame, text="Add Product", command=self.add_product).grid(row=2, columnspan=2, pady=10)

        # Customer Section
        customer_frame = tk.LabelFrame(self.root, text="Customer Details")
        customer_frame.pack(fill="both", expand="yes", padx=20, pady=10)

        tk.Label(customer_frame, text="Customer Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(customer_frame, textvariable=self.customer_name_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(customer_frame, text="Customer Contact:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(customer_frame, textvariable=self.customer_contact_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(customer_frame, text="Add Customer", command=self.add_customer).grid(row=2, columnspan=2, pady=10)

        # Transaction Section
        transaction_frame = tk.LabelFrame(self.root, text="Transaction Details")
        transaction_frame.pack(fill="both", expand="yes", padx=20, pady=10)

        tk.Label(transaction_frame, text="Quantity:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(transaction_frame, textvariable=self.transaction_quantity_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(transaction_frame, text="Generate Invoice", command=self.generate_invoice).grid(row=1, columnspan=2, pady=10)

    def add_product(self):
        name = self.product_name_var.get()
        price = self.product_price_var.get()

        conn = sqlite3.connect('billing.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Products (name, price) VALUES (?, ?)", (name, price))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Product added successfully")

    def add_customer(self):
        name = self.customer_name_var.get()
        contact = self.customer_contact_var.get()

        conn = sqlite3.connect('billing.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Customers (name, contact) VALUES (?, ?)", (name, contact))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Customer added successfully")

    def generate_invoice(self):
        # Here you would implement logic to generate the invoice
        # This example just prints the details to console for simplicity

        quantity = self.transaction_quantity_var.get()

        # Normally you'd look up product/customer info here
        # This is just a placeholder example

        print(f"Invoice generated: Quantity - {quantity}")

if __name__ == "__main__":
    setup_database()
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
