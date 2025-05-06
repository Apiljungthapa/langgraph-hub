from typing import Optional

class AgentManager:
    def __init__(self):
        self._agent_id = None
  

    def set_agent_id(self, agent_id: str):
        """Sets the agentId value."""
        self._agent_id = agent_id

    def get_agent_id(self) -> Optional[str]:
        """Gets the agentId value."""
        return self._agent_id


# Create a single instance of the class to manage agentId
agent_manager = AgentManager()