import os
from .user_storage import UserStorage

class BudgetHandler:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        userdata_path = os.path.join(base_dir, "userdata", "budgets.json") 
        self.storage = UserStorage(filepath=userdata_path)

    def set_budget(self, category, limit):
        if limit <= 0:
            print("Error: Budget limit must be a positive number.")
            return

        data = self.storage.readfile()
        budgets = data.get('budgets', [])

        for budget in budgets:
            if budget['category'] == category:
                print(f"Budget for category '{category}' already exists. Updating limit to €{limit}.")
                budget['limit'] = limit
                self.storage.writefile(data)
                return

        budgets.append({'category': category, 'limit': limit})
        data['budgets'] = budgets
        self.storage.writefile(data)
        print(f"Budget of €{limit} set for category '{category}'.")

    def remove_budget(self, category):
        data = self.storage.readfile()
        budgets = data.get('budgets', [])

        for i, budget in enumerate(budgets):
            if budget['category'] == category:
                budgets.pop(i)
                data['budgets'] = budgets
                self.storage.writefile(data)
                print(f"Budget for category '{category}' removed.")
                return

        print(f"No budget found for category '{category}'.")
