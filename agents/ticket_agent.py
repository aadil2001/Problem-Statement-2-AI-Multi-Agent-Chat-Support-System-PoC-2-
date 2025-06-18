
from database.db import log_ticket

def handle_ticket(user_id, message: str) -> str:
    log_ticket(user_id, message)
    return "Your complaint has been registered. We'll get back to you."
