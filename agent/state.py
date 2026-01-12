from typing import TypedDict, Optional


class AgentState(TypedDict):
    intent: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    last_user_message: Optional[str]
