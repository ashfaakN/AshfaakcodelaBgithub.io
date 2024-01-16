from tkinter import *
import requests

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")
        master.config(bg="#202630")

        # Load image
        self.img = PhotoImage(file="images.png")
        self.image_label = Label(master, image=self.img, bg="#202630")
        self.image_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.from_label = Label(master, text="From Currency:", font=('Arial', 12), bg="#202630", fg="#FFFFFF")
        self.from_label.grid(row=1, column=0, pady=5)

        self.to_label = Label(master, text="To Currency:", font=('Arial', 12), bg="#202630", fg="#FFFFFF")
        self.to_label.grid(row=2, column=0, pady=5)

        self.variable1 = StringVar()
        self.variable2 = StringVar()

        self.from_menu = OptionMenu(master, self.variable1, *currency_list)
        self.from_menu.config(font=('Arial', 12))
        self.from_menu.grid(row=1, column=1, pady=5)

        self.to_menu = OptionMenu(master, self.variable2, *currency_list)
        self.to_menu.config(font=('Arial', 12))
        self.to_menu.grid(row=2, column=1, pady=5)

        self.amount_label = Label(master, text="Amount:", font=('Arial', 12), bg="#202630", fg="#FFFFFF")
        self.amount_label.grid(row=3, column=0, pady=5)

        self.amount_entry = Entry(master, font=('Arial', 12))
        self.amount_entry.grid(row=3, column=1, pady=5)

        self.convert_button = Button(master, text="Convert", command=self.convert_currency, font=('Arial', 12), bg="#710193", fg="#FFFFFF")
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.result_label = Label(master, text="", font=('Arial', 14), fg="#FFFFFF", bg="#202630")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        from_currency = self.variable1.get()
        to_currency = self.variable2.get()

        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            self.result_label.configure(text="Invalid input for amount. Please enter a numeric value.")
            return

        api_key = 'YOUR_API_KEY'
        api_url = f'https://open.er-api.com/v6/latest?apikey={api_key}'

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            exchange_rates = response.json().get('rates', {})

            if from_currency in exchange_rates and to_currency in exchange_rates:
                conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
                conversion_result = amount * conversion_rate
                self.result_label.configure(text=f"Converted Amount: {conversion_result:.2f} {to_currency}")
            else:
                self.result_label.configure(text="Invalid currency selection.")
        except requests.RequestException as e:
            self.result_label.configure(text=f"Error fetching exchange rates: {e}")

if __name__ == "__main__":
    currency_list = ["USD", "EUR", "GBP", "JPY", "INR", "AUD"]
    root = Tk()
    app = CurrencyConverterApp(root)
    root.geometry("500x500")
    root.mainloop()



