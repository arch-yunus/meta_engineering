from typing import Any, Dict, List, Optional
import time

class ShortTermMemory:
    """Volatile working memory for immediate context."""
    def __init__(self):
        self._store: Dict[str, Any] = {}

    def set(self, key: str, value: Any):
        self._store[key] = {"value": value, "timestamp": time.time()}

    def get(self, key: str) -> Optional[Any]:
        item = self._store.get(key)
        return item["value"] if item else None

    def clear(self):
        self._store.clear()

class LongTermMemory:
    """
    Mock implementation of a Vector Database interface.
    In a full production system, this would connect to Pinecone or Milvus.
    """
    def __init__(self):
        self.vectors = []

    def store_memory(self, text: str, metadata: Dict[str, Any] = None):
        """Simulate storing a semantic vector."""
        # In reality, we would generate an embedding here.
        entry = {
            "id": len(self.vectors) + 1,
            "text": text,
            "metadata": metadata or {},
            "timestamp": time.time()
        }
        self.vectors.append(entry)
        return entry["id"]

    def retrieve_similar(self, query: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Simulate semantic retrieval."""
        # For this prototype, we just do a simple keyword match
        results = [v for v in self.vectors if query.lower() in v["text"].lower()]
        return results[:limit]

class MemoryGrid:
    """Facade for the entire memory system."""
    def __init__(self):
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
