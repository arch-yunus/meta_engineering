import argparse
import asyncio
import logging
from core.orchestrator import SwarmOrchestrator
from core.plugin_manager import PluginManager

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [MAIN] - %(levelname)s - %(message)s')
logger = logging.getLogger("MetaEngine")

def main():
    parser = argparse.ArgumentParser(description="Meta-Engineering: Autonomous System")
    parser.add_argument("--start-autonomous-mode", action="store_true", help="Start the autonomous agent swarm")
    parser.add_argument("--load-plugins", action="store_true", help="Load external plugins")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--intent", type=str, default="Build a secure login system", help="Initial goal for the swarm")
    
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    print("\nMeta-Engineering System v1.1.5 (Async)")
    print("========================================")

    if args.start_autonomous_mode:
        try:
            asyncio.run(run_async_swarm(args.intent))
        except KeyboardInterrupt:
            logger.info("System interrupted by user.")
    else:
        print("System ready. Use --start-autonomous-mode to ignite the swarm.")

async def run_async_swarm(intent: str):
    logger.info("Starting Asynchronous Orchestrator...")
    
    # 1. Load Plugins
    pm = PluginManager()
    pm.discover_plugins()
    
    # 2. Start Orchestrator
    orchestrator = SwarmOrchestrator()
    await orchestrator.start(intent)

if __name__ == "__main__":
    main()
