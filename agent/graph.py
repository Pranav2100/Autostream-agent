from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.intents import detect_intent
from agent.rag import answer_from_kb
from agent.tools import mock_lead_capture


def agent_node(state: AgentState) -> AgentState:
    user_input = state.get("last_user_message", "")

    # 🔒 Lock intent once high intent is detected
    if state.get("intent") != "high_intent_lead":
        intent = detect_intent(user_input)
        state["intent"] = intent

    intent = state.get("intent")

    if intent == "casual_greeting":
        print("Agent: Hi! How can I help you today?")
        return state

    if intent == "product_or_pricing_inquiry":
        response = answer_from_kb(user_input)
        print(f"Agent: {response}")
        return state

    if intent == "high_intent_lead":
        if not state.get("name"):
            print("Agent: May I know your name?")
        elif not state.get("email"):
            print("Agent: Please share your email.")
        elif not state.get("platform"):
            print("Agent: Which creator platform do you use?")
        else:
            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )
        return state

    return state



def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")
    return graph.compile()
