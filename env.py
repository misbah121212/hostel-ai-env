from tasks import TASKS

class HostelEnv:
    def __init__(self):
        self.tasks = TASKS
        self.index = 0

    def reset(self):
        self.index = 0
        return self.tasks[self.index]

    def step(self, action):
        current_task = self.tasks[self.index]

        # simple grading logic
        reward = 0.0

        if action.get("priority", "").lower() == current_task["priority"].lower():
            reward += 0.5

        if action.get("category", "").lower() == current_task["category"].lower():
            reward += 0.5

        # move to next task
        self.index += 1
        done = self.index >= len(self.tasks)

        return {
            "reward": reward,
            "done": done
        }