user_history = {
    "user123": {"avg": 800}
}

def detect_risk(user_id, data):
    if data["action"] == "send_money":
        amount = data["amount"]
        avg = user_history[user_id]["avg"]

        if amount > avg * 2:
            return "High Risk"
        elif amount > avg:
            return "Medium Risk"

    return "Safe"
