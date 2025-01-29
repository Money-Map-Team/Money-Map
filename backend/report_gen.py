from .transaction_handler import TransactionHandler
from .budget_handler import BudgetHandler

class ReportGen:
    def __init__(self):
        self.transaction_handler = TransactionHandler()
        self.budget_handler = BudgetHandler()

    def all_transactions(self):
        transactions = self.transaction_handler.storage.readfile().get('transactions', [])
        if not transactions:
            print("\nNo transactions found.")
            return

        print("\n--- Transactions ---")
        for idx, t in enumerate(transactions):
            print(f"{idx}. €{t['amount']} | {t['category']} | {t['description']} | {t['date']}")

    def view_balance(self):
        income_data = self.transaction_handler.income_storage.readfile()
        print("\n--- Balance ---")
        print(f"Current Balance: €{income_data.get('current_balance', 0)}")
        print(f"Last Added Income: €{income_data.get('last_added_income', 0)}")

    def view_budgets(self):
        budgets = self.budget_handler.storage.readfile().get('budgets', [])
        if not budgets:
            print("\nNo budgets set.")
            return

        print("\n--- Budgets ---")
        for budget in budgets:
            print(f"Category: {budget['category']} | Limit: €{budget['limit']}")

    def filter_transactions(self, filter_type, filter_value):
        transactions = self.transaction_handler.storage.readfile().get('transactions', [])
        
        if not transactions:
            print("\nNo transactions found.")
            return

        filtered_transactions = []
        if filter_type == 'date':
            filtered_transactions = [
                t for t in transactions
                if t['date'] == filter_value
            ]
        elif filter_type == 'category':
            filtered_transactions = [
                t for t in transactions
                if t['category'].lower() == filter_value.lower()
            ]
        elif filter_type == 'description':
            filtered_transactions = [
                t for t in transactions
                if filter_value.lower() in t['description'].lower()
            ]
        else:
            print("Invalid filter type.")
            return

        if not filtered_transactions:
            print(f"\nNo transactions found for {filter_type}: {filter_value}.")
            return

        print(f"\n--- Transactions filtered by {filter_type}: {filter_value} ---")
        for idx, t in enumerate(filtered_transactions):
            print(f"{idx}. €{t['amount']} | {t['category']} | {t['description']} | {t['date']}")

    def combined_report(self):
        self.all_transactions()
        self.view_balance()
        self.view_budgets()