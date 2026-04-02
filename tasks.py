import random

def get_task():
    tasks = [
        {
            "type": "easy",
            "complaint": "Light not working",
            "category": "Electricity",
            "priority": "Low"
        },
        {
            "type": "medium",
            "complaint": "Water leakage in bathroom",
            "category": "Plumbing",
            "priority": "Medium"
        },
        {
            "type": "hard",
            "complaint": "Room dirty and fan not working",
            "category": ["Cleaning", "Electricity"],
            "priority": "High"
        }
    ]

    return random.choice(tasks)