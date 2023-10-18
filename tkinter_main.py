import requests
import json
import datetime


class CurrencyConverter:
    def __init__(self):
        """
        When a currency converter is created it should first try to load currency data from JSON (using the load_currency_data-method)
        If it doesn't find any json-data, it should try to get the data from the exchangerates API (using the fetch_currency_data-method)
        """
        pass
    
    def fetch_currency_data(self):
        """
        This method should fetch new currency data using the openexchangerate API
        It has some boilerplate code you can use.
        """
        # Use this code to fetch currency data from openexchangerates.org.
        app_id = '57680e3013ec47d0a04b1fe84eb5ede6' # Add your own app_id from openexchangerates.org here
        url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}"
        headers = {"accept": "application/json"} # This needs to be added, it tells the API that they should return JSON
        response = requests.get(url, headers=headers)
        return response.json()
    
    def convert_from_usd(self, to_currency, amount):
        """
        This method should convert from USD to a currency of choice
        You should not use an additional endpoint, the latest currencies are enough.
        """ 
        currency_data = self.load_from_file()
        rates = currency_data["rates"]

        converted_value = rates[to_currency]*amount
        print(f"If you exchange {amount:.2f} USD, you would have {converted_value:.2f} {to_currency} ")

        return converted_value

            
    def convert_any_currency(self, from_currency, to_currency, amount):
 
        currency_data = self.load_from_file()
        rates = currency_data["rates"]
        exchanged_any_value = (rates[to_currency] / rates[from_currency]) * amount
        #print(f"If you exchange {amount:.2f} {from_currency}, you would have {exchanged_any_value:.2f} {to_currency} ")
        return exchanged_any_value
    
    def list_currencies(self):
        """
        This method lists available currencies in alphabetical order
        """
        open_exchange_rates = self.load_from_file()
        rates = open_exchange_rates['rates'] 
        return rates
    
    def load_currency_data(self):
        current_time = datetime.datetime.now()
        timestamp_now = int(current_time.timestamp())
        data1 = self.load_from_file()

        if ( timestamp_now - data1['timestamp'] ) > 3600:
            self.export_to_json()  

        data2 = self.load_from_file()
        print("\n\nCurrent time: ", current_time)
        print("Last Update of currency rates: ", datetime.datetime.fromtimestamp(data2['timestamp']))

    def export_to_json(self):
        """
        This should export to JSON so that the application can be run again without the need to fetch new data
        """
        data = self.fetch_currency_data()
        with open('exchange_rate.json', "w") as f:
            json.dump(data,f)
            return f
    def load_from_file(self):
        
        """
        Load and return the items from a JSON file with the specified filename.
        """
        with open('exchange_rate.json') as f:
            items = json.load(f)
            return items



# ========================================================================================
# ===================================== tkinter part =====================================
from tkinter import *

CurrencyConverter2 = CurrencyConverter()

def currency_list_window():
    """
    Currency List
    """
    currencies = CurrencyConverter2.list_currencies()

    new_window = Toplevel(window)
    # new_window.minsize(200,400)
    # new_window.geometry('300x2500')
    new_window.title("Currency List")

    canvas = Canvas(new_window, width=400)
    canvas.pack(side=RIGHT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(new_window, command=canvas.yview)
    scrollbar.pack(side=LEFT, fill=Y)
    canvas.config(yscrollcommand=scrollbar.set)

    frame = Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')

    label_width = 40
    for currency, exchange_rate in currencies.items():
        label_text = f"  {currency}  -  {exchange_rate}"
        label = Label(frame, text= label_text, width=label_width, anchor='w')
        label.pack()

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))


"""
Convert from USD to any currency
"""

from tkinter import messagebox

class USDConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("USD Exchange")

        self.amount_label = Label(master, text="\nEnter amount in USD:", font=("Times new roman", 14), foreground='green')
        self.amount_entry = Entry(master)
        self.amount_label.pack()
        self.amount_entry.pack()

        self.currency_label = Label(master, text="\n\nSelect currency:", font=("Times new roman", 14), foreground='green')
        self.currency_var = StringVar()
        currencies = CurrencyConverter().list_currencies().keys()

        self.currency_combobox = OptionMenu(master, self.currency_var, *currencies)

        self.currency_label.pack()

        self.currency_combobox.pack()
        self.currency_label2 = Label(master, text="\n", font=("Times new roman", 14), foreground='green')
        self.currency_label2.pack()

        self.convert_button = Button(master, text="Convert", font=("Times new roman", 14), foreground='red', command=self.convert)
        self.convert_button.pack()

    def convert(self):
        amount_str = self.amount_entry.get()
        currency = self.currency_var.get()

        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for the amount.")
            return

        result = CurrencyConverter().convert_from_usd(currency, amount)

        result_text = f"If you exchange {amount:.2f} USD, you will have {result:.2f} {currency}"
        messagebox.showinfo("Conversion Result", result_text)


def open_conversion_window():
    conversion_window = Toplevel(window)
    conversion_window.title("USD exchange")
    conversion_window.minsize(300,300)
    USDConverter(conversion_window)



def refresh_data():
    """
    Refresh data
    """
    CurrencyConverter2.load_currency_data()
    update_text = f"Old data is replaced with new data."
    messagebox.showinfo("Uppdate data", update_text)


def save_file():
    """
    Save file to json file
    """
    CurrencyConverter2.export_to_json()
    save_massage = f"File has been saved to 'exchange_rate.json' file"
    messagebox.showinfo("Uppdate data", save_massage)
    

"""
Convert from any currency to any currency
"""


class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Exchange Allpication")

        self.amount_label = Label(master, text="\nEnter amount of money:", font=("Times new roman", 14), foreground='green')
        self.amount_entry = Entry(master)
        self.amount_label.pack()
        self.amount_entry.pack()

        self.currency_from_label = Label(master, text="\n\nSelect currency to exchange from:", font=("Times new roman", 14), foreground='green')
        self.currency_from_var = StringVar()
        currencies_from = CurrencyConverter().list_currencies().keys()
        self.currency_from_combobox = OptionMenu(master, self.currency_from_var, *currencies_from)
        self.currency_from_label.pack()
        self.currency_from_combobox.pack()

        self.currency_to_label = Label(master, text="\nSelect currency to exchange to:", font=("Times new roman", 14), foreground='green')
        self.currency_to_var = StringVar()
        currencies_to = CurrencyConverter().list_currencies().keys()
        self.currency_to_combobox = OptionMenu(master, self.currency_to_var, *currencies_to)
        self.currency_to_label.pack()
        self.currency_to_combobox.pack()
        self.currency_label2 = Label(master, text="\n", font=("Times new roman", 14), foreground='green')
        self.currency_label2.pack()

        self.convert_button = Button(master, text="Convert", font=("Times new roman", 14), foreground='red', command=self.convert)
        self.convert_button.pack()

    def convert(self):
        amount_str = self.amount_entry.get()
        currency_from = self.currency_from_var.get()
        currency_to = self.currency_to_var.get()

        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for the amount.")
            return

        result = CurrencyConverter().convert_any_currency(currency_from, currency_to, amount)

        result_text = f"If you change {currency_from}, you will have {result:.2f} {currency_to}"
        messagebox.showinfo("Conversion Result", result_text)


def open_conversion_window_any():
    conversion_window = Toplevel(window)
    conversion_window.title("Any Currency Exchange")
    conversion_window.minsize(300, 300)
    CurrencyConverterApp(conversion_window)
#================================


window = Tk()
window.title("Currency Exchange App")
window.minsize(700,700)
window.maxsize(1000,1000)
#window.geometry('1000x900')
canvas = Canvas(width=250, height=300)
exchange_img = PhotoImage(file="C:/Users/aeros/OneDrive/Desktop/laboration-2-pia23-AliAbdi1987/exchange.png")
canvas.create_image(120, 150, image=exchange_img)
#window.resizable(width= False , height= False)
my_lable1 = Label(window, text= " \n Welcome to currency exchange application  ", font= ("Times new roman" , 20), foreground= "green")
my_lable1.grid(column=0,row=0,columnspan=2)
my_lable2 = Label(window, text= "   ", font= ("Times new roman" , 20), foreground= "green")
my_lable2.grid(column=0,row=5,columnspan=2)
my_lable3 = Label(window, text= " \n   ", font= ("Times new roman" , 20), foreground= "green")
my_lable3.grid(column=0,row=7,columnspan=2)
my_lable4 = Label(window, text= " \n\n  ", font= ("Times new roman" , 20), foreground= "green")
my_lable4.grid(column=0,row=4,columnspan=2)

button_q = Button(window, text= "Exit", font= ("Times new roman" , 16), foreground= "black",background="red" ,command=window.quit, width=20 )
button_0 = Button(window, text= "Currency list", font= ("Times new roman" , 14), foreground= "black", command= currency_list_window )
# list_currencies = Label(window, text = "    Currency    Exchange rate from USD\n")
# list_currencies.pack()
button_1 = Button(window, text= "Convert from USD to any currency", font= ("Times new roman" , 14), foreground= "purple", command= open_conversion_window, width=40, height=3 )
button_2 = Button(window, text= "Refresh data", font= ("Times new roman" , 14), foreground= "blue", command= refresh_data, width=40 )
button_3 = Button(window, text= "Export data to json file", font= ("Times new roman" , 14), foreground= "green", command= save_file, width=40)
button_4 = Button(window, text= "Convert from any currency to any currency", font= ("Times new roman" , 14), foreground= "purple", command= open_conversion_window_any, width=40, height=3 )

canvas.grid(column=0, row=1, columnspan=2)
button_q.grid(column=0,row=8, columnspan=2)
button_0.grid(column=0,row=2,columnspan=2)
button_1.grid(column=0,row=4)
button_2.grid(column=0,row=6)
button_3.grid(column=1,row=6)
button_4.grid(column=1,row=4)

window.mainloop()
