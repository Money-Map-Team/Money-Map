import json
import os

class UserStorage:
    def __init__(self, filepath):
        self.filepath = filepath
        self._initialize_file()

    def _initialize_file(self):
        """Initialize the file with default data if it doesn't exist."""
        # Ensure the directory exists
        directory = os.path.dirname(self.filepath)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Initialize default data if the file is missing
        if not os.path.exists(self.filepath):
            default_data = {}
            if "transactions" in self.filepath:
                default_data = {"transactions": []}
            elif "income" in self.filepath:
                default_data = {"Total income": 0, "Income added": 0}
            elif "budgets" in self.filepath:
                default_data = {"budgets": []}
            self.writefile(default_data)

    def readfile(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file is empty or corrupted, reset it
            print(f"Initializing/resetting file: {self.filepath}")
            self._initialize_file()
            return self.readfile()

    def writefile(self, data):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error writing to {self.filepath}: {e}")
