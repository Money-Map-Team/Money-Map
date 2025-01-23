from .user_storage import UserStorage

class BudgetHandler:
    def __init__(self):
        self.storage = UserStorage(filepath="userdata/budgets.json")

    def set_budget(self, category, limit):
        data = self.storage.readfile()
        budgets = data.get('budgets', [])

        for budget in budgets:
            if budget['category'] == category:
                print(f"Budget for category '{category}' already exists.")
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