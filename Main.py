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
        print("3. Filter Transactions")
        print("4. Edit Transaction")
        print("5. Add Income")
        print("6. Edit Income")
        print("7. Set Budget")
        print("8. Remove Budget")
        print("9. Generate Report")
        print("10. Exit")

        choice = input("Choose an option: ").strip()

        if not choice:
            print("\nError: No option selected. Please try again.")
            continue

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
        elif choice == '3':  # Filter Transactions
            print("\nFilter by:")
            print("1. Date")
            print("2. Category")
            print("3. Description")
            filter_choice = input("Choose a filter option: ").strip()

            if filter_choice == '1':  # Date
                filter_value = input("Enter date (YYYY-MM-DD): ").strip()
                report_gen.filter_transactions('date', filter_value)
            elif filter_choice == '2':  # Category
                filter_value = input("Enter category: ").strip()
                report_gen.filter_transactions('category', filter_value)
            elif filter_choice == '3':  # Description
                filter_value = input("Enter description: ").strip()
                report_gen.filter_transactions('description', filter_value)
            else:
                print("Invalid filter option.")
        elif choice == '4':  # Edit Transaction
            try:
                index = int(input("Enter transaction index to edit: "))
                print("Leave fields blank to keep current values.")
                new_amount = input("Enter new amount: ").strip()
                new_category = input("Enter new category: ").strip()
                new_description = input("Enter new description: ").strip()
                new_date = input("Enter new date (YYYY-MM-DD): ").strip()

                # Convert new_amount to float if provided
                new_amount = float(new_amount) if new_amount else None

                transaction_handler.edit_transaction(
                    index,
                    new_amount=new_amount,
                    new_category=new_category,
                    new_description=new_description,
                    new_date=new_date
                )
            except ValueError:
                print("Error: Invalid input. Please enter a valid number for the amount.")
        elif choice == '5':  # Add Income
            try:
                income_amount = float(input("Enter income amount: "))
                transaction_handler.add_income(income_amount)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number for the income.")
        elif choice == '6':  # Edit Income
            try:
                new_income = float(input("Enter new total income: "))
                transaction_handler.edit_income(new_income)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number for the income.")
        elif choice == '7':  # Set Budget
            category = input("Enter budget category: ").strip()
            try:
                limit = float(input("Enter budget limit: "))
                budget_handler.set_budget(category, limit)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number for the limit.")
        elif choice == '8':  # Remove Budget
            category = input("Enter budget category to remove: ").strip()
            budget_handler.remove_budget(category)
        elif choice == '9':  # Generate Report
            report_gen.combined_report()
        elif choice == '10':  # Exit
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()