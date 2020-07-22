from BudgetGUI import *
from class_stuff import *

def main():
    myDatabase = Database("expense_data.pickle", "category_data.pickle")
    myDatabase.save("expense_data.pickle", "category_data.pickle")
    root = Tk()
    root_setup(root, myDatabase)
    root.mainloop()

main()
