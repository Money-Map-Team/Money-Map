#In-Progress
class report_gen:
    def __init__(self):
        self.budget = {}

    def update_budget(self, month, amount):
        self.budget[month] = amount
        self.show_changes()

    def show_changes(self):
        print("Updated Budget:")
        for month, amount in self.budget.items():
            print(f"{month}: ${amount}")
