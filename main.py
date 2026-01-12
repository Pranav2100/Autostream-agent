from agent.graph import build_graph

graph = build_graph()
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "last_user_message": None
}

print("AutoStream AI Agent (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    state["last_user_message"] = user_input

    if state["intent"] == "high_intent_lead":
        if not state["name"]:
            state["name"] = user_input
        elif not state["email"]:
            state["email"] = user_input
        elif not state["platform"]:
            state["platform"] = user_input

    state = graph.invoke(state)
