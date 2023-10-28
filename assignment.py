class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

class ExpenseList:
    def __init__(self, expenses=[]):
        self.expenses = expenses

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        self.expenses.pop(index)

    def view_expense_list(self):
        print("Expense List:")
        for expense in self.expenses:
            print(f"{expense.date} | {expense.category} | {expense.amount}")

class BudgetTracker:
    def __init__(self, monthly_income=0, expense_list=ExpenseList()):
        self.monthly_income = monthly_income
        self.expense_list = expense_list

    def add_monthly_income(self, amount):
        self.monthly_income += amount

    def add_expense(self, date, category, amount):
        expense = Expense(date, category, amount)
        self.expense_list.add_expense(expense)

    def view_expense_list(self):
        self.expense_list.view_expense_list()

    def remove_expense(self, index):
        self.expense_list.remove_expense(index)

    def calculate_remaining_income(self):
        total_expenses = 0
        for expense in self.expense_list.expenses:
            total_expenses += expense.amount
        remaining_income = self.monthly_income - total_expenses
        return remaining_income

    def exit(self):
        print("Thank you!")

def main():
    budget_tracker = BudgetTracker()

    # Displays a menu of options to the user to enter their choice
    while True:
        print("Budget Tracker Menu:")
        print("1. Add monthly income")
        print("2. Add expense")
        print("3. View expense list")
        print("4. Remove expense")
        print("5. Calculate remaining income")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter your monthly income:LKR. "))
            budget_tracker.add_monthly_income(amount)
        elif choice == 2:
            date = (input("Enter the date of the expense: "))
            category = input("Enter the category of the expense: ")
            amount = float(input("Enter the amount of the expense:LKR. "))
            budget_tracker.add_expense(date, category, amount)
        elif choice == 3:
            budget_tracker.view_expense_list()
        elif choice == 4:
            index = int(input("Enter the index of the expense to remove: "))
            budget_tracker.remove_expense(index)
        elif choice == 5:
            remaining_income = budget_tracker.calculate_remaining_income()
            print("Your remaining income is:LKR.", remaining_income)
        elif choice == 6:
            budget_tracker.exit()
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
