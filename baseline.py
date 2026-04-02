import requests

url = "http://127.0.0.1:8000"

# Step 1: get complaint
res = requests.get(f"{url}/reset")
data = res.json()

complaint = data["complaint"]
print("Complaint:", complaint)

# Step 2: simple AI logic
text = complaint.lower()

if "water" in text or "leak" in text or "toilet" in text:
    action = "Plumbing"
elif "fan" in text or "light" in text:
    action = "Electricity"
elif "dirty" in text or "dust" in text or "mess" in text:
    action = "Cleaning"
else:
    action = "Other"

print("Predicted:", action)

# Step 3: send action
result = requests.post(f"{url}/step", params={"action": action})

print("Result:", result.json())