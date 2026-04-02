def evaluate(task, action):
    try:
        # EASY
        if task["type"] == "easy":
            return action.get("category") == task["category"]

        # MEDIUM
        elif task["type"] == "medium":
            return (
                action.get("category") == task["category"]
                and action.get("priority") == task["priority"]
            )

        # HARD
        elif task["type"] == "hard":
            return (
                set(action.get("categories", [])) == set(task["category"])
                and action.get("priority") == task["priority"]
            )

    except:
        return False

    return False