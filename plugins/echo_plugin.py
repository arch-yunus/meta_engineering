import logging
from core.communication import OmniBus

logger = logging.getLogger("EchoPlugin")

def register():
    """Entry point for the plugin manager."""
    bus = OmniBus()
    bus.subscribe("general", echo_handler)
    logger.info("EchoPlugin registered to 'general' channel.")

def echo_handler(message):
    logger.info(f"EchoPlugin received: {message}")
