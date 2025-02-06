import tkinter as tk
from tkinter import messagebox

# Functions for calculator operations
def add():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result_var.set(f"{num1} + {num2} = {num1 + num2}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def sub():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result_var.set(f"{num1} - {num2} = {num1 - num2}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def mult():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result_var.set(f"{num1} x {num2} = {num1 * num2}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def div():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
        else:
            result_var.set(f"{num1} / {num2} = {num1 / num2:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

# Creating the main window
root = tk.Tk()
root.title("Calculator")

# Create the input fields
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=10, pady=10)

# Create buttons for operations
button_add = tk.Button(root, text="+", width=10, command=add)
button_add.grid(row=1, column=0, padx=10, pady=10)

button_sub = tk.Button(root, text="-", width=10, command=sub)
button_sub.grid(row=1, column=1, padx=10, pady=10)

button_mult = tk.Button(root, text="*", width=10, command=mult)
button_mult.grid(row=1, column=2, padx=10, pady=10)

button_div = tk.Button(root, text="/", width=10, command=div)
button_div.grid(row=2, column=0, padx=10, pady=10)

button_clear = tk.Button(root, text="Clear", width=10, command=clear)
button_clear.grid(row=2, column=1, padx=10, pady=10)

# Display result area
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, width=25, height=2)
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()