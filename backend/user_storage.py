import json

class UserStorage:
    def __init__(self, filepath):
        self.filepath = filepath

    def readfile(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found.")
            return {} 
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON data in '{self.filepath}'.")
            return {}

    def writefile(self, data):
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)