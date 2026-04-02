from fastapi import FastAPI, Body
from env import HostelEnv

app = FastAPI()
env = HostelEnv()

@app.get("/")
def home():
    return {"message": "Hostel AI Environment Running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict = Body(...)):
    return env.step(action)