import os
import json

class user_storage:
    
    def readfile(filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                return json.load(file)
        
    def writefile(filepath,data):
        if os.path.exists(filepath):
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)