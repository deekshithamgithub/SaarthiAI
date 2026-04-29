import re

def process_text(text):
    text = text.lower()

    if "send" in text:
        amount = re.findall(r'\d+', text)
        return {
            "action": "send_money",
            "amount": int(amount[0]) if amount else 0,
            "receiver": "Ravi"
        }

    elif "balance" in text:
        return {"action": "check_balance"}

    return {"action": "unknown"}
