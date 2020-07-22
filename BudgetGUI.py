from tkinter import *
from tkinter import ttk
from tkcalendar import *
from class_stuff import *

def root_setup(root, myDatabase):
    #basic window setup
    root.title("BudgetJournal")
    root.iconbitmap("icon_root.ico")
    root.geometry("800x600")

    #defining buttons
    button_new_expense = Button(root,padx = 10, pady = 5, text="Enter new expense", width=20, command=lambda: new_expense(myDatabase))
    button_display_expenses = Button(root,padx = 10, pady = 5, text="Display expenses", width=20, command=lambda: print_expenses(myDatabase))
    button_new_category = Button(root,padx = 10, pady = 5, text="New Category", width=20, command=lambda: new_category(myDatabase))
    button_save = Button(root,padx = 10, pady = 5, text="Save", width=20, command=lambda: myDatabase.save(myDatabase.expense_filename, myDatabase.category_filename))
    button_exit = Button(root,padx = 10, pady = 5, text="Exit", width=20, command=root.quit)

    #displaying buttons
    button_new_expense.grid(row=0, column=0)
    button_display_expenses.grid(row=1, column=0)
    button_new_category.grid(row=2, column=0)
    button_save.grid(row=3,column=0)
    button_exit.grid(row=10, column=0)

def print_expenses(myDatabase):
    window_display_expenses = Tk()
    for i in range(len(myDatabase.expenses)):
        amt = myDatabase.expenses[i].amount
        cat = myDatabase.expenses[i].category
        date = myDatabase.expenses[i].date
        if myDatabase.expenses[i].description == '\n':
            desc = "None"
        else:
            desc = myDatabase.expenses[i].description
        expense_data_string = str(i) + "  Amount: $" + amt + "  Category: " + cat + "  Date: " +  date + "  Description: " +  desc
        expense_data = Label(window_display_expenses, text = expense_data_string)
        expense_data.pack()
def new_expense(myDatabase):
    #basic window setup
    window_new_expense = Tk()
    window_new_expense.title("New Expense")
    window_new_expense.iconbitmap('icon_new_expense.ico')
    window_new_expense.geometry("280x400")

    #DEFINING BUTTONS/FIELDS ON SCREEN

    #Drop down Combobox for Categories
    selected_category = StringVar()
    selected_category.set("Choose a category")
    category_drop = ttk.Combobox(window_new_expense, values=myDatabase.categories, width=10)
    category_drop_label = Label(window_new_expense, text="Category:")

    #Entry field for the amount
    amount_entry_field = Entry(window_new_expense, width=13, borderwidth=2 )
    amount_entry_field_label = Label(window_new_expense, text="Amount: ")

    #Entry field for description
    description_entry_field = Text(window_new_expense, width= 28, height=4)
    description_entry_field_label = Label(window_new_expense, text="Enter a description of the expense if necessary:")

    #Date Entry Widget for the date
    date_entry = Calendar(window_new_expense, selectmode="day", year=2020, month=7, day=22)

    #Enter Button
    def exp_entry():
        new_expense = Expense(amount_entry_field.get(), category_drop.get(), date_entry.get_date(), description_entry_field.get('1.0', END))
        myDatabase.expenses.append(new_expense)
        window_new_expense.destroy()
    enter_button = Button(window_new_expense, text="Enter", command=exp_entry)

    #DISPLAYING BUTTONS/FIELDS ON THE SCREEN
    category_drop_label.grid(row=0, column=0)
    category_drop.grid(row=0,column=1)

    amount_entry_field_label.grid(row=1,column=0)
    amount_entry_field.grid(row=1,column=1)

    date_entry.grid(row=2, columnspan=2)

    description_entry_field_label.grid(row=3,columnspan=2)
    description_entry_field.grid(row=4,columnspan=2)

    enter_button.grid(row=5)


def new_category(myDatabase):
    # basic window setup
    window_new_category = Tk()
    window_new_category.title("New Category")
    window_new_category.iconbitmap('icon_new_expense.ico')
    window_new_category.geometry("250x200")

    #defining entry field and enter button, as well as the function that executes when you press the enter button
    entry_field = Entry(window_new_category, width=13, borderwidth=2)

    def cat_entry():
        myDatabase.categories.append(entry_field.get())
        window_new_category.destroy()
    enter_button = Button(window_new_category, text="Enter", command=cat_entry)

    #displaying the button/field on screen
    entry_field.grid(row=0)
    enter_button.grid(row=1)

    #displaying current categories
    cat_header = Label(window_new_category, text="Current Categories:")
    cat_header.grid(row=0,column=1)
    for i in range(len(myDatabase.categories)):
        category_name = myDatabase.categories[i]
        cat_label = Label(window_new_category, text=category_name)
        cat_label.grid(row=i+1,column=1)




