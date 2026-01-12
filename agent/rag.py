import json

def load_knowledge_base():
    with open("data/knowledge_base.json", "r") as f:
        return json.load(f)

def answer_from_kb(query: str) -> str:
    kb = load_knowledge_base()
    pricing = kb["pricing"]
    policies = kb["policies"]

    if "basic" in query.lower():
        return str(pricing["Basic Plan"])

    if "pro" in query.lower():
        return str(pricing["Pro Plan"])

    if "refund" in query.lower():
        return policies["refund"]

    if "support" in query.lower():
        return policies["support"]

    return "Can you specify what you'd like to know about AutoStream?"
