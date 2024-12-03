

import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear entry
def clear_entry():
    entry.delete(0, tk.END)  # Clear the text

# Function to backspace the wrong entry on the calculator
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])  # Clear the current text i.e backspace

# Function to Evaluate/Calculate the result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # To calculate the expression
        entry.delete(0, tk.END)  # Clear the text
        entry.insert(tk.END, str(result))  # Show the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")  # To show the message as "ERROR" when expression is uncalculable

# To set up the main window of the application
root = tk.Tk()
root.title("My Calculator")  # Creating the application name
root.geometry("400x500")  # Function to set the size of the application
root.config(bg="#E0BFB8")  # Function to set the color of the application

# Function to create the entry widget to display the expression and result
entry = tk.Entry(root, width=20, font=('Arial', 20), justify=tk.RIGHT, bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)

# Button layout (buttons are arranged in a grid as follows)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Place the buttons in the grid
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root, text=button, padx=20, pady=20, font=('Arial', 16),
        command=lambda b=button: button_click(b) if b != '=' else calculate(),
        bg="#61dafb", fg="#282c35"
    ).grid(row=row_val, column=col_val, sticky="nsew")
    
    col_val += 1
    if col_val > 3:  # Move to next row after 4 columns
        col_val = 0
        row_val += 1

# Buttons for CLR (clear) and backspace
tk.Button(
    root, text='CLR', padx=20, pady=20, font=('Arial', 16),
    command=clear_entry, bg="#ff6b6b", fg="#282c35"
).grid(row=row_val, column=col_val, sticky="nsew")

col_val += 1

tk.Button(
    root, text='⌫', padx=20, pady=20, font=('Arial', 16),
    command=backspace, bg="#ff6b6b", fg="#282c35"
).grid(row=row_val, column=col_val, sticky="nsew")

# Configure rows and columns to expand evenly
for i in range(5):  # 5 rows (0 to 4) to be adjustable
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # 4 columns (0 to 3) to be adjustable
    root.grid_columnconfigure(i, weight=1)

# Main loop
root.mainloop()