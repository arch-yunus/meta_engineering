from typing import Dict, Any
from .base import BaseAgent, AgentResult

class ArchitectAgent(BaseAgent):
    """
    Agent responsible for high-level system design and planning.
    """
    def __init__(self, name: str = "Architect-01"):
        super().__init__(name, role="Architect")

    def think(self, context: Dict[str, Any]) -> AgentResult:
        goal = context.get("goal", context.get("intent", ""))
        
        prompt = f"As an AI Architect, create a structured technical plan for the following goal: {goal}. Return the plan as a JSON-like structure."
        plan_str = self.generate_thought(prompt)
        
        return AgentResult(
            payload=plan_str,
            status="success",
            metadata={"type": "high_level_plan"}
        )

    def act(self, action_plan: Any) -> AgentResult:
        return AgentResult(payload=action_plan, status="success")
