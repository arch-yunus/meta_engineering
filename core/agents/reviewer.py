from typing import Dict, Any
import ast
import logging
from .base import BaseAgent, AgentResult
from ..communication import OmniBus

logger = logging.getLogger("Reviewer")

class ReviewerAgent(BaseAgent):
    """
    Agent responsible for analyzing and critiquing code.
    """
    def __init__(self, name: str = "Reviewer-01"):
        super().__init__(name, role="Reviewer")
        from ..fabrication import get_sandbox
        self.sandbox = get_sandbox()

    async def initialize(self):
        bus = OmniBus()
        bus.subscribe("code_review", self.handle_review)
        logger.info(f"{self.name} subscribed to 'code_review' channel.")

    async def handle_review(self, message: Dict[str, Any]):
        content = message.get("content") or message.get("code")
        file_path = message.get("file_path")
        
        result = await self.think({"code": content, "file_path": file_path})
        if result.status == "success":
            await self.act(result.payload)
            await OmniBus().publish("reviews", {
                "sender": self.name,
                "content": result.payload
            })

    async def think(self, context: Dict[str, Any]) -> AgentResult:
        file_path = context.get("file_path")
        code_to_review = context.get("code", "")
        
        if file_path:
            # Perform physical verification in sandbox
            res = self.sandbox.run_tests(file_path)
            if res["status"] == "success":
                review_result = f"FABRICATION SUCCESS: {res['message']}"
            else:
                review_result = f"FABRICATION FAILURE: {res['error']}"
        elif code_to_review:
            prompt = f"Review the following Python code for security, performance, and best practices: \n\n{code_to_review}\n\nProvide a concise bulleted review."
            review_result = await self.generate_thought(prompt)
        else:
             return AgentResult(payload=None, status="failure", error="No code or file to review")

        return AgentResult(
            payload=review_result,
            status="success"
        )

    async def act(self, action_plan: Any) -> AgentResult:
        return AgentResult(payload=action_plan, status="success")

    def _static_analysis(self, code: str) -> str:
        try:
            ast.parse(code)
            return "PASSED: Syntax is correct."
        except SyntaxError as e:
            return f"FAILED: Syntax error detected: {e}"
