import random
from tasks import tasks

class HostelEnv:
    def __init__(self):
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(tasks)
        return {
            "complaint": self.current_task["complaint"],
            "task_type": self.current_task["type"]
        }

    def step(self, action):
        task_type = self.current_task["type"]
        reward = 0

        # EASY
        if task_type == "easy":
            if action.get("category") == self.current_task["label"]:
                reward = 1

        # MEDIUM
        elif task_type == "medium":
            correct_label = self.current_task["label"]
            correct_priority = self.current_task["priority"]

            if (action.get("category") == correct_label and
                action.get("priority") == correct_priority):
                reward = 1
            elif action.get("category") == correct_label:
                reward = 0.5

        # HARD
        elif task_type == "hard":
            correct_labels = set(self.current_task["labels"])
            predicted_labels = set(action.get("categories", []))
            correct_priority = self.current_task["priority"]

            if predicted_labels == correct_labels and action.get("priority") == correct_priority:
                reward = 1
            elif len(predicted_labels.intersection(correct_labels)) > 0:
                reward = 0.5

        return {
            "reward": reward,
            "done": True,
            "task_type": task_type,
            "correct_answer": self.current_task
        }