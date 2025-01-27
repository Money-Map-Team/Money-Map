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

        # Capture input and strip whitespace
        choice = input("Choose an option: ").strip()

        if not choice:
            print("\nError: No option selected. Please try again.")
            continue  # Skip the rest of the loop and show the menu again

        if choice == '1':  # Add Transaction
            try:
                amount = float(input("Enter transaction amount: "))
                category = input("Enter category: ").strip()
                description = input("Enter description: ").strip()
                transaction_handler.add_transaction(amount, category, description)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number for the amount.")
        elif choice == '2':  # Remove Transaction
            try:
                index = int(input("Enter transaction index to remove: "))
                transaction_handler.remove_transaction(index)
            except ValueError:
                print("Error: Invalid input. Please enter a valid index.")
        elif choice == '3':  # Add Income
            try:
                income_amount = float(input("Enter income amount: "))
                transaction_handler.add_income(income_amount)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number for the income.")
        elif choice == '4':  # Set Budget
            category = input("Enter budget category: ").strip()
            try:
                limit = float(input("Enter budget limit: "))
                budget_handler.set_budget(category, limit)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number for the limit.")
        elif choice == '5':  # Remove Budget
            category = input("Enter budget category to remove: ").strip()
            budget_handler.remove_budget(category)
        elif choice == '6':  # Generate Report
            report_gen.combined_report()
        elif choice == '7':  # Exit
            sys.exit()
        
        if choice not in ['1', '2', '3', '4','5','6','7',' ']:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
