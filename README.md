# Agentic HR Planner

Author: *Armaghan Abtahi*

---

## Overview

**Agentic HR Planner** is an Agentic AI application designed to assist HR professionals in planning startup hiring processes.  It transforms a simple user prompt into a structured multi-step interaction that produces job descriptions, hiring plans, and actionable checklists, all powered by LangGraph and LLM reasoning.

> Example prompt:_  
> “I need to hire a founding engineer and a GenAI intern. Can you help?”

The agent responds dynamically by asking clarifying questions, gathering requirements, drafting job descriptions, creating a hiring plan, and presenting the results in a structured markdown format.

---
## Walkthrough Demo

[App Walkthrough](assets/Walkthrough.gif)

---

## Video Presentation

Watch this video explaining the architecture and design decisions:

[Loom Video Link](https://www.loom.com/share/a67e77121235481f9545910558f09e5f?sid=aefeb9bb-4190-46e2-9280-cd96a54ece44)

---
## Tech Stack

| Component         | Technology |
|-------------------|------------|
| LLM Reasoning     | OpenAI GPT-4o |
| Orchestration     | LangGraph |
| Frontend          | Streamlit |
| Memory            | JSON-based session memory |
| Language          | Python |
| Optional Tools    | (Simulated) Email writer, Checklist builder, Salary Estimate|

---
## Architecture

User Input ➡ Agentic Graph ➡ Clarifying Questions ➡ Job Description Draft ➡ Hiring Checklist ➡ Final Plan

---

## Key Components

- **graph.py** — Defines the LangGraph multi-step reasoning flow.
- **nodes.py** — Modular nodes for different agent tasks (clarifying, drafting, checklist creation).
- **app.py** — Streamlit app to provide an interactive frontend.
- **schema.py** — Data models and validation.
- **session_memory.json** — Retains state between user sessions (session-based memory).

*The agent design is modular, enabling easy extension with new tools or steps.*

---

## Design Decisions

- **LangGraph over LangChain Agents**  
  Chosen for better control over multi-step reasoning and handling stateful workflows where user input at each stage affects the next step.

- **Streamlit Frontend**  
  Provided a simple but effective UI where HR professionals can interact with the app without technical barriers. Streamlit was selected for rapid prototyping and visualization.

- **Memory Implementation**  
  Used JSON file-based session memory for fast iteration and debugging. This allows memory to persist between app restarts without complex database setup.

- **Tool Simulation**  
  Simulated essential tools like a salary estimator and email writer to show the app’s potential extensibility. This keeps the system lightweight while demonstrating agentic flexibility.

- **Code Modularity**  
  Broke down the app into clearly defined files — `graph.py`, `nodes.py`, `schema.py`, and `app.py` — to ensure maintainability and scalability.

- **Reset Functionality**  
  Added a reset button to clear session memory easily, giving users a smooth way to restart the hiring process without refreshing or manual resets.


---

## What I'd Improve with More Time

If given additional time and resources, I would:

- **Enhance Memory**  
  Replace JSON memory with a more scalable database (e.g., SQLite or Redis) or LangChain’s memory system.

- **Implement Analytics**  
  Track user interactions, most requested roles, and common salary ranges to provide useful insights.

- **Improve UI/UX**  
  Develop a more advanced frontend ( React ) for a modern user experience beyond Streamlit.

- **Deploy Online**  
  Host the app using Streamlit Community Cloud or a cloud service like AWS or GCP for easy access.


---

## How to Run

```bash
# (1) Create virtual environment and activate it
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# (2) Install requirements
pip install -r requirements.txt

# (3) Run the Streamlit app
streamlit run app.py
