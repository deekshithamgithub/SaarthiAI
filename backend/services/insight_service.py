transactions = {
    "user123": [
        {"amount": 200, "type": "food"},
        {"amount": 1500, "type": "shopping"},
        {"amount": 300, "type": "food"},
        {"amount": 2000, "type": "electronics"}
    ]
}

def get_insights(user_id):
    txns = transactions[user_id]

    total = sum(t["amount"] for t in txns)

    suggestions = []

    if total > 3000:
        suggestions.append("You are spending too much this week.")

    food = sum(t["amount"] for t in txns if t["type"] == "food")
    if food > 500:
        suggestions.append("Reduce food expenses.")

    return suggestions