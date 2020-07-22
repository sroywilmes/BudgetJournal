from tkinter import *
from tkinter import ttk
from expense_class import Expense
from PIL import ImageTk,Image
from file_append import *

#testing function
def print_expense(eoi,amt,cat):
    print(eoi)
    print(amt)
    print(cat)
#new expense will be used to input a new expense and will bring up an interface to input information
#about the expense such as the amount, the category, etc

def display_expenses():
    pass

def new_category():
    category_fieldnames = ['category','subcategory1','subcategory2','subcategory3']
    #window setup
    window_new_category = Tk()
    window_new_category.title("New Category")
    #window_new_category.iconbitmap("placeholder.png")
    window_new_category.geometry("250x50")

    category_title = StringVar()
    entry_category = Entry(window_new_category, width=30, borderwidth=5)

    entry_category.pack()
    button_enter = Button(window_new_category, text="Enter", command=lambda: file_append('categories.csv', entry_category.get(), category_fieldnames)).pack()
    return entry_category.get()

def del_category():
    pass
def new_subcategory():
    pass
def root_setup(root):
    # setting up the basic window
    root.title("BudgetJournal")
    root.iconbitmap('icon_root.ico')
    root.geometry("800x600")

    #defining buttons
    button_new_expense = Button(root, text = "Enter new expense", width=20, command=new_expense)
    button_display_expenses = Button(root, text = "Display expenses", width=20, command=display_expenses)
    button_new_category = Button(root, text="New Category", width=20, command=new_category)
    button_exit = Button(root, text = "Exit", width=20, command=root.quit)

    #placing buttons in the window
    button_new_expense.grid(row = 0, column = 0)
    button_display_expenses.grid(row = 1, column = 0)
    button_new_category.grid(row=2, column=0)
    button_exit.grid(row=10, column=10)

def main():
    root = Tk()
    root_setup(root)
    root.mainloop()

main()