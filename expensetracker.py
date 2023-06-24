import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

allExpenses = {}

class ExpenseTracker():
    def __init__(self):
        self.data = allExpenses

    def addToAllExpenses(self, amount, category):
        allExpenses.update(amount,category)
         #   amount = 123
         #category =
            #return amount
        # return category

class App(tk.Tk):

    def __init__(self, tracker):
        tk.Tk.__init__(self)
        self.title = 'Expense tracker'
        self.expense_tracker = tracker

        self.configure(background = 'white')
        self.geometry("500x200")

        # Label
        self.intro_label = Label(self, text='Expense tracker', fg='green', borderwidth=3)
        self.intro_label.config(font=('Arial', 15, 'bold'))
        self.intro_label.place(x=150, y=20)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)

        # dropdown
        self.categories = ("groceries", "rent", "health", "fun", "clothes", "transport")
        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.categories_dropdown = ttk.Combobox(self, textvariable=self.categories,
                                                   values=list(self.categories), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)

        # placing
        self.categories_dropdown.place(x=30, y=140)
        self.amount_field.place(x=30, y=100)

        # Add expense button
        self.addexpense_button = Button(self, text="Add expense", fg="black", command=self.addtolist)
        self.addexpense_button.config(font=('Arial', 10, 'bold'))
        self.addexpense_button.place(x=225, y=135)

        # Show summary button
        self.showsummary_button = Button(self, text="Show summary", fg="black", command=self.summarize)
        self.showsummary_button.config(font=('Arial', 10, 'bold'))
        self.showsummary_button.place(x=225, y=100)

    def addtolist(self):
        allExpenses.update({self.amount_field.get(): self.categories_dropdown.get()})
        print(allExpenses)

    def summarize(self):
        values = list(allExpenses.keys())
        names = list(allExpenses.values())

        plt.bar(names, values)
        plt.bar(x=values, height = names)
        plt.show()

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

if __name__ == '__main__':
    tracker = ExpenseTracker()
    App(tracker)
    mainloop()