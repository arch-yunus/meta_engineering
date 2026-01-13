from typing import Any, Dict
from .base import BaseAgent, AgentResult

class ArchitectAgent(BaseAgent):
    """
    The Visionary. Breaks down high-level intents into technical tasks.
    """
    def __init__(self, name: str = "Architect"):
        super().__init__(name, role="Architect")

    def think(self, context: Dict[str, Any]) -> AgentResult:
        intent = context.get("intent")
        self.memory.append(f"Analyzing intent: {intent}")
        
        # Simulate breaking down the task
        tasks = [
            "Analyze requirements",
            "Design schema",
            "Draft core classes"
        ]
        
        return AgentResult(
            payload=tasks,
            status="success",
            metadata={"step": "planning"}
        )

    def act(self, action_plan: Any) -> AgentResult:
        tasks = action_plan
        message = f"Plan created with {len(tasks)} steps."
        return AgentResult(payload=message, status="success")

class CoderAgent(BaseAgent):
    """
    The Builder. Turns tasks into code (simulated).
    """
    def __init__(self, name: str = "Coder"):
        super().__init__(name, role="Coder")

    def think(self, context: Dict[str, Any]) -> AgentResult:
        task = context.get("task")
        self.memory.append(f"Coding task: {task}")
        return AgentResult(
            payload=f"def implement_{task.lower().replace(' ', '_')}(): pass",
            status="success"
        )

    def act(self, action_plan: Any) -> AgentResult:
        code = action_plan
        return AgentResult(payload=f"Generated code: {code}", status="success")

class ReviewerAgent(BaseAgent):
    """
    The Critic. Reviews code for safety and style.
    """
    def __init__(self, name: str = "Reviewer"):
        super().__init__(name, role="Reviewer")

    def think(self, context: Dict[str, Any]) -> AgentResult:
        code = context.get("code")
        self.memory.append("Reviewing code snippet")
        
        if "eval(" in code:
            return AgentResult(payload="Security Alert: eval() used", status="failure")
        
        return AgentResult(payload="Code looks good", status="success")

    def act(self, action_plan: Any) -> AgentResult:
        verdict = action_plan
        return AgentResult(payload=f"Review complete: {verdict}", status="success")
