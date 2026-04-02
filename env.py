import random
from tasks import TASKS

class HostelEnv:
    def __init__(self):
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(TASKS)
        return {
            "task_type": self.current_task["type"],
            "complaint": self.current_task["complaint"],
            "priority": self.current_task.get("priority", None)
        }

    def step(self, action):
        if not self.current_task:
            return {"error": "Call reset first"}

        reward = 0
        done = True

        task_type = self.current_task["type"]

        # EASY
        if task_type == "easy":
            if action.get("action") == self.current_task["label"]:
                reward = 1

        # MEDIUM
        elif task_type == "medium":
            if (
                action.get("category") == self.current_task["label"]
                and action.get("priority") == self.current_task["priority"]
            ):
                reward = 1

        # HARD
        elif task_type == "hard":
            if (
                set(action.get("categories", [])) == set(self.current_task["labels"])
                and action.get("priority") == self.current_task["priority"]
            ):
                reward = 1

        return {
            "reward": reward,
            "done": done,
            "task_type": task_type,
            "correct_answer": self.current_task
        }