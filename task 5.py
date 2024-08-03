import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("USD Currency Converter")
        
        # Set up the main frame
        self.mainframe = ttk.Frame(root, padding="10 10 30 30")
        self.mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # USD Amount Entry
        self.usd_amount = tk.StringVar()
        ttk.Label(self.mainframe, text="Amount in USD:").grid(column=1, row=1, sticky=tk.W)
        self.usd_entry = ttk.Entry(self.mainframe, width=15, textvariable=self.usd_amount)
        self.usd_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        
        # Currency Selection
        self.currency = tk.StringVar()
        ttk.Label(self.mainframe, text="Select Currency:").grid(column=1, row=2, sticky=tk.W)
        self.currency_combobox = ttk.Combobox(self.mainframe, textvariable=self.currency)
        self.currency_combobox['values'] = ('EUR', 'GBP', 'INR', 'JPY', 'AUD', 'CAD')
        self.currency_combobox.grid(column=2, row=2, sticky=(tk.W, tk.E))
        
        # Convert Button
        self.convert_button = ttk.Button(self.mainframe, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=2, row=3, sticky=tk.W)
        
        # Result Display
        self.result = tk.StringVar()
        ttk.Label(self.mainframe, text="Converted Amount:").grid(column=1, row=4, sticky=tk.W)
        self.result_label = ttk.Label(self.mainframe, textvariable=self.result)
        self.result_label.grid(column=2, row=4, sticky=(tk.W, tk.E))
        
        # Padding for all widgets
        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
        # API Key and URL
        self.api_key = 'your_api_key_here'  # Replace with your actual API key
        self.api_url = f'https://v6.exchangerate-api.com/v6/{self.api_key}/latest/USD'
        
        # Get Exchange Rates
        self.exchange_rates = self.get_exchange_rates()

    def get_exchange_rates(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            return data['conversion_rates']
        except requests.exceptions.RequestException as e:
            tk.messagebox.showerror("Error", f"Failed to fetch exchange rates: {e}")
            return {}

    def convert_currency(self):
        try:
            usd_amount = float(self.usd_amount.get())
            target_currency = self.currency.get()
            if target_currency and target_currency in self.exchange_rates:
                converted_amount = usd_amount * self.exchange_rates[target_currency]
                self.result.set(f"{converted_amount:.2f} {target_currency}")
            else:
                tk.messagebox.showerror("Error", "Please select a valid currency.")
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
