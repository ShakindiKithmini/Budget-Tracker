class Expense:



class ExpenseList:


class BudgetTracker:


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