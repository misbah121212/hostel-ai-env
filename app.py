from fastapi import FastAPI
from tasks import get_task
from grader import evaluate

app = FastAPI()

state = {}

@app.get("/")
def home():
    return {"message": "Hostel AI Environment Running"}

@app.post("/reset")
def reset():
    global state
    state = {"task": get_task()}
    return state["task"]

@app.post("/step")
def step(action: dict):
    global state
    correct = evaluate(state["task"], action)
    reward = 1 if correct else 0

    return {
        "reward": reward,
        "done": True,
        "task_type": state["task"]["type"],
        "correct_answer": state["task"]
    }