import os
import json
from pathlib import Path

class UserStorage:
    def __init__(self, filepath="userdata/transactions.json"):
        self.filepath = os.path.join(Path(__file__).parent.parent, filepath)
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"{self.filepath} does not exist. Please make sure the file is present.")
    def readfile(self):
        with open(self.filepath, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {"transactions": []}
    
    def writefile(self, data):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}")

    def save_transaction(self, transaction):
        data = self.readfile()
        data['transactions'].append(transaction)
        self.writefile(data)

    def remove_transaction(self, transaction):
        data = self.readfile()
        if transaction in data['transactions']:
            data['transactions'].remove(transaction)
            self.writefile(data)
