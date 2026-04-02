# 🏨 Hostel Complaint AI Environment

This project is an AI environment designed to simulate real-world hostel complaint management.

## 📌 Objective
The goal is to train and evaluate AI agents that can classify hostel complaints into appropriate categories.

## 🧠 Task Description

### Easy Task:
Classify complaints into:
- Plumbing
- Electricity
- Cleaning
- Other

Example:
Input: "Fan not working"  
Output: Electricity

## ⚙️ Environment Design

- `reset()` → returns a new complaint
- `step(action)` → evaluates agent prediction and returns reward
- Reward = 1 for correct, 0 for incorrect

## 🤖 Baseline Agent

A simple rule-based agent is provided that classifies complaints using keyword matching.

## 🚀 Deployment

The environment is deployed using FastAPI and Docker on HuggingFace Spaces.

## 📊 Evaluation

- Correct classification → reward = 1
- Incorrect classification → reward = 0

## 🌍 Real-World Relevance

This simulates hostel maintenance systems where complaints need to be categorized and resolved efficiently.