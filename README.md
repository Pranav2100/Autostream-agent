# AutoStream — Agentic AI Sales Assistant

> A production-grade conversational AI agent that qualifies leads,
> retrieves pricing via RAG, and captures contact data —
> built with LangGraph, LangChain, and Python.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Stateful%20Agent-green)
![RAG](https://img.shields.io/badge/RAG-Local%20Knowledge%20Base-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🎬 Demo

https://github.com/user-attachments/assets/45d2f22d-f018-4e3e-b83e-ed1595c321ae

---

## What It Does

AutoStream is a stateful AI sales agent designed to mirror how a
real sales rep operates:

- **Intent detection** — identifies when a user is ready to buy
  and locks that intent across turns
- **Slot filling** — collects name, email, and creator platform
  through natural conversation
- **RAG-based retrieval** — answers pricing and policy questions
  from a local knowledge base, not LLM memory (no hallucinations)
- **Lead capture** — triggers backend lead storage only when all
  required fields are confirmed
- **Multi-channel ready** — designed for WhatsApp / API deployment
  via webhook integration

---

## Architecture

AutoStream uses **LangGraph** to build a stateful, single-node
agentic workflow — not a stateless chatbot.

User Input
│
▼
AgentState (persistent across turns)
│ ├── detected intent
│ ├── user name / email / platform
│ └── intent lock (prevents reset during slot filling)
│
├──► RAG Retrieval (local JSON knowledge base)
│ └── pricing, policies — deterministic, no hallucination
│
└──► Tool Execution (lead capture)
└── fires only when all slots are confirmed


**Why LangGraph over a simple chain?**
LangGraph gives explicit control over state transitions — critical
for multi-turn sales flows where intent, memory, and tool calls
must be coordinated safely and predictably.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent framework | LangGraph, LangChain |
| Language | Python 3.11 |
| Knowledge retrieval | Local JSON RAG |
| State management | LangGraph AgentState |
| Deployment target | FastAPI + WhatsApp Business Cloud API |

---

## Quickstart

```bash
git clone https://github.com/Pranav2100/Autostream-agent.git
cd Autostream-agent
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
python main.py
```

AutoStream AI Agent (type 'exit' to quit)
You:


---

## WhatsApp Deployment

The agent is designed for real-world deployment via
**WhatsApp Business Cloud API + webhooks**:

1. Host a FastAPI webhook endpoint to receive incoming messages
2. Route each message to the agent with a unique `session_id`
3. Persist `AgentState` per user across messages
4. On successful lead capture → forward to CRM or backend service

This architecture keeps agent logic channel-agnostic and scalable.

---

## Built By

**Pranav Jagtap** — AI/ML Engineer
[GitHub](https://github.com/Pranav2100) ·
[LinkedIn](https://linkedin.com/in/pranav--jagtap)
