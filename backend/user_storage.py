import json
import os

class UserStorage:
    def __init__(self, filepath):
        self.filepath = filepath
        self._initialize_file()

    def _initialize_file(self):
        """Initialize the file with default data if it doesn't exist."""
        directory = os.path.dirname(self.filepath)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        if not os.path.exists(self.filepath):
            self.writefile(self._default_data())

    def _default_data(self):
        """Return default data structure based on file type."""
        if "transactions" in self.filepath:
            return {"transactions": []}
        elif "income" in self.filepath:
            return {
                "total_income": 0,  # Hidden from users
                "current_balance": 0,
                "last_added_income": 0
            }
        elif "budgets" in self.filepath:
            return {"budgets": []}
        return {}

    def readfile(self):
        try:
            with open(self.filepath, 'r', encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"File corrupted: {self.filepath}. Resetting...")
            self._initialize_file()
            return self._default_data()

    def writefile(self, data):
        try:
            with open(self.filepath, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error writing to {self.filepath}: {e}")