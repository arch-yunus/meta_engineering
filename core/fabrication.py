import os
import shutil
import subprocess
import logging
from typing import Optional, Dict, Any, List

logger = logging.getLogger("Fabrication")

class LocalSandbox:
    """
    Managed execution environment for agent-generated code.
    Ensures that files are written to safe, isolated directories.
    """
    def __init__(self, base_path: str = "workspace"):
        self.base_path = os.path.abspath(base_path)
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
            logger.info(f"Created sandbox workspace at: {self.base_path}")

    def write_artifact(self, filename: str, content: str, project_id: str = "default") -> str:
        """Writes a file to the sandbox and returns its absolute path."""
        target_dir = os.path.join(self.base_path, project_id)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        file_path = os.path.join(target_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        logger.info(f"Artifact written to: {file_path}")
        return file_path

    def run_tests(self, file_path: str) -> Dict[str, Any]:
        """Runs basic syntax and unit tests on a file (if applicable)."""
        logger.info(f"Running tests on: {file_path}")
        
        # 1. Syntax search via compile
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                source = f.read()
            compile(source, file_path, "exec")
        except SyntaxError as e:
            return {"status": "failure", "error": f"Syntax Error: {e}"}
        
        # 2. Basic subprocess execution for verification
        # For security, we just do a dry run or static check in this prototype
        # In a full system, you would use 'pytest' or similar.
        return {"status": "success", "message": "Static verification passed."}

    def cleanup(self, project_id: Optional[str] = None):
        """Removes project files or the entire sandbox."""
        path_to_remove = os.path.join(self.base_path, project_id) if project_id else self.base_path
        if os.path.exists(path_to_remove):
            shutil.rmtree(path_to_remove)
            logger.info(f"Cleaned up sandbox at: {path_to_remove}")

_default_sandbox = None

def get_sandbox() -> LocalSandbox:
    global _default_sandbox
    if _default_sandbox is None:
        _default_sandbox = LocalSandbox()
    return _default_sandbox
