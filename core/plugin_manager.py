import importlib
import os
import sys
import logging
from typing import Dict, Any

logger = logging.getLogger("PluginManager")

class PluginManager:
    """
    Manages the lifecycle of external plugins.
    Plugins are python modules located in the 'plugins' directory.
    """
    def __init__(self, plugin_dir: str = "plugins"):
        self.plugin_dir = plugin_dir
        self.plugins: Dict[str, Any] = {}

    def discover_plugins(self):
        """Scans the plugin directory for python files."""
        if not os.path.exists(self.plugin_dir):
            logger.warning(f"Plugin directory not found: {self.plugin_dir}")
            return

        sys.path.append(os.getcwd())  # Ensure current dir is in path

        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                self.load_plugin(module_name)

    def load_plugin(self, module_name: str):
        try:
            # Import dynamically: plugins.module_name
            module_path = f"{self.plugin_dir}.{module_name}"
            module = importlib.import_module(module_path)
            
            if hasattr(module, "register"):
                module.register()
                self.plugins[module_name] = module
                logger.info(f"Plugin loaded: {module_name}")
            else:
                logger.warning(f"Plugin {module_name} missing 'register()' function.")
        except Exception as e:
            logger.error(f"Failed to load plugin {module_name}: {e}")

    def get_plugin(self, name: str):
        return self.plugins.get(name)
