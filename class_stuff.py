import pickle

class Expense():

    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        return self.amount - other.amount

class Database():

    expenses = []
    categories = []

    def __init__(self, expense_filename, category_filename):

        self.expense_filename = expense_filename
        self.category_filename = category_filename
        pickle_in = open(expense_filename,"rb")
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










