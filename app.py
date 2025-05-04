import streamlit as st
from graph import create_graph
from schema import HRHiringState
import json

st.set_page_config(page_title="Agentic HR Planner", layout="wide")
st.title("Agentic HR Planner")
st.write("I can help you plan your startup hiring process!")

graph = create_graph()

# Load or initialize memory
if "memory" not in st.session_state:
    try:
        with open("session_memory.json") as f:
            st.session_state.memory = json.load(f)
    except FileNotFoundError:
        st.session_state.memory = {}


# Question
question = st.text_input(
    "How Can I Help You?", 
    value=st.session_state.get("question", ""), 
    key="question"
)
if question:
    st.session_state.memory["question"]=question

if "question" in st.session_state.memory:
    st.markdown("Sure! But before we proceed, could you please answer the following clarifying questions?")    
    
# Input field for clarification questions
st.markdown("### Clarifying Questions")

# Roles
roles = st.text_input(
    "What roles are you hiring for? (comma-separated)", 
    value=", ".join(st.session_state.memory.get("roles", [])), 
    key="roles"
)
if roles:
    st.session_state.memory["roles"] = [r.strip() for r in roles.split(",")]

# Budget
budget = st.text_input(
    "Do you have a budget in mind?", 
    value=st.session_state.get("budget", ""), 
    key="budget"
)

if budget:
    st.session_state.memory["budget"] = budget

# Timeline
timeline = st.text_input(
    "What is your expected hiring timeline?", 
    value=st.session_state.get("timeline", ""), 
    key="timeline"
)

if timeline:
    st.session_state.memory["timeline"] = timeline

# Once all questions are answered
if all(k in st.session_state.memory for k in ["roles", "budget", "timeline"]):
    st.success("All clarifying info provided!")
    user_input = st.text_area("Optional message to the agent:", placeholder="Help me create a hiring plan...")

    if st.button("Generate Hiring Plan"):
        with st.spinner("Thinking..."):
            state = HRHiringState(input=user_input, memory=st.session_state.memory)
            result = graph.invoke(state)

            # Save memory for session continuity
            with open("session_memory.json", "w") as f:
                json.dump(st.session_state.memory, f, indent=2)

            st.markdown("### Structured Hiring Plan")
            st.markdown(result["output"])
    
    if st.button("Reset Memory"):
        st.session_state.memory = {}
        for key in ["question", "roles", "budget", "timeline"]:
           if key in st.session_state:
             del st.session_state[key]
        with open("session_memory.json", "w") as f:
            json.dump({}, f)
        st.session_state.clear() 
        st.rerun()

            
else:
    st.warning("Please answer all clarification questions to proceed.")
