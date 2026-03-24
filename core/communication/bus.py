import asyncio
import logging
import time
from typing import Any, Callable, Dict, List, Coroutine, Optional

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("OmniBus")

class OmniBus:
    """
    The Nervous System of the Meta-Engineering architecture.
    Handles asynchronous event-driven communication between agents.
    """
    
    _instance: Optional['OmniBus'] = None
    subscribers: Dict[str, List[Callable[[Dict[str, Any]], Coroutine[Any, Any, None]]]]
    history: List[Dict[str, Any]]
    lock: asyncio.Lock

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OmniBus, cls).__new__(cls)
            cls._instance.subscribers = {}
            cls._instance.history = []
            cls._instance.lock = asyncio.Lock()
        return cls._instance

    def subscribe(self, channel: str, callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]]):
        """Register an async callback function for a specific channel."""
        if channel not in self.subscribers:
            self.subscribers[channel] = []
        self.subscribers[channel].append(callback)
        logger.info(f"New async subscriber added to channel: {channel}")

    async def publish(self, channel: str, message: Dict[str, Any]):
        """Broadcast a message to all subscribers of a channel asynchronously."""
        async with self.lock:
            self.history.append({"channel": channel, "message": message, "timestamp": time.time()})
        
        if channel in self.subscribers:
            logger.debug(f"Publishing to {channel}: {message.get('sender')}")
            # Run all subscribers concurrently
            tasks = [callback(message) for callback in self.subscribers[channel]]
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)
        else:
            logger.warning(f"No subscribers for channel: {channel}")

    def get_history(self) -> List[Dict[str, Any]]:
        return self.history
