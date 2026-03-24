from typing import Dict, Any
import logging
from .base import BaseAgent, AgentResult
from ..communication import OmniBus

logger = logging.getLogger("Coder")

class CoderAgent(BaseAgent):
    """
    Agent responsible for generating code based on specifications.
    Specialized in Python.
    """
    def __init__(self, name: str = "Coder-01"):
        super().__init__(name, role="Coder")
        from ..fabrication import get_sandbox
        self.sandbox = get_sandbox()

    async def initialize(self):
        bus = OmniBus()
        bus.subscribe("coding_tasks", self.handle_task)
        logger.info(f"{self.name} subscribed to 'coding_tasks' channel.")

    async def handle_task(self, message: Dict[str, Any]):
        task = message.get("task")
        result = await self.think({"task": task})
        if result.status == "success":
            act_res = await self.act(result.payload)
            await OmniBus().publish("code_review", {
                "sender": self.name,
                "content": act_res.payload,
                "file_path": act_res.metadata.get("file_path")
            })

    async def think(self, context: Dict[str, Any]) -> AgentResult:
        """
        Uses the LLM Engine to generate code based on the task asynchronously.
        """
        task = context.get("task", "")
        
        prompt = f"Write a Python function for the following task: {task}. Return ONLY the code."
        code = await self.generate_thought(prompt)
        
        return AgentResult(
            payload=code,
            status="success",
            metadata={"language": "python", "task_name": task.lower().replace(" ", "_")}
        )

    async def act(self, action_plan: Any) -> AgentResult:
        """
        Execute the writing of code to the sandbox asynchronously.
        """
        code = action_plan
        # For this prototype, we just name it based on timestamp or a simple counter
        filename = f"generated_module.py"
        file_path = self.sandbox.write_artifact(filename, code)
        
        return AgentResult(
            payload=f"File successfully created at: {file_path}", 
            status="success",
            metadata={"file_path": file_path}
        )

    def _generate_add_function(self) -> str:
        return """
def add_numbers(a: int, b: int) -> int:
    '''Calculates the sum of two integers.'''
    return a + b
"""
