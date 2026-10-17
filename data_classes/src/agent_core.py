# agent_core.py
from dataclasses import dataclass, asdict

@dataclass
class AgentProfile:
    agent_name: str
    model_engine: str
    temperature: float
    # We can assign default values easily
    max_retries: int = 3
    is_active: bool = True