from backend.user_storage import UserStorage

class TransactionHandler:
    def __init__(self):
        self.storage = UserStorage(filepath="userdata/transactions.json")  

    def add_transaction(self, amount, category, description):
        transaction = {
            'amount': f"€{amount:.2f}",
            'category': category,
            'description': description
        }
        self.storage.save_transaction(transaction)

    def remove_transaction(self, index):
        try:
            transactions = self.storage.readfile()['transactions']
            removed_transaction = transactions.pop(index)
            self.storage.remove_transaction(removed_transaction)
        except IndexError:
            raise ValueError("Invalid index. Transaction not found.")

    def view_transactions(self):
        return self.storage.readfile()['transactions']
