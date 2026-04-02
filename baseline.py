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

    # CATEGORY LOGIC
    if "water" in text or "leak" in text:
        category = "Plumbing"
    elif "fan" in text or "light" in text:
        category = "Electricity"
    elif "dirty" in text:
        category = "Cleaning"
    else:
        category = "Other"

    action = {"category": category}

    # MEDIUM TASK → ADD PRIORITY
    if task_type == "medium":
        if "flood" in text or "extremely" in text:
            priority = "High"
        else:
            priority = "Medium"

        action["priority"] = priority

    print("Action:", action)

    result = requests.post(f"{url}/step", json=action)

    print("Result:", result.json())