---
title: Hostel AI Environment
emoji: 🏠
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---
# 🏠 Hostel AI Environment (Agentic System)

An intelligent AI-powered environment designed to simulate real-world hostel issue management using agent-based decision-making.

---

## 🚀 Overview

This project models a **Hostel Complaint Management System** where an AI agent processes different types of complaints and predicts the correct action required.

The system supports **three difficulty levels**:

* 🟢 **Easy** → Simple classification
* 🟡 **Medium** → Classification + Priority
* 🔴 **Hard** → Multi-label classification + Priority

---

## 🎯 Problem Statement

In hostels, students often raise complaints like:

* “Fan not working”
* “Water leaking”
* “Room is dirty”

Managing these manually is inefficient.

👉 This project builds an **AI agent** that:

* Understands the complaint
* Classifies it into the correct category
* Assigns the correct priority
* Returns structured output

---

## 🧠 Agentic Approach

This system follows an **agent-based workflow**:

1. Environment generates a task (`/reset`)
2. Agent observes the complaint
3. Agent decides the correct action
4. Agent responds via (`/step`)
5. Environment evaluates and gives reward

---

## ⚙️ Tech Stack

* 🐍 Python
* ⚡ FastAPI
* 🐳 Docker
* 🤗 Hugging Face Spaces

---

## 📂 Project Structure

```
hostel-ai-env/
│── app.py           # FastAPI server
│── env.py           # Environment logic
│── tasks.py         # Task definitions (easy, medium, hard)
│── grader.py        # Evaluation logic
│── baseline.py      # Sample baseline agent
│── requirements.txt # Dependencies
│── Dockerfile       # Deployment config
│── README.md        # Documentation
```

---

## 🔄 API Workflow

### 🔹 1. Reset Environment

**GET /reset**

Returns a new task:

```json
{
  "task_type": "medium",
  "complaint": "Room extremely dirty",
  "priority": "High"
}
```

---

### 🔹 2. Submit Action

**POST /step**

---

### 🟢 Easy Task Input

```json
{
  "action": "Cleaning"
}
```

---

### 🟡 Medium Task Input

```json
{
  "category": "Cleaning",
  "priority": "High"
}
```

---

### 🔴 Hard Task Input

```json
{
  "categories": ["Cleaning", "Electricity"],
  "priority": "Medium"
}
```

---

### ✅ Response Example

```json
{
  "reward": 1,
  "done": true
}
```

---

## 🧪 Evaluation Logic

* ✔ Correct classification → Reward = 1
* ❌ Incorrect classification → Reward = 0
* ✔ Exact match required (case-sensitive)
* ✔ Hard tasks require ALL labels

---

## 🌍 Deployment

This project is deployed on **Hugging Face Spaces using Docker**.

👉 The API is publicly accessible and can be tested using Swagger UI (`/docs`).

---

## 💡 Key Features

✨ Multi-level task handling
✨ Real-world problem simulation
✨ Agent-environment interaction
✨ FastAPI-based API
✨ Fully deployable system

---

## 👥 Authors

* 👤 Iban Nadir Mondal
* 👤 Umme Misbah Sikandar

---

## 🏁 Conclusion

This project demonstrates how **AI agents can automate real-world problem classification systems** efficiently.

It combines:

* Decision-making
* Classification
* System design

into a single scalable solution.

---

## ⭐ Future Improvements

* 🔹 Integrate ML model for prediction
* 🔹 Add database for complaint tracking
* 🔹 Build frontend dashboard
* 🔹 Add real-time notifications

---

## 🔗 Links

* 🔹 GitHub Repository: *(Add your link here)*
* 🔹 Hugging Face Deployment: *(Add your link here)*

---

🔥 Built for Hackathon Submission 🚀
