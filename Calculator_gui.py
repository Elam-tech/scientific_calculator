import tkinter as tk
import math
from tkinter import ttk

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("340x580")

expression = ""


def press(key):
    global expression
    if key == "^":
        expression += "**"
    elif key == "√":
        expression += "math.sqrt("
    else:
        expression += str(key)
    input_text.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result  
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")


exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "ZAR": 18.2,
    "GBP": 0.78,
    "JPY": 156.3,
    "CAD": 1.36,
    "AUD": 1.51,
    "INR": 83.2,
    "CNY": 7.25,
    "CHF": 0.87,
    "NZD": 1.62,
    "BRL": 5.47,
    "MXN": 18.03
}

def open_currency_converter():
    converter_window = tk.Toplevel(root)
    converter_window.title("Currency Converter")
    converter_window.geometry("380x250")

   
    tk.Label(converter_window, text="Amount:", font=('arial', 12)).pack(pady=5)
    amount_var = tk.StringVar()
    amount_entry = tk.Entry(converter_window, font=('arial', 14), textvariable=amount_var)
    amount_entry.pack(pady=5)

   
    current_value = input_text.get()
    if current_value and current_value not in ["Error", ""]:
        amount_var.set(current_value)

   
    tk.Label(converter_window, text="Convert from:", font=('arial', 12)).pack(pady=5)
    from_currency = ttk.Combobox(converter_window, values=list(exchange_rates.keys()), font=('arial', 14))
    from_currency.pack(pady=5)
    from_currency.set("USD")  

    
    tk.Label(converter_window, text="Convert to:", font=('arial', 12)).pack(pady=5)
    to_currency = ttk.Combobox(converter_window, values=list(exchange_rates.keys()), font=('arial', 14))
    to_currency.pack(pady=5)
    to_currency.set("EUR")  

    
    result_label = tk.Label(converter_window, text="", font=('arial', 14))
    result_label.pack(pady=10)

    
    def update_conversion(*args):
        try:
            amount = float(amount_var.get())
            from_cur = from_currency.get().upper()
            to_cur = to_currency.get().upper()

            if from_cur in exchange_rates and to_cur in exchange_rates:
                usd_amount = amount / exchange_rates[from_cur]
                converted = usd_amount * exchange_rates[to_cur]
                result_label.config(text=f"{amount} {from_cur} = {round(converted, 2)} {to_cur}")
            else:
                result_label.config(text="Unsupported currency!")
        except:
            result_label.config(text="")

   
    amount_var.trace_add("write", update_conversion)
    from_currency.bind("<<ComboboxSelected>>", update_conversion)
    to_currency.bind("<<ComboboxSelected>>", update_conversion)


input_text = tk.StringVar()
input_field = tk.Entry(root, textvariable=input_text, font=('arial', 18), bd=10, insertwidth=2,
                       width=18, borderwidth=4, relief='ridge', justify='right')
input_field.pack(ipady=15)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '^', '+'],
    ['√', '(', ')', '='],
    ['C'],
    ['Currency']
]

for row in buttons:
    row_frame = tk.Frame(root)
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        if btn_text == "=":
            btn = tk.Button(row_frame, text=btn_text, font=('arial', 18), height=2, width=5,
                            command=equalpress)
        elif btn_text == "C":
            btn = tk.Button(row_frame, text=btn_text, font=('arial', 18), height=2, width=22,
                            command=clear)
        elif btn_text == "Currency":
            btn = tk.Button(row_frame, text=btn_text, font=('arial', 18), height=2, width=22,
                            command=open_currency_converter)
        else:
            btn = tk.Button(row_frame, text=btn_text, font=('arial', 18), height=2, width=5,
                            command=lambda b=btn_text: press(b))
        btn.pack(side='left', expand=True, fill='both')

root.mainloop()
