from typing import Any, Callable, Dict, List
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("OmniBus")

class OmniBus:
    """
    The Nervous System of the Meta-Engineering architecture.
    Handles event-driven communication between agents and components.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OmniBus, cls).__new__(cls)
            cls._instance.subscribers = {}
            cls._instance.history = []
        return cls._instance

    def subscribe(self, channel: str, callback: Callable[[Dict[str, Any]], None]):
        """Register a callback function for a specific channel."""
        if channel not in self.subscribers:
            self.subscribers[channel] = []
        self.subscribers[channel].append(callback)
        logger.info(f"New subscriber added to channel: {channel}")

    def publish(self, channel: str, message: Dict[str, Any]):
        """Broadcast a message to all subscribers of a channel."""
        self.history.append({"channel": channel, "message": message})
        
        if channel in self.subscribers:
            for callback in self.subscribers[channel]:
                try:
                    callback(message)
                except Exception as e:
                    logger.error(f"Error in subscriber callback: {e}")
        else:
            logger.warning(f"No subscribers for channel: {channel}")

    def get_history(self) -> List[Dict[str, Any]]:
        return self.history
