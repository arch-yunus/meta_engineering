from typing import Dict, Any
from .base import BaseAgent, AgentResult

class CoderAgent(BaseAgent):
    """
    Agent responsible for generating code based on specifications.
    Specialized in Python.
    """
    def __init__(self, name: str = "Coder-01"):
        super().__init__(name, role="Coder")
        from ..fabrication import get_sandbox
        self.sandbox = get_sandbox()

    def think(self, context: Dict[str, Any]) -> AgentResult:
        """
        Uses the LLM Engine to generate code based on the task.
        """
        task = context.get("task", "")
        
        prompt = f"Write a Python function for the following task: {task}. Return ONLY the code."
        code = self.generate_thought(prompt)
        
        return AgentResult(
            payload=code,
            status="success",
            metadata={"language": "python", "task_name": task.lower().replace(" ", "_")}
        )

    def act(self, action_plan: Any) -> AgentResult:
        """
        Execute the writing of code to the sandbox.
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
