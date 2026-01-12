def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    # 1. High intent FIRST
    if any(w in text for w in [
        "sign up", "signup", "try", "buy", "subscribe", "get started"
    ]):
        return "high_intent_lead"

    # 2. Casual greeting
    if any(w in text for w in ["hi", "hello", "hey"]):
        return "casual_greeting"

    # 3. Pricing / product inquiry
    if any(w in text for w in ["price", "pricing", "plan", "features", "pro", "basic"]):
        return "product_or_pricing_inquiry"

    return "product_or_pricing_inquiry"
