import random
from tasks import tasks

class HostelEnv:
    def __init__(self):
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(tasks)
        return {"complaint": self.current_task["complaint"]}

    def step(self, action):
        correct = self.current_task["label"]

        if action == correct:
            reward = 1
        else:
            reward = 0

        return {
            "reward": reward,
            "done": True,
            "correct_answer": correct
        }