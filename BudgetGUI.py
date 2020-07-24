from tkinter import *
from tkinter import ttk
from tkcalendar import *
from class_stuff import *
from datetime import datetime
from datetime import timedelta
from decimal import *

def root_setup(root, myDatabase):
    #basic window setup
    root.title("BudgetJournal")
    root.iconbitmap("icon_root.ico")
    root.geometry("800x600")

    #defining buttons
    button_new_expense = Button(root,padx = 10, pady = 5, text="Enter new expense", width=20, command=lambda: new_expense(myDatabase))
    button_edit_expense = Button(root, padx=10, pady=5, text="Edit Expense", width=20, command=lambda: choose_expense(myDatabase))
    button_display_expenses = Button(root,padx = 10, pady = 5, text="Display expenses", width=20, command=lambda: display_expenses(myDatabase))
    button_new_category = Button(root,padx = 10, pady = 5, text="New Category", width=20, command=lambda: new_category(myDatabase))
    button_edit_category = Button(root,padx = 10, pady = 5, text="Edit Category", width=20, command=lambda: choose_category(myDatabase))
    button_view_month = Button(root,padx = 10, pady = 5, text="View Month", width=20, command=lambda: view_month(myDatabase))

    def push_save_and_exit(myDatabase):
        myDatabase.save(myDatabase.expense_filename, myDatabase.category_filename)
        root.quit()
    button_save_and_exit = Button(root,padx = 10, pady = 5, text="Save and Exit", width=20, command=lambda: push_save_and_exit(myDatabase))

    #displaying buttons
    button_new_expense.grid(row=0, column=0)
    button_edit_expense.grid(row=1,column=0)
    button_display_expenses.grid(row=2, column=0)
    button_new_category.grid(row=3, column=0)
    button_edit_category.grid(row=4,column=0)
    button_view_month.grid(row=5,column=0)
    button_save_and_exit.grid(row=6,column=0)


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



#Both the choose_expense function and the edit_expense function will be used for the edit expense button
def choose_expense(myDatabase):
    #setting up the basic window
    window_choose_expense = Tk()
    window_choose_expense.title("Choose Expense")
    window_choose_expense.iconbitmap('icon_new_expense.ico')
    window_choose_expense.geometry("710x400")

    #DEFINING BUTTONS/LABELS/FIELDS ON SCREEN
    #defining the header
    header_text = ' {:8}'.format("Amount") + \
                 '| {:20}'.format("Category") + \
                 '| {:8}'.format("Date") + \
                 '| {:<}'.format("Decription")
    header_label = Label(window_choose_expense, text= header_text, font=("Courier New", 8), anchor=W,width=100)

    #Defining the option menu to select the choice
    expense_choice = StringVar()
    expense_strings = []
    expense_menu = Listbox(window_choose_expense, width=100, font=('Courier New', 8))
    for i in range(len(myDatabase.expenses)):
        expense_strings.append(str(myDatabase.expenses[i]))
        expense_menu.insert(i, expense_strings[i])
    expense_menu.select_set(0)


    #Defining the button to actually edit the choice
    def push_enter_button(myDatabase):
        chosen_expense_tuple = expense_menu.curselection()
        chosen_expense_index = chosen_expense_tuple[0]
        window_choose_expense.destroy()
        edit_expense(myDatabase, myDatabase.expenses[chosen_expense_index], chosen_expense_index)
        # choose_expense(myDatabase)

    enter_button = Button(window_choose_expense,
                          text="Edit Chosen Expense",
                          command=lambda: push_enter_button(myDatabase))

    #Displaying everything on screen
    header_label.grid(row=0, column=0)
    expense_menu.grid(row=1,column=0,columnspan=10)
    enter_button.grid(row=2,column=0)

#edit expense uses the same window code as new_expense but instead of making a new one and appending it, it edits an existing one
def edit_expense(myDatabase, expense, chosen_expense_index):
    # basic window setup
    window_edit_expense = Tk()
    window_edit_expense.title("Edit Expense")
    window_edit_expense.iconbitmap('icon_new_expense.ico')
    window_edit_expense.geometry("280x400")

    # DEFINING BUTTONS/FIELDS ON SCREEN

    # Drop down Combobox for Categories
    selected_category = StringVar()
    selected_category.set("Choose a category")
    category_drop = ttk.Combobox(window_edit_expense, values=myDatabase.categories, width=10)
    category_drop.set(expense.category)
    category_drop_label = Label(window_edit_expense, text="Category:")

    # Entry field for the amount
    amount_entry_field = Entry(window_edit_expense, width=13, borderwidth=2)
    amount_entry_field.insert(0, expense.amount)
    amount_entry_field_label = Label(window_edit_expense, text="Amount: ")

    # Entry field for description
    description_entry_field = Text(window_edit_expense, width=28, height=4)
    description_entry_field_label = Label(window_edit_expense, text="Enter a description of the expense if necessary:")
    description_entry_field.insert(INSERT, expense.description)

    # Date Entry Widget for the date
    date_list = expense.date.split("/")
    date_entry = Calendar(window_edit_expense, selectmode="day", year=int(date_list[2]), month=int(date_list[0]), day=int(date_list[1]))

    # Enter Button
    def exp_entry():

        myDatabase.expenses[chosen_expense_index].edit_expense(amount_entry_field.get(), category_drop.get(), date_entry.get_date(),
                              description_entry_field.get('1.0', END))
        window_edit_expense.destroy()
        choose_expense(myDatabase)
    enter_button = Button(window_edit_expense, text="Enter", command=exp_entry)

    #Delete button
    def push_delete_button(myDatabase):
        myDatabase.delete_expense(chosen_expense_index)
        window_edit_expense.destroy()
        choose_expense(myDatabase)
    delete_button = Button(window_edit_expense, text="DELETE", command=lambda: push_delete_button(myDatabase))

    # DISPLAYING BUTTONS/FIELDS ON THE SCREEN
    category_drop_label.grid(row=0, column=0)
    category_drop.grid(row=0, column=1)
    amount_entry_field_label.grid(row=1, column=0)
    amount_entry_field.grid(row=1, column=1)
    date_entry.grid(row=2, columnspan=2)
    description_entry_field_label.grid(row=3, columnspan=2)
    description_entry_field.grid(row=4, columnspan=2)
    enter_button.grid(row=5,column=0)
    delete_button.grid(row=5,column=1)

def display_expenses(myDatabase):
    window_display_expenses = Tk()
    window_display_expenses.geometry("800x400")
    Label(window_display_expenses, text = "Amount",width = 10).grid(row=0,column=0)
    Label(window_display_expenses, text="Category",width = 10).grid(row=0, column=1)
    Label(window_display_expenses, text="Date",width = 10).grid(row=0, column=2)
    for i in range(len(myDatabase.expenses)):
        cat = myDatabase.expenses[i].category
        date = myDatabase.expenses[i].date
        if myDatabase.expenses[i].description == '\n':
            desc = "None"
        else:
            desc = myDatabase.expenses[i].description
        amtLabel = Label(window_display_expenses,text="$" + myDatabase.expenses[i].amount,width = 10)
        catLabel = Label(window_display_expenses, text=myDatabase.expenses[i].category,width = 10)
        dateLabel = Label(window_display_expenses, text=myDatabase.expenses[i].date,width = 10)

        amtLabel.grid(row=i+1,column=0)
        catLabel.grid(row=i+1, column=1)
        dateLabel.grid(row=i+1, column=2)



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

def choose_category(myDatabase):
    #setting up the basic window
    window_choose_category = Tk()
    window_choose_category.title("Choose Expense")
    window_choose_category.iconbitmap('icon_new_expense.ico')
    window_choose_category.geometry("250x400")

    #DEFINING BUTTONS/LABELS/FIELDS ON SCREEN
    #defining the header
    header_text = 'Categories'
    header_label = Label(window_choose_category, text= header_text, font=("Courier New", 8), anchor=W,width=20)

    #Defining the option menu to select the choice
    category_choice = StringVar()
    category_strings = []
    category_menu = Listbox(window_choose_category, width=20, font=('Courier New', 8))
    for i in range(len(myDatabase.categories)):
        category_strings.append(str(myDatabase.categories[i]))
        category_menu.insert(i, category_strings[i])
    category_menu.select_set(0)


    #Defining the button to actually edit the choice
    def push_enter_button(myDatabase):
        chosen_category_tuple = category_menu.curselection()
        chosen_category_index = chosen_category_tuple[0]
        window_choose_category.destroy()
        edit_category(myDatabase, chosen_category_index)
        # choose_expense(myDatabase)

    enter_button = Button(window_choose_category,
                          text="Edit Chosen Category",
                          command=lambda: push_enter_button(myDatabase))

    exit_button = Button(window_choose_category,
                         text="Done Editing",
                         command=window_choose_category.destroy)
    #Displaying everything on screen
    header_label.grid(row=0, column=0)
    category_menu.grid(row=1,column=0,columnspan=10)
    enter_button.grid(row=2,column=0)
    exit_button.grid(row=3,column=0)

def edit_category(myDatabase, chosen_category_index):
    # basic window setup
    window_edit_category = Tk()
    window_edit_category.title("Edit Category")
    window_edit_category.iconbitmap('icon_new_expense.ico')
    window_edit_category.geometry("250x200")


    # defining entry field and enter button, as well as the function that executes when you press the enter button
    name_field = Entry(window_edit_category, width=13, borderwidth=2)
    name_field.insert(INSERT, str(myDatabase.categories[chosen_category_index].name))
    limit_field = Entry(window_edit_category, width=13, borderwidth=2)
    limit_field.insert(INSERT, str(myDatabase.categories[chosen_category_index].limit))

    def push_edit_category_button(myDatabase):
        old_category = myDatabase.categories[chosen_category_index]
        myDatabase.categories[chosen_category_index].edit_category(name_field.get(), limit_field.get())
        for i in range(len(myDatabase.expenses)):
            if old_category.name == myDatabase.expenses[i].category:
                myDatabase.expenses[i].category = name_field.get()
        window_edit_category.destroy()
        choose_category(myDatabase)

    edit_category_button = Button(window_edit_category, text="Enter", command=lambda: push_edit_category_button(myDatabase))
    def push_delete_category_button(myDatabase):
        myDatabase.delete_category(chosen_category_index)
        window_edit_category.destroy()
        choose_category()
    delete_category_button = Button(window_edit_category, text="DELETE", command=lambda: push_edit_category_button(myDatabase))

    # displaying the button/fields on screen
    name_label = Label(window_edit_category, text="Name of category:").grid(row=0, column=0)
    name_field.grid(row=0, column=1)
    limit_label = Label(window_edit_category, text="Monthly limit: $").grid(row=1, column=0)
    limit_field.grid(row=1, column=1)
    edit_category_button.grid(row=2)


#The category tally function is be used in the view month function for each category
def category_tally(myDatabase, month, year, category):
    total = 0
    for i in range(len(myDatabase.expenses)):
        if str(myDatabase.expenses[i].category) == str(category) and str(myDatabase.expenses[i].date[0]) == str(month):
            total += eval(myDatabase.expenses[i].amount)
    total_string = round(total, 2)
    print(total_string)
    return total_string

#used in the view month category (there may already be something like this built in somewhere *shrug*)
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

#Defining functions to be used for buttons (I know using global variables is bad but I couldn't figure it out)
def next_month():
    global display_date
    one_day = timedelta(days=1)
    display_date += one_day *30

def prev_month():
    global display_date
    one_day = timedelta(days=1)
    display_date -= one_day * 30

def view_month(myDatabase):
    #initializing date and timedelta object
    global display_date
    display_date = datetime.today()


    #basic window setup
    window_view_month = Tk()
    window_view_month.title("View Month")
    window_view_month.iconbitmap('icon_new_expense.ico')
    window_view_month.geometry("250x200")

    # label for the month header
    month_label = Label(window_view_month, width=10,text=number_to_month(display_date.month))

    def next():
        next_month()
        display_month()

    def prev():
        prev_month()
        display_month()


    #function to display the current month
    def display_month():
        month_label.config(text=number_to_month(display_date.month))
        month_label.update()
        for i in range(len(myDatabase.categories)):
            category_label = Label(window_view_month, text=str(myDatabase.categories[i]) + ":")
            tally_string = "$" + str(category_tally(myDatabase, display_date.month, display_date.year, myDatabase.categories[i]))
            limit_string = str(myDatabase.categories[i].limit)
            if limit_string != '':
                tally_string += " / $" + limit_string
            amount_label = Label(window_view_month, text=tally_string)

            category_label.grid(row=i+1,column=0)
            amount_label.grid(row=i + 1, column=1)

    next_button = Button(window_view_month, text = ">", command=next)
    prev_button = Button(window_view_month, text = "<", command=prev)

    #displaying things on screen
    display_month()
    prev_button.grid(row=0,column=0)
    month_label.grid(row=0,column=1)
    next_button.grid(row=0,column=2)
