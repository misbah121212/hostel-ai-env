import requests

url = "http://127.0.0.1:8000"

for _ in range(5):
    res = requests.get(f"{url}/reset")
    data = res.json()

    complaint = data["complaint"]
    task_type = data["task_type"]

    print("\nComplaint:", complaint)
    print("Task Type:", task_type)

    text = complaint.lower()

    categories = []

    if "water" in text:
        categories.append("Plumbing")
    if "light" in text or "fan" in text:
        categories.append("Electricity")
    if "dirty" in text:
        categories.append("Cleaning")

    categories = list(set(categories))

    # EASY
    if task_type == "easy":
        action = {"category": categories[0] if categories else "Other"}

    # MEDIUM
    elif task_type == "medium":
        priority = "High" if "flood" in text or "extremely" in text else "Medium"
        action = {
            "category": categories[0] if categories else "Other",
            "priority": priority
        }

    # HARD
    elif task_type == "hard":
        priority = "High" if "leaking" in text else "Medium"
        action = {
            "categories": categories,
            "priority": priority
        }

    print("Action:", action)

    result = requests.post(f"{url}/step", json=action)

    print("Result:", result.json())