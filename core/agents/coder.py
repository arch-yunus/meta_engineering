from typing import Dict, Any
from .base import BaseAgent, AgentResult

class CoderAgent(BaseAgent):
    """
    Agent responsible for generating code based on specifications.
    Specialized in Python.
    """
    def __init__(self, name: str = "Coder-01"):
        super().__init__(name, role="Coder")

    def think(self, context: Dict[str, Any]) -> AgentResult:
        """
        Simulates the thinking process of writing code.
        In a real scenario, this would call an LLM.
        """
        task = context.get("task", "")
        
        # Simple mock logic for demonstration
        if "add two numbers" in task.lower():
            code = self._generate_add_function()
            return AgentResult(
                payload=code,
                status="success",
                metadata={"language": "python"}
            )
        
        return AgentResult(
            payload=None,
            status="pending",
            error="Task not understood or too complex for mock logic."
        )

    def act(self, action_plan: Any) -> AgentResult:
        """
        Execute the writing of code to a specific location (mock).
        """
        # In this simplified version, 'act' returns the code directly.
        return AgentResult(payload=action_plan, status="success")

    def _generate_add_function(self) -> str:
        return """
def add_numbers(a: int, b: int) -> int:
    '''Calculates the sum of two integers.'''
    return a + b
"""
