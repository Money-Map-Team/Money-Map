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
        """Load the current balance from income.json."""
        income_data = self.income_storage.readfile()
        self.current_balance = income_data.get('current_balance', 0)
        return self.current_balance

    def add_transaction(self, amount, category, description):
        if amount <= 0:
            print("Error: Transaction amount must be a positive number.")
            return

        # Check if the transaction exceeds the current balance
        income_data = self.income_storage.readfile()
        if amount > income_data['current_balance']:
            print(f"\nWarning: Your transaction of €{amount} will exceed your current balance of €{income_data['current_balance']}.")
            print("Please make a transaction under your current balance.")
            return

        # Check budget limits
        budgets = self.budget_storage.readfile().get('budgets', [])
        for budget in budgets:
            if budget['category'].lower() == category.lower():
                if amount > budget['limit']:
                    print(f"\nWarning: This €{amount} transaction will exceed the {category} budget limit of €{budget['limit']}!")
                    confirm = input("Do you want to proceed anyway? (y/n): ").strip().lower()
                    if confirm != 'y':
                        print("Transaction canceled.")
                        return

        # Proceed with transaction if checks pass
        date = datetime.now().strftime("%Y-%m-%d")
        transaction_data = self.storage.readfile()
        transaction_data['transactions'].append({
            'amount': amount,
            'category': category,
            'description': description,
            'date': date
        })
        self.storage.writefile(transaction_data)

        # Update balance
        income_data['current_balance'] -= amount
        self.income_storage.writefile(income_data)
        print(f"\nTransaction of €{amount} added. New balance: €{income_data['current_balance']}")
        
    def edit_transaction(self, index, new_amount=None, new_category=None, new_description=None, new_date=None):
        transaction_data = self.storage.readfile()
        transactions = transaction_data.get('transactions', [])

        if not (0 <= index < len(transactions)):
            print("Error: Invalid transaction index.")
            return

        transaction = transactions[index]

        # Update fields if new values are provided
        if new_amount is not None:
            if new_amount <= 0:
                print("Error: Transaction amount must be a positive number.")
                return
            # Adjust balance based on the difference
            income_data = self.income_storage.readfile()
            difference = new_amount - transaction['amount']
            if income_data['current_balance'] - difference < 0:
                print("Error: This edit would result in a negative balance.")
                return
            transaction['amount'] = new_amount
            income_data['current_balance'] -= difference
            self.income_storage.writefile(income_data)

        if new_category is not None:
            transaction['category'] = new_category.strip()

        if new_description is not None:
            transaction['description'] = new_description.strip()

        if new_date is not None:
            transaction['date'] = new_date.strip()

        self.storage.writefile(transaction_data)
        print(f"Transaction {index} updated successfully.")

    def add_income(self, amount):
        if amount <= 0:
            print("Error: Income amount must be a positive number.")
            return

        income_data = self.income_storage.readfile()
        # Update hidden total_income
        income_data['total_income'] += amount
        # Update visible values
        income_data['current_balance'] += amount
        income_data['last_added_income'] = amount
        self.income_storage.writefile(income_data)
        print(f"Income of €{amount} added. New balance: €{income_data['current_balance']}")
        
    def edit_income(self, new_income):
        if new_income < 0:
            print("Error: Income cannot be negative.")
            return

        income_data = self.income_storage.readfile()
        old_income = income_data.get('total_income', 0)
        
        # Calculate the difference and update the balance
        difference = new_income - old_income
        income_data['total_income'] = new_income
        income_data['current_balance'] += difference
        self.income_storage.writefile(income_data)
        
        print(f"Income updated to €{new_income}. Current balance adjusted to €{income_data['current_balance']}.")

    def remove_transaction(self, index):
        transaction_data = self.storage.readfile()
        transactions = transaction_data['transactions']
        
        if 0 <= index < len(transactions):
            removed = transactions.pop(index)
            # Refund to balance
            income_data = self.income_storage.readfile()
            income_data['current_balance'] += removed['amount']
            self.income_storage.writefile(income_data)
            self.storage.writefile(transaction_data)
            print(f"Transaction removed. Balance updated to €{income_data['current_balance']}")
        else:
            print("Invalid index")