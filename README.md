1️⃣ How to Run the Project Locally:
Prerequisites
Python 3.9+ (recommended: Python 3.11)
Git 

Steps
# Clone the repository
git clone https://github.com/Pranav2100/Autostream-agent.git
cd Autostream-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the agent
python main.py





The agent will start in CLI mode:
AutoStream AI Agent (type 'exit' to quit)
You:

2️⃣ Architecture Explanation:

This project uses LangGraph to build a stateful, agentic conversational workflow rather than a stateless chatbot. LangGraph was chosen because it provides explicit control over conversation state, making it ideal for multi-turn interactions where intent, memory, and tool execution must be carefully managed.
The agent is designed as a single state-driven node that processes user input and updates a shared AgentState. This state persists across multiple conversation turns and stores information such as detected intent, user name, email, and creator platform. Once a user expresses high intent, the agent locks the intent and switches into a lead-capture mode, preventing accidental intent resets during slot filling.
Knowledge retrieval is implemented using a local JSON-based RAG approach. Pricing and policy information is retrieved deterministically from a local knowledge base instead of relying on the language model’s internal knowledge, ensuring accuracy and preventing hallucination.
Tool execution is strictly controlled. The lead capture function is triggered only when all required user details are present in the state. This architecture mirrors real-world AI sales agents, where reasoning, memory, and backend actions must be coordinated safely and predictably.

3️⃣ WhatsApp Deployment:

To deploy this agent on WhatsApp, the WhatsApp Business Cloud API can be used along with webhooks. Incoming WhatsApp messages would be received via a webhook endpoint hosted on a backend server (for example, using FastAPI or Flask). Each incoming message would be forwarded to the agent along with a unique user or session ID.
The backend would maintain conversation state per user, allowing the agent to preserve memory across multiple WhatsApp messages. The agent’s response would then be sent back to the user using the WhatsApp API’s message-sending endpoint.
When the agent successfully captures a lead, the collected data can be forwarded to a CRM system or backend service for storage and follow-up. This webhook-based integration allows the same agent logic to be reused across channels while maintaining scalability and real-world deployability.
