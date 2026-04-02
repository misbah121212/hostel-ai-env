# 🏠 Hostel AI Environment (OpenEnv Hackathon)

## 📌 Overview

This project simulates a **real-world hostel complaint management system** where an AI agent learns to classify and prioritize issues.

The environment follows the **OpenEnv standard** with:

* `reset()` → provides a new complaint
* `step(action)` → evaluates the agent’s response

---

## 🎯 Problem Statement

In hostels, students raise complaints like:

* Water leakage 🚿
* Electrical issues ⚡
* Cleaning problems 🧹

The goal is to build an AI agent that:

1. **Classifies the complaint correctly**
2. **Assigns priority (for complex cases)**

---

## 🧠 Tasks Implemented

### 🟢 Easy Tasks

Agent must classify complaint into correct category:

| Complaint                 | Correct Category |
| ------------------------- | ---------------- |
| Fan not working           | Electricity      |
| Room is dirty             | Cleaning         |
| Water leaking in bathroom | Plumbing         |

👉 Reward:

* Correct → **+1**
* Wrong → **0**

---

### 🟡 Medium Tasks

Agent must:

1. Classify category
2. Assign priority

| Complaint                     | Category    | Priority |
| ----------------------------- | ----------- | -------- |
| Water flooding room           | Plumbing    | High     |
| Light flickering continuously | Electricity | Medium   |
| Room extremely dirty for days | Cleaning    | High     |

👉 Reward:

* Correct category + priority → **+1**
* Only category correct → **+0.5**
* Wrong → **0**

---

## ⚙️ Environment Design

### 🔹 Observation (from `/reset`)

```json
{
  "complaint": "Water leaking in bathroom",
  "task_type": "easy"
}
```

---

### 🔹 Action (to `/step`)

#### Easy Task:

```json
{
  "category": "Plumbing"
}
```

#### Medium Task:

```json
{
  "category": "Plumbing",
  "priority": "High"
}
```

---

### 🔹 Response

```json
{
  "reward": 1,
  "done": true,
  "task_type": "medium",
  "correct_answer": {...}
}
```

---

## 🚀 How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run server

```bash
uvicorn app:app --reload
```

### 3. Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Support

Run using Docker:

```bash
docker build -t hostel-ai-env .
docker run -p 7860:7860 hostel-ai-env
```

---

## 🤖 Baseline Agent

A simple rule-based agent is implemented in `baseline.py`:

* Uses keyword matching
* Handles both easy and medium tasks
* Produces reproducible results

---

## 📊 Evaluation

* Rewards range from **0 to 1**
* Medium tasks include **partial rewards**
* Deterministic grading

---

## 🌍 Deployment

The app is deployed on Hugging Face Spaces and accessible via:

* `/docs` for testing API
* Public URL for evaluation

---

## ✨ Features

✔ Real-world scenario (hostel complaints)
✔ Multi-level tasks (easy → medium)
✔ Partial reward system
✔ API-based environment
✔ Dockerized deployment

---

## 📌 Future Improvements

* Add **hard tasks** (multi-issue complaints)
* NLP-based understanding instead of keywords
* Priority escalation logic

---

## 👩‍💻 Authors

- Iban Nadir Mondal  
- Umme Misbah Sikandar