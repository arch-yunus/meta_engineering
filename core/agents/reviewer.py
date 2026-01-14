from typing import Dict, Any
import ast
from .base import BaseAgent, AgentResult

class ReviewerAgent(BaseAgent):
    """
    Agent responsible for analyzing and critiquing code.
    """
    def __init__(self, name: str = "Reviewer-01"):
        super().__init__(name, role="Reviewer")

    def think(self, context: Dict[str, Any]) -> AgentResult:
        code_to_review = context.get("code", "")
        if not code_to_review:
             return AgentResult(payload=None, status="failure", error="No code to review")

        review_result = self._static_analysis(code_to_review)
        return AgentResult(
            payload=review_result,
            status="success"
        )

    def act(self, action_plan: Any) -> AgentResult:
        return AgentResult(payload=action_plan, status="success")

    def _static_analysis(self, code: str) -> str:
        try:
            ast.parse(code)
            return "PASSED: Syntax is correct."
        except SyntaxError as e:
            return f"FAILED: Syntax error detected: {e}"
