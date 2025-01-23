#In-Progress
from backend.user_storage import UserStorage
from backend.transaction_handler import TransactionHandler

class ReportGen:
    def __init__(self):
        self.current_balance = 0
        self.storage = UserStorage(filepath="userdata/transactions.json") 
        self.budget = UserStorage(filepath="userdata/budgets.json") 


    def all_transactions(self):
        data = self.storage.readfile()
        transactions = data.get('transactions', [])
        
        if not transactions:
            print("No transactions found.")
            return
        
        print("\nTransactions List:")
        for i, transaction in enumerate(transactions):
            print(f"{i}. Amount: {transaction['amount']} | Category: {transaction['category']} | Description: {transaction['description']}")


    def total_budget(self):
        data = self.storage.readfile()
        budget = data.get('budget', [])

        if not budget:
            print("No Amount available")
            return
   
        print("\nTotal Amount: ")
