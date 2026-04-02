from fastapi import FastAPI
from env import HostelEnv

app = FastAPI()
env = HostelEnv()

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: str):
    return env.step(action)