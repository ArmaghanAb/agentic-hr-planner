import os
from dotenv import load_dotenv
from graph import create_graph

load_dotenv()

graph = create_graph()

# Sample memory (simulate session memory)
memory = {
    "roles": ["Founding Engineer", "GenAI Intern"],
    "budget": "$120K total",
    "timeline": "within 2 months"
}

# Run graph with input
user_input = input(" You: ")
state = {
    "input": user_input,
    "memory": memory  # preload known answers
}

result = graph.invoke(state)

# Print result
print("\nAgent Output:\n")
print(result["output"])
