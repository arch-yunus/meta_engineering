import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.agents.coder import CoderAgent
from core.agents.reviewer import ReviewerAgent
from core.agents.architect import ArchitectAgent

def main():
    print("🚀 Initializing Meta-Engineering Swarm Simulation...\n")

    # 1. Initialize Agents
    architect = ArchitectAgent(name="Arch-01")
    coder = CoderAgent(name="Coder-Alpha")
    reviewer = ReviewerAgent(name="Review-Bot")

    print(f"✅ Agents Online: {architect}, {coder}, {reviewer}\n")

    # 2. Define a Scenario
    goal = "Create a Python function to add two numbers."
    print(f"🎯 Mission: {goal}\n")

    # 3. Architect Plans
    print("--- 🏗️ Architect Planning ---")
    plan_result = architect.think({"goal": goal})
    print(f"Plan: {plan_result.payload}\n")

    # 4. Coder Writes Code
    print("--- 👨‍💻 Coder Working ---")
    # In a real system, the Architect's output would be passed here.
    # For this simplified example, we pass the task directly.
    code_result = coder.think({"task": goal})
    generated_code = code_result.payload
    print(f"Generated Code:\n{generated_code}\n")

    # 5. Reviewer Checks Code
    print("--- 🕵️ Reviewer Analyzing ---")
    review_result = reviewer.think({"code": generated_code})
    print(f"Review Verdict: {review_result.payload}\n")

    if "PASSED" in review_result.payload:
        print("✅ Process Completed Successfully: Code is ready for deployment.")
    else:
        print("❌ Process Failed: Code needs revision.")

if __name__ == "__main__":
    main()
