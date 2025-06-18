# agents/intent_classifier.py
import openai

def classify_intent(message: str) -> str:
    message = message.lower()
    if "return" in message or "price" in message or "how to" in message or "what is" in message:
        return "faq"
    elif "complaint" in message or "not working" in message or "ticket" in message or "issue" in message:
        return "ticket"
    elif "account" in message or "balance" in message or "profile" in message or "subscription" in message:
        return "account"
    return "faq"
