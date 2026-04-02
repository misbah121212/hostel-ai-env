TASKS = [

    # EASY
    {
        "type": "easy",
        "complaint": "Fan not working",
        "label": "Electricity"
    },
    {
        "type": "easy",
        "complaint": "Room is dirty",
        "label": "Cleaning"
    },

    # MEDIUM
    {
        "type": "medium",
        "complaint": "Room extremely dirty",
        "label": "Cleaning",
        "priority": "High"
    },
    {
        "type": "medium",
        "complaint": "Water leaking in bathroom",
        "label": "Plumbing",
        "priority": "Medium"
    },

    # HARD
    {
        "type": "hard",
        "complaint": "Room dirty and fan not working",
        "labels": ["Cleaning", "Electricity"],
        "priority": "Medium"
    },
    {
        "type": "hard",
        "complaint": "Water flooding and light not working",
        "labels": ["Plumbing", "Electricity"],
        "priority": "High"
    }
]