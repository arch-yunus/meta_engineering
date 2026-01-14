# 🚀 Getting Started with Meta-Engineering (Agnet Swarm)

Welcome to the future of coding. This guide will help you run your first autonomous agent simulation.

## Prerequisites

- Python 3.10+
- An open mind regarding the obsolescence of manual coding.

## Running the "Hello Swarm" Example

We have provided a sample script `examples/hello_swarm.py` that demonstrates the interaction between three core agents:
1.  **Architect**: Plans the task.
2.  **Coder**: Writes the code.
3.  **Reviewer**: Verifies the code.

### Step-by-Step

1.  **Navigate to the project root:**
    ```bash
    cd meta_engineering1
    ```

2.  **Run the simulation:**
    ```bash
    python examples/hello_swarm.py
    ```

### Expected Output

You should see a log of the agents "talking" and working:

```text
🚀 Initializing Meta-Engineering Swarm Simulation...

✅ Agents Online: <Agent Arch-01 (Architect)>, <Agent Coder-Alpha (Coder)>, <Agent Review-Bot (Reviewer)>

🎯 Mission: Create a Python function to add two numbers.

--- 🏗️ Architect Planning ---
Plan: {'phase_1': 'Analyze Requirements', ...}

--- 👨‍💻 Coder Working ---
Generated Code:
def add_numbers(a: int, b: int):
    return a + b

--- 🕵️ Reviewer Analyzing ---
Review Verdict: PASSED: Syntax is correct.

✅ Process Completed Successfully: Code is ready for deployment.
```

## Next Steps

- Explore `core/agents/` to see how the agents are implemented.
- Try modifying `examples/hello_swarm.py` with different goals.
