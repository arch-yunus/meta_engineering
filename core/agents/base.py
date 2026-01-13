from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

@dataclass
class AgentResult:
    """Standardized result format for agent operations."""
    payload: Any
    status: str  # 'success', 'failure', 'pending'
    metadata: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

class BaseAgent(ABC):
    """
    Abstract base class for all Meta-Engineering agents.
    Acts as a blueprint for biological swarm intelligence simulation.
    """
    
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.memory = []  # Short-term local memory
        
    @abstractmethod
    def think(self, context: Dict[str, Any]) -> AgentResult:
        """
        Process the input context and determine the next action.
        Represents the cognitive processing step.
        """
        pass

    @abstractmethod
    def act(self, action_plan: Any) -> AgentResult:
        """
        Execute the determined action.
        Represents the motor cortex function.
        """
        pass

    def communicate(self, message: str, channel: str = "general") -> Dict[str, Any]:
        """
        Format a message to be sent to the Omni-Bus.
        """
        return {
            "sender": self.name,
            "role": self.role,
            "channel": channel,
            "content": message
        }

    def __repr__(self):
        return f"<Agent {self.name} ({self.role})>"
