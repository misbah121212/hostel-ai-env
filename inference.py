import requests

BASE_URL = "http://localhost:7860"

def reset_env():
    response = requests.post(f"{BASE_URL}/reset")
    return response.json()

def take_step(action):
    response = requests.post(f"{BASE_URL}/step", json=action)
    return response.json()


if __name__ == "__main__":
    # Example run

    print("🔁 Resetting environment...")
    task = reset_env()
    print("Task:", task)

    task_type = task.get("task_type")

    # EASY
    if task_type == "easy":
        action = {"action": "Cleaning"}

    # MEDIUM
    elif task_type == "medium":
        action = {
            "category": "Cleaning",
            "priority": "High"
        }

    # HARD
    else:
        action = {
            "categories": ["Cleaning", "Electricity"],
            "priority": "Medium"
        }

    print("➡️ Taking action:", action)
    result = take_step(action)
    print("✅ Result:", result)