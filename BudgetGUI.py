from tkinter import *
from tkinter import ttk
from tkcalendar import *
from class_stuff import *
from datetime import datetime
from datetime import timedelta

def root_setup(root, myDatabase):
    #basic window setup
    root.title("BudgetJournal")
    root.iconbitmap("icon_root.ico")
    root.geometry("800x600")

    #defining buttons
    button_new_expense = Button(root,padx = 10, pady = 5, text="Enter new expense", width=20, command=lambda: new_expense(myDatabase))
    button_display_expenses = Button(root,padx = 10, pady = 5, text="Display expenses", width=20, command=lambda: print_expenses(myDatabase))
    button_new_category = Button(root,padx = 10, pady = 5, text="New Category", width=20, command=lambda: new_category(myDatabase))
    button_view_month = Button(root,padx = 10, pady = 5, text="View Month", width=20, command=lambda: view_month(myDatabase))
    button_save = Button(root,padx = 10, pady = 5, text="Save", width=20, command=lambda: myDatabase.save(myDatabase.expense_filename, myDatabase.category_filename))
    button_exit = Button(root,padx = 10, pady = 5, text="Exit", width=20, command=root.quit)
    #displaying buttons
    button_new_expense.grid(row=0, column=0)
    button_display_expenses.grid(row=1, column=0)
    button_new_category.grid(row=2, column=0)
    button_view_month.grid(row=3,column=0)
    button_save.grid(row=4,column=0)
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
    now = datetime.now()
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
    date_entry = Calendar(window_new_expense, selectmode="day", year=now.year, month=now.month, day=now.day)

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
    name_field = Entry(window_new_category, width=13, borderwidth=2)
    limit_field = Entry(window_new_category, width=13, borderwidth=2)
    def cat_entry():
        new_cat = Category(name_field.get(), limit_field.get())
        myDatabase.categories.append(new_cat)
        window_new_category.destroy()
    enter_button = Button(window_new_category, text="Enter", command=cat_entry)

    #displaying the button/fieldS on screen
    name_label = Label(window_new_category, text= "Name of category:").grid(row=0,column=0)
    name_field.grid(row=0,column=1)
    limit_label = Label(window_new_category, text="Monthly limit: $").grid(row=1, column=0)
    limit_field.grid(row=1,column=1)
    enter_button.grid(row=2)

    #displaying current categories
    cat_header = Label(window_new_category, text="Current Categories:")
    cat_header.grid(row=2,column=1)
    for i in range(len(myDatabase.categories)):
        category_name = myDatabase.categories[i]
        cat_label = Label(window_new_category, text=category_name)
        cat_label.grid(row=i+3,column=1)

def edit_expense(myDatabase):
    pass

def category_tally(myDatabase, month, year, category):
    total = 0
    for i in range(len(myDatabase.expenses)):
        if myDatabase.expenses[i].category == category and myDatabase.expenses[i].date.month == month and myDatabase.expenses[i].date.year == year:
            total += myDatabase.expenses[i]
    return total

def number_to_month(number):
    if number == 1:
        return 'January'
    if number == 2:
        return 'February'
    if number == 3:
        return 'March'
    if number == 4:
        return 'April'
    if number == 5:
        return 'May'
    if number == 6:
        return 'June'
    if number == 7:
        return 'July'
    if number == 8:
        return 'August'
    if number == 9:
        return 'September'
    if number == 10:
        return 'October'
    if number == 11:
        return 'November'
    if number == 12:
        return 'December'
    else:
        return 'n2m conversion error'
def view_month(myDatabase):
    #initializing date and timedelta object
    display_date = datetime.today()
    one_day = timedelta(days=1)

    #basic window setup
    window_view_month = Tk()
    window_view_month.title("View Month")
    window_view_month.iconbitmap('icon_new_expense.ico')
    window_view_month.geometry("250x200")

    # label for the month header
    month_label = Label(window_view_month, text=number_to_month(display_date.month))

    #Defining functions to be used for buttons
    def next_month():
        display_date += one_day * 31
        display_month()

    def prev_month():
        display_date -= one_day * 27
        display_month()

    #function to display the current month
    def display_month():
        month_label.config(text=number_to_month(display_date.month))
        for i in range(len(myDatabase.categories)):
            category_label = Label(window_view_month, text=str(myDatabase.categories[i]) + ":")
            amount_string = "$" + str(category_tally(myDatabase, display_date.month, display_date.year, myDatabase.categories[i])) + " / $" + str(myDatabase.categories[i].limit)
            amount_label = Label(window_view_month, text=amount_string)

            category_label.grid(row=i+1,column=0)
            amount_label.grid(row=i + 1, column=1)

    next_button = Button(window_view_month, text = ">", command=next_month())
    prev_button = Button(window_view_month, text = "<", command=prev_month())

    #displaying things on screen
    display_month()
    prev_button.grid(row=0,column=0)
    month_label.grid(row=0,column=1)
    next_button.grid(row=0,column=2)
