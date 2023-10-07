#!/usr/bin/env python
# coding: utf-8

# # Calculator App: Making a calculator with Addition , Subtraction , Multiplication and Deletion functionality of 2 numbers



import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Calculator")

# Create input fields for the numbers and the operation
num1_entry = tk.Entry(window, width=10)
num1_entry.grid(row=0, column=0, padx=5, pady=5)

operator_label = tk.Label(window, text="")
operator_label.grid(row=0, column=1, padx=5, pady=5)

num2_entry = tk.Entry(window, width=10)
num2_entry.grid(row=0, column=2, padx=5, pady=5)

# Create functions to perform calculations
def add():
  num1 = float(num1_entry.get())
  num2 = float(num2_entry.get())
  result = num1 + num2
  operator_label.config(text="+")
  result_label.config(text=str(result))

def subtract():
  num1 = float(num1_entry.get())
  num2 = float(num2_entry.get())
  result = num1 - num2
  operator_label.config(text="-")
  result_label.config(text=str(result))

def multiply():
  num1 = float(num1_entry.get())
  num2 = float(num2_entry.get())
  result = num1 * num2
  operator_label.config(text="*")
  result_label.config(text=str(result))

def divide():
  num1 = float(num1_entry.get())
  num2 = float(num2_entry.get())
  if num2 == 0:
    result_label.config(text="Error: division by zero")
  else:
    result = num1 / num2
    operator_label.config(text="/")
    result_label.config(text=str(result))

# Create buttons for the operations
add_button = tk.Button(window, text="+", command=add)
add_button.grid(row=1, column=0, padx=5, pady=5)

subtract_button = tk.Button(window, text="-", command=subtract)
subtract_button.grid(row=1, column=1, padx=5, pady=5)

multiply_button = tk.Button(window, text="*", command=multiply)
multiply_button.grid(row=1, column=2, padx=5, pady=5)

divide_button = tk.Button(window, text="/", command=divide)
divide_button.grid(row=1, column=3, padx=5, pady=5)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

# Run the Tkinter event loop
window.mainloop()






