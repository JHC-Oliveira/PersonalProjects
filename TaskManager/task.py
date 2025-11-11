import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

class Task:
    def __init__(self, id, description, status,  date_created):
        self.id = id
        self.status = status
        self.description = description
        self.date_created = date_created or datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
    def to_dict(self):
        #It will convert the task to a dict to be able to save in json
        return {
            "id": self.id,
            "status": self.status,
            "description": self.description,
            "date_created": self.date_created
        }
    
    @classmethod
    def task_from_dict(cls, data):
        #Creates an instance of Task from a dict coming from json file
        return cls(
            id = data["id"],
            status = data["status"],
            description = data["description"],
            date_created = data["date_created"]
        )
        
class TaskManager:
    def __init__(self, data_file = DATA_FILE):
        self.data_file = data_file
        
    def load_tasks(self):
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, "r") as f:
            data = json.load(f)
            return[Task.task_from_dict(item) for item in data]