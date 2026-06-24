

import tkinter as tk
from tkinter import messagebox


# ---------- Calculation Functions ----------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# ---------- GUI Logic ----------

def get_numbers():
    """Read and validate the two number inputs from the entry boxes."""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        return num1, num2
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")
        return None, None


def calculate(operation):
    """Called when an operation button is pressed."""
    num1, num2 = get_numbers()
    if num1 is None or num2 is None:
        return

    try:
        if operation == "add":
            result = add(num1, num2)
            symbol = "+"
        elif operation == "subtract":
            result = subtract(num1, num2)
            symbol = "-"
        elif operation == "multiply":
            result = multiply(num1, num2)
            symbol = "*"
        elif operation == "divide":
            result = divide(num1, num2)
            symbol = "/"
        else:
            return

        label_result.config(text=f"{num1} {symbol} {num2} = {result}")

    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))


def clear_fields():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")


# ---------- GUI Setup ----------

window = tk.Tk()
window.title("Menu Driven Calculator")
window.geometry("400x350")
window.resizable(False, False)

title_label = tk.Label(window, text="Simple Calculator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Input frame
frame_inputs = tk.Frame(window)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Number 1:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_num1 = tk.Entry(frame_inputs, font=("Arial", 12), width=15)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Number 2:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_num2 = tk.Entry(frame_inputs, font=("Arial", 12), width=15)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Menu (operation buttons) frame
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Add (+)", width=12, font=("Arial", 11),
                     command=lambda: calculate("add"))
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_sub = tk.Button(frame_buttons, text="Subtract (-)", width=12, font=("Arial", 11),
                     command=lambda: calculate("subtract"))
btn_sub.grid(row=0, column=1, padx=5, pady=5)

btn_mul = tk.Button(frame_buttons, text="Multiply (*)", width=12, font=("Arial", 11),
                     command=lambda: calculate("multiply"))
btn_mul.grid(row=1, column=0, padx=5, pady=5)

btn_div = tk.Button(frame_buttons, text="Divide (/)", width=12, font=("Arial", 11),
                     command=lambda: calculate("divide"))
btn_div.grid(row=1, column=1, padx=5, pady=5)

# Result label
label_result = tk.Label(window, text="Result: ", font=("Arial", 14, "bold"), fg="blue")
label_result.pack(pady=15)

# Clear button
btn_clear = tk.Button(window, text="Clear", width=12, font=("Arial", 11), bg="lightgray",
                       command=clear_fields)
btn_clear.pack(pady=5)

window.mainloop()
