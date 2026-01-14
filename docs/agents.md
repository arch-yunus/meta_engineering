# 🧠 Meta-Engineering Agent Reference

This document details the specific agents designed for the Meta-Engineering swarm ecosystem.

## 🏗️ ArchitectAgent

- **Role:** System Design & High-Level Planning
- **Responsibility:**
    - Analyzes vague user goals (e.g., "Build a blog").
    - Breaks down goals into executable phases.
    - Determines necessary resources and constraints.
- **Input:** High-level intent (natural language).
- **Output:** Structured Implementation Plan (JSON).

## 👨‍💻 CoderAgent

- **Role:** Implementation Specialist
- **Responsibility:**
    - Takes specific technical tasks (e.g., "Write a Python function to sort a list").
    - Generates syntactically correct code.
    - Adheres to project style guides (PEP8, etc.).
- **Specialization:** Currently optimized for Python (v0.1).
- **Mock Behavior:** In the current prototype, detects keywords like "add" to generate sample code.

## 🕵️ ReviewerAgent

- **Role:** Quality Assurance & Security
- **Responsibility:**
    - Performs static analysis on generated code.
    - Checks for syntax errors, security vulnerabilities, and logic flaws.
    - Rejects code that doesn't meet quality standards.
- **Tools:** Uses Python `ast` module for syntax verification in v0.1.
