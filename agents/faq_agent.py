def handle_faq(message: str) -> str:
    if "return policy" in message:
        return "Our return policy allows returns within 30 days."
    elif "reset password" in message:
        return "You can reset your password from the login page."
    return "I'm here to help! Please ask a specific question."
