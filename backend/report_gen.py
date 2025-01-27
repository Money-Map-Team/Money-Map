from .transaction_handler import TransactionHandler
from .budget_handler import BudgetHandler

class ReportGen:
    def __init__(self):
        self.transaction_handler = TransactionHandler()
        self.budget_handler = BudgetHandler()

    def all_transactions(self):
        transactions = self.transaction_handler.storage.readfile().get('transactions', [])

        if not transactions:
            print("No transactions found.")
            return

        print("\n--- Transactions List ---")
        for i, transaction in enumerate(transactions):
            print(f"{i}. Amount: €{transaction['amount']} | Category: {transaction['category']} | Description: {transaction['description']} | Date: {transaction['date']}")

    def view_balance(self):
        print("\n--- Balance ---")
        print(f"Total Income: €{self.transaction_handler.income_storage.readfile().get('Total income', 0)}")
        print(f"Total Expenses: €{sum(t['amount'] for t in self.transaction_handler.storage.readfile().get('transactions', []))}")
        print(f"Current Balance: €{self.transaction_handler.current_balance}")

    def view_budgets(self):
        budgets = self.budget_handler.storage.readfile().get('budgets', [])

        if not budgets:
            print("\nNo budgets set.")
            return

        print("\n--- Budgets ---")
        for budget in budgets:
            print(f"Category: {budget['category']} | Limit: €{budget['limit']}")

    def combined_report(self):
        self.all_transactions()
        self.view_balance()
        self.view_budgets()
