# agents/router.py
from agents.faq_agent import handle_faq
from agents.ticket_agent import handle_ticket
from agents.account_agent import handle_account

def route_query(intent: str, query):
    if intent == "faq":
        return handle_faq(query.message)
    elif intent == "ticket":
        return handle_ticket(query.user_id, query.message)
    elif intent == "account":
        return handle_account(query.user_id)
    elif intent == "blocked":
        return "Sorry, that kind of request is not allowed."

    return "Sorry, I didn't understand that."
