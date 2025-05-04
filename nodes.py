from schema import HRHiringState
from dotenv import load_dotenv

load_dotenv()

from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

# Step 1: Clarify required inputs
def clarify_input(state: HRHiringState) -> HRHiringState:
    memory = state.memory or {}

    questions = []
    if "roles" not in memory:
        questions.append("What specific roles are you hiring for?")
    if "budget" not in memory:
        questions.append("Do you have a budget in mind for these roles?")
    if "timeline" not in memory:
        questions.append("What is your expected timeline for hiring?")

    if questions:
        state.output = "Before I can help, I need to ask:\n" + "\n".join(f"- {q}" for q in questions)
    else:
        state.proceed = True

    return state

# Step 2: Generate Job Descriptions with GPT
def generate_job_descriptions(state: HRHiringState) -> HRHiringState:
    roles = state.memory.get("roles", ["Engineer"])
    jd_output = {}

    for role in roles:
        prompt = f"""Write a concise startup-style job description for the role of {role}.
Include sections: Responsibilities and Requirements."""
        jd = llm.predict(prompt)
        jd_output[role] = f"### {role} - Job Description\n{jd}"

    state.job_descriptions = jd_output
    return state

# Step 3: Build hiring checklist using GPT
def generate_checklist(state: HRHiringState) -> HRHiringState:
    prompt = "List the key steps an HR professional should take when hiring for a startup, in concise bullet points."
    checklist_text = llm.predict(prompt)
    checklist = [f"- {line.strip()}" for line in checklist_text.split("\n") if line.strip()]
    state.checklist = checklist
    return state

# Step 4: Salary Search
def estimate_salary_ranges(state):
    prompt = f"""
    For the following roles, provide an estimated US salary range per year in USD.
    Roles: {', '.join(state.memory.get('roles', []))}.
    Format like: Role: $X - $Y
    """

    response = llm.invoke(prompt)
    state.memory["salary_estimates"] = response.content
    return state

# Step 5: Simulated Google Search Tool
def simulate_search(query: str) -> str:
    prompt = f"Simulate a Google search summary for this query: {query}"
    return llm.predict(prompt)

# Step 6: Email Writer Tool
def generate_email(role: str) -> str:
    prompt = f"Write a short, friendly recruiting outreach email for a {role} at an early-stage startup."
    return llm.predict(prompt)

# Step 7: Final Output Formatter
def format_output(state: HRHiringState) -> HRHiringState:
    jd = state.job_descriptions or {}
    checklist = state.checklist or []

    # Simulate search + email generation
    search_summary = simulate_search("best hiring practices for startups")
    email_samples = {
        role: generate_email(role) for role in state.memory.get("roles", [])
    }

    output = "### Hiring Plan\n"

    for role, desc in jd.items():
        output += f"\n{desc}\n"

    output += "\n### General Checklist:\n"
    for step in checklist:
        output += f"{step}\n"
    
    # Salary Estimates Section
    salary_estimates = state.memory.get("salary_estimates", "")
    output += "\n\n### Salary Estimates:\n"
    if salary_estimates:
        lines = salary_estimates.split("\n")
        for line in lines:
            if not line.strip():
                continue
            if ":" in line:
                role, range_text = line.split(":", 1)
                numbers = range_text.replace("$", "").replace(",", "").split("—")
                if len(numbers) == 2:
                    min_salary = f"**${int(numbers[0].strip()):,}**"
                    max_salary = f"**${int(numbers[1].strip()):,}**"
                    output += f"- **{role.strip()}**: {min_salary} — {max_salary}\n"
                else:
                    # If there's no range, just bold the number
                    output += f"- **{role.strip()}**: **${range_text.strip()}**\n"
            else:
                output += f"- **{line.strip()}**\n"


    output += "\n### Simulated Google Search:\n"
    output += f"{search_summary}\n"

    output += "\n### Sample Outreach Emails:\n"
    for role, email in email_samples.items():
        output += f"\n#### {role}:\n{email}\n"

    state.output = output
    return state
