# AutoStream – Social-to-Lead Conversational AI Agent

This project implements a **stateful, agentic Conversational AI** for a fictional SaaS company called **AutoStream**, which provides automated video editing tools for content creators.

The agent is designed to go beyond simple chat responses by:
- Understanding user intent
- Answering questions using a local knowledge base (RAG)
- Identifying high-intent users
- Capturing qualified leads via a controlled tool execution flow

---

## 🚀 Tech Stack

- **Language:** Python 3.9+
- **Framework:** LangChain + LangGraph
- **LLM:** GPT-4o-mini (pluggable)
- **Knowledge Retrieval:** Local JSON-based RAG
- **State Management:** LangGraph StateGraph

---

## 📁 Project Structure

autostream-agent/
│
├── data/
│ └── knowledge_base.json
│
├── agent/
│ ├── state.py # Conversation memory
│ ├── intents.py # Intent classification
│ ├── rag.py # Knowledge retrieval
│ ├── tools.py # Lead capture tool
│ └── graph.py # LangGraph workflow
│
├── main.py
├── requirements.txt
└── README.md


---

## 🧠 Agent Capabilities

### 1. Intent Identification
The agent classifies user input into:
- Casual greeting
- Product or pricing inquiry
- High-intent lead (ready to sign up)

### 2. RAG-Powered Knowledge Retrieval
The agent answers questions using a **local JSON knowledge base** containing:
- AutoStream pricing plans
- Feature details
- Company policies

This ensures **accurate, deterministic responses** with no hallucination.

### 3. Tool Execution – Lead Capture
When a user shows high intent, the agent:
1. Collects **name**
2. Collects **email**
3. Collects **creator platform**

Only after all three values are present does it trigger the mock tool:
```python
mock_lead_capture(name, email, platform)