USE_LLM = False  # keep False for demo / no API key

def detect_intent_llm(user_input: str) -> str:
    # Lazy import — only happens if USE_LLM = True
    from agent.llm import get_llm

    llm = get_llm()

    prompt = f"""
Classify the user intent into one of these:
- casual_greeting
- product_or_pricing_inquiry
- high_intent_lead

User message: "{user_input}"

Respond with ONLY the intent label.
"""

    response = llm.invoke(prompt)
    return response.content.strip()


def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    # 🔥 High intent FIRST
    if any(w in text for w in ["try", "sign up", "buy", "subscribe", "get started"]):
        return "high_intent_lead"

    if any(w in text for w in ["hi", "hello", "hey"]):
        return "casual_greeting"

    if any(w in text for w in ["price", "pricing", "plan", "features", "pro", "basic"]):
        return "product_or_pricing_inquiry"

    # Optional LLM fallback
    if USE_LLM:
        return detect_intent_llm(user_input)

    return "product_or_pricing_inquiry"