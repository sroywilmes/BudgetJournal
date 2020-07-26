import pickle
import datetime
from datetime import timedelta
class Expense():
    date = datetime.date.today()
    def __init__(self):
        self.amount=0
        self.category
        self.date=datetime()
        self.description = ''

    def __init__(self, amount=None, category=None, date=None, description=None):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        return self.amount - other.amount

    def get_list_string(self):
        return '| ${:>8.2f}'.format(self.amount) + \
               '| {:25}'.format(str(self.category)) + \
               '| {:14}'.format(self.date.strftime("%b %d %Y")) + \
               '| {:<}'.format(str(self.description))

    def edit_expense(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def date_string_to_datetime(self):
        new_date = self.date.split("/")
        self.date = datetime.date(int(new_date[2]) + 2000,int(new_date[0]),int(new_date[1]))

    def amount_string_to_float(self):
        self.amount = round(float(self.amount),2)
class Category():

    def __init__(self, name):
        self.name = name
        self.limit = 0
    def __init__(self, name, limit, index):
        self.name = name
        self.limit = limit
        self.index = index

    def __str__(self):
        return self.name
    def compare(self, other):
        if self.name == other.name and self.limit == other.limit:
            return True
        return False
    def edit_category(self, name, limit):
        self.name = name
        self.limit = limit

class Database():

    expenses = []
    categories = []

    def __init__(self, expense_filename, category_filename):
        self.expense_filename = expense_filename
        self.category_filename = category_filename
        try:
            pickle_in = open(expense_filename,"rb")
            self.expenses = pickle.load(pickle_in)
            pickle_in.close()

            pickle_in = open(category_filename, "rb")
            self.categories = pickle.load(pickle_in)
            pickle_in.close()

        except:
            pickle_out = open(expense_filename, "wb")
            pickle.dump(self.expenses, pickle_out)
            pickle_out.close()

            pickle_out = open(category_filename, "wb")
            pickle.dump(self.categories, pickle_out)
            pickle_out.close()

            pickle_in = open(expense_filename, "rb")
            self.expenses = pickle.load(pickle_in)
            pickle_in.close()

            pickle_in = open(category_filename, "rb")
            self.categories = pickle.load(pickle_in)
            pickle_in.close()


    def save(self, expense_filename, category_filename):
        pickle_out = open(expense_filename,"wb")
        pickle.dump(self.expenses, pickle_out)
        pickle_out.close()

        pickle_out = open(category_filename, "wb")
        pickle.dump(self.categories, pickle_out)
        pickle_out.close()

    def delete_expense(self, index):
        self.expenses.pop(index)

    def delete_category(self, index):
        self.categories.pop(index)

    def sort_expenses_amount(self):
        self.expenses = sorted(self.expenses, key=lambda expense: float(expense.amount))

    def sort_expenses_category(self):
        self.expenses = sorted(self.expenses, key=lambda expense: expense.category)

    def sort_expenses_date(self):
        self.expenses = sorted(self.expenses, key=lambda expense: expense.date)

    def sort_expenses_description(self):
        self.expenses = sorted(self.expenses, key=lambda expense: expense.description)



    def convert_expense_amounts(self):
        for i in range(len(self.expenses)):
            if type(self.expenses[i].amount) == str:
                self.expenses[i].amount_string_to_float()



