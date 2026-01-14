# ⚛️ Core System Documentation

Welcome to the heart of the Meta-Engineering beast. This directory (`core/`) contains the fundamental logic, base classes, and neural architecture that powers the entire ecosystem.

> **Warning:** Changes here affect every single agent and subsystem. Tread lightly.

## 📂 Directory Structure

### `agents/` (The Population)
Contains the concrete implementations of the biological swarm members.
- `base.py`: **THE HOLY GRAIL.** The abstract base class (`BaseAgent`). Defines the interface `think()` and `act()`. All agents MUST inherit from this.
- `coder.py`: Implementation of the coding specialist.
- `reviewer.py`: Implementation of the critic.
- `architect.py`: Implementation of the planner.

### `memory/` (The Hippocampus)
Manages the state and history of the system.
- `grid.py`: The main interface ensuring thread-safe access to memory.
- `short_term.py`: Redis/In-memory wrapper for volatile context.
- `long_term.py`: Vector DB (Pinecone/Milvus) wrapper for episodic recall.

### `communication/` (The Synapses)
Handles the `Omni-Bus` messaging protocol.
- `bus.py`: The event loop and message broker. Implementation of the Pub/Sub pattern.
- `protocol.py`: Definitions of the JSON schemas and message types.

## 🛠️ How to Extend (Developer Guide)

### Adding a New Agent
To create a new type of agent (e.g., `SecurityAgent`), follow these steps:

1.  **Inherit:** Create `core/agents/security.py` and inherit from `BaseAgent`.
2.  **Implement:** You must implement the abstract methods `think(context)` and `act(plan)`.
3.  **Register:** Add your new agent to `core/agents/__init__.py`.
4.  **Prompt:** Define the unique system prompt/persona for your agent.

```python
from core.agents.base import BaseAgent, AgentResult

class SecurityAgent(BaseAgent):
    def think(self, context):
        # ... your LLM logic here ...
        return AgentResult(...)
```

### Modifying the Event Bus
If you need to add a new event type:
1.  Go to `core/communication/protocol.py`.
2.  Add your new Enum to `EventType`.
3.  Update the validation schema.

## 🧪 Testing
Run the core test suite before pushing changes:
```bash
pytest tests/core/
```
