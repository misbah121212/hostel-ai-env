tasks = [
    # EASY TASKS
    {"type": "easy", "complaint": "Fan not working", "label": "Electricity"},
    {"type": "easy", "complaint": "Room is dirty", "label": "Cleaning"},
    {"type": "easy", "complaint": "Water leaking in bathroom", "label": "Plumbing"},

    # MEDIUM TASKS
    {
        "type": "medium",
        "complaint": "Water flooding room",
        "label": "Plumbing",
        "priority": "High"
    },
    {
        "type": "medium",
        "complaint": "Light flickering continuously",
        "label": "Electricity",
        "priority": "Medium"
    },
    {
        "type": "medium",
        "complaint": "Room extremely dirty for days",
        "label": "Cleaning",
        "priority": "High"
    },

    # HARD TASKS
    {
        "type": "hard",
        "complaint": "Water leaking and lights not working",
        "labels": ["Plumbing", "Electricity"],
        "priority": "High"
    },
    {
        "type": "hard",
        "complaint": "Room dirty and fan not working",
        "labels": ["Cleaning", "Electricity"],
        "priority": "Medium"
    }
]