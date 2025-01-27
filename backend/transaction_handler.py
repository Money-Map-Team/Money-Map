from .user_storage import UserStorage
from datetime import datetime
import os

class TransactionHandler:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        userdata_dir = os.path.join(project_root, "userdata")

        self.storage = UserStorage(filepath=os.path.join(userdata_dir, "transactions.json"))
        self.income_storage = UserStorage(filepath=os.path.join(userdata_dir, "income.json"))
        self.budget_storage = UserStorage(filepath=os.path.join(userdata_dir, "budgets.json"))
        self.current_balance = self._load_balance()

    def _load_balance(self):
        transactions_data = self.storage.readfile()
        transactions = transactions_data.get('transactions', [])
        total_expenses = sum(t['amount'] for t in transactions)

        income_data = self.income_storage.readfile()
        total_income = income_data.get('Total income', 0)

        self.current_balance = total_income - total_expenses
        return self.current_balance

    def add_transaction(self, amount, category, description):
        if amount <= 0:
            print("Error: Transaction amount must be a positive number.")
            return

        date = datetime.now().strftime("%Y-%m-%d")
        data = self.storage.readfile()
        transactions = data.get('transactions', [])

        new_transaction = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': date
        }

        budgets = self.budget_storage.readfile().get('budgets', [])
        for budget in budgets:
            if budget['category'] == category:
                if amount > budget['limit']:
                    print(f"Warning: Transaction amount exceeds budget limit for '{category}'.")
                break

        transactions.append(new_transaction)
        data['transactions'] = transactions
        self.storage.writefile(data)
        print(f"Transaction of €{amount} for '{category}' added successfully.")
        self.current_balance -= amount

    def add_income(self, amount):
        if amount <= 0:
            print("Error: Income amount must be a positive number.")
            return

        data = self.income_storage.readfile()

        total_income = data.get('Total income', 0) + amount
        data['Total income'] = total_income
        data['Income added'] = amount

        self.income_storage.writefile(data)
        print(f"Income of €{amount} added successfully.")
        self.current_balance += amount

    def remove_transaction(self, index):
        data = self.storage.readfile()
        transactions = data.get('transactions', [])

        if 0 <= index < len(transactions):
            removed_transaction = transactions.pop(index)
            amount = removed_transaction['amount']
            data['transactions'] = transactions
            self.storage.writefile(data)
            print(f"Transaction {removed_transaction} removed successfully.")
            self.current_balance += amount
        else:
            print("Invalid transaction index.")
