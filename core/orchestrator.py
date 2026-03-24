import asyncio
import logging
from typing import List
from .communication import OmniBus
from .agents.base import BaseAgent
from .agents import ArchitectAgent, CoderAgent, ReviewerAgent

logger = logging.getLogger("SwarmOrchestrator")

class SwarmOrchestrator:
    """
    The Prefrontal Cortex of the Meta-Engineering system.
    Orchestrates the lifecycle and event loop of the agent swarm.
    """
    def __init__(self):
        self.bus = OmniBus()
        self.agents: List[BaseAgent] = [
            ArchitectAgent("DaVinci"),
            CoderAgent("Lovelace"),
            ReviewerAgent("Torvalds")
        ]
        self.is_running = False

    async def initialize_swarm(self):
        """Wake up all agents and let them subscribe to channels."""
        logger.info("Igniting the swarm...")
        for agent in self.agents:
            await agent.initialize()
        logger.info("All agents are now online and listening.")

    async def start(self, initial_intent: str):
        """Start the main event loop and inject the initial intent."""
        self.is_running = True
        await self.initialize_swarm()
        
        logger.info(f"Injecting Global Intent: {initial_intent}")
        await self.bus.publish("intent", {"content": initial_intent, "sender": "Orchestrator"})
        
        # Keep the loop alive
        while self.is_running:
            await asyncio.sleep(1)
            # Add logic here for system monitoring or shutdown conditions
            if len(self.bus.get_history()) > 100: # Simple threshold for prototype
                 logger.info("History threshold reached. Cooling down...")
                 break

    def stop(self):
        self.is_running = False
        logger.info("Swarm shutdown sequence initiated.")
