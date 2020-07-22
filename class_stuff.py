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

    def __init__(self, filename):
        pickle_in = open(filename,"rb")
        self.expenses = pickle.load(pickle_in)
        pickle_in.close()

    def save(self, filename):
        pickle_out = open(filename,"wb")
        pickle.dump(self.expenses, pickle_out)
        pickle_out.close()










