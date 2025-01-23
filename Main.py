import sys
from backend.transaction_handler import TransactionHandler
from backend.budget_handler import BudgetHandler
from backend.report_gen import ReportGen

def main():
    transaction_handler = TransactionHandler()
    budget_handler = BudgetHandler()
    report_gen = ReportGen()

    while True:
        print("\n--- Money Map ---")
        print("1. Add Transaction")
        print("2. Remove Transaction")
        print("3. Add Income")
        print("4. Set Budget")
        print("5. Remove Budget")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':  # Add Transaction
            amount = float(input("Enter transaction amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            transaction_handler.add_transaction(amount, category, description)

        elif choice == '2':  # Remove Transaction
            index = int(input("Enter transaction index to remove: "))
            transaction_handler.remove_transaction(index)

        elif choice == '3':  # Add Income
            income_amount = float(input("Enter income amount: "))
            transaction_handler.add_income(income_amount)

        elif choice == '4':  # Set Budget
            category = input("Enter budget category: ")
            limit = float(input("Enter budget limit: "))
            budget_handler.set_budget(category, limit)

        elif choice == '5':  # Remove Budget
            category = input("Enter budget category to remove: ")
            budget_handler.remove_budget(category)

        elif choice == '6':  # Generate Report
            report_gen.combined_report()

        elif choice == '7':  # Exit
            sys.exit()

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()