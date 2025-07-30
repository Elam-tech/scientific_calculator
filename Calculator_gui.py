import tkinter as tk
import math


root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("320x460")

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
    except Exception as e:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")


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
    ['C']
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
        else:
            btn = tk.Button(row_frame, text=btn_text, font=('arial', 18), height=2, width=5,
                            command=lambda b=btn_text: press(b))
        btn.pack(side='left', expand=True, fill='both')

root.mainloop()

