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

import os
import uuid
import chromadb

class LongTermMemory:
    """
    Real implementation of a Vector Database interface using ChromaDB.
    """
    def __init__(self, db_path: str = "workspace/chroma_db"):
        os.makedirs(db_path, exist_ok=True)
        self.client = chromadb.PersistentClient(path=os.path.abspath(db_path))
        self.collection = self.client.get_or_create_collection(name="episodic_memory")

    def store_memory(self, text: str, metadata: Optional[Dict[str, Any]] = None):
        """Store a semantic vector."""
        # ChromaDB automatically generates embeddings using the default embedding function
        doc_id = str(uuid.uuid4())
        
        meta = metadata or {}
        # ChromaDB metadata values must be str, int, float or bool
        cleaned_meta = {k: v for k, v in meta.items() if isinstance(v, (str, int, float, bool))}
        cleaned_meta["timestamp"] = time.time()
        
        self.collection.add(
            documents=[text],
            metadatas=[cleaned_meta],
            ids=[doc_id]
        )
        return doc_id

    def retrieve_similar(self, query: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Semantic retrieval using vector embeddings."""
        # If collection is empty, chroma might error on query, so we handle safely
        if self.collection.count() == 0:
            return []
            
        results = self.collection.query(
            query_texts=[query],
            n_results=min(limit, self.collection.count())
        )
        
        parsed_results = []
        if results['documents'] and len(results['documents']) > 0:
            for i in range(len(results['documents'][0])):
                parsed_results.append({
                    "id": results['ids'][0][i],
                    "text": results['documents'][0][i],
                    "metadata": results['metadatas'][0][i] if results['metadatas'] else {}
                })
        return parsed_results

class MemoryGrid:
    """Facade for the entire memory system."""
    def __init__(self):
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
