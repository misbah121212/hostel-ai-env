from fastapi import FastAPI
from env import HostelEnv

app = FastAPI()

env = HostelEnv()

# Home route
@app.get("/")
def home():
    return {"message": "Hostel AI Environment Running"}

# ✅ IMPORTANT: POST (not GET)
@app.post("/reset")
def reset():
    return env.reset()

# Step route
@app.post("/step")
def step(action: dict):
    return env.step(action)