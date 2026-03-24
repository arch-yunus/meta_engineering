import json
from typing import Dict, Any
import logging
from .base import BaseAgent, AgentResult
from ..communication import OmniBus

logger = logging.getLogger("Architect")

class ArchitectAgent(BaseAgent):
    """
    Agent responsible for high-level system design and planning.
    """
    def __init__(self, name: str = "Architect-01"):
        super().__init__(name, role="Architect")

    async def initialize(self):
        bus = OmniBus()
        bus.subscribe("intent", self.handle_intent)
        logger.info(f"{self.name} subscribed to 'intent' channel.")

    async def handle_intent(self, message: Dict[str, Any]):
        intent = message.get("content")
        result = await self.think({"intent": intent})
        if result.status == "success":
            await self.act(result.payload)
            
            # Autonomous Task Breakout
            try:
                plan = json.loads(result.payload)
                phases = plan.get("phases", [])
                for phase in phases:
                    task_desc = phase.get("task")
                    logger.info(f"{self.name} dispatching task: {task_desc}")
                    await OmniBus().publish("coding_tasks", {
                        "sender": self.name,
                        "task": task_desc,
                        "metadata": phase
                    })
            except (json.JSONDecodeError, TypeError):
                # Fallback if LLM didn't return perfect JSON
                logger.warning(f"{self.name} failed to parse plan JSON. Dispatching raw plan.")
                await OmniBus().publish("coding_tasks", {
                    "sender": self.name,
                    "task": result.payload
                })

    async def think(self, context: Dict[str, Any]) -> AgentResult:
        goal = context.get("goal", context.get("intent", ""))
        
        prompt = f"As an AI Architect, create a structured technical plan for the following goal: {goal}. Return the plan as a JSON-like structure."
        plan_str = await self.generate_thought(prompt)
        
        return AgentResult(
            payload=plan_str,
            status="success",
            metadata={"type": "high_level_plan"}
        )

    async def act(self, action_plan: Any) -> AgentResult:
        return AgentResult(payload=action_plan, status="success")
