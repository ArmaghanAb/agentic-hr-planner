from langgraph.graph import StateGraph, END
from nodes import clarify_input, generate_job_descriptions, generate_checklist, format_output, estimate_salary_ranges
from schema import HRHiringState  

def create_graph():
    builder = StateGraph(HRHiringState)

    builder.add_node("clarify", clarify_input)
    builder.add_node("generate_jd", generate_job_descriptions)
    builder.add_node("generate_checklist", generate_checklist)
    builder.add_node("estimate_salary", estimate_salary_ranges)
    builder.add_node("format_output", format_output)

    builder.set_entry_point("clarify")

    # Add transitions
    builder.add_conditional_edges(
        "clarify",
        lambda state: "generate_jd" if state.proceed else END
    )
    builder.add_edge("generate_jd", "generate_checklist")
    builder.add_edge("generate_checklist", "estimate_salary")
    builder.add_edge("estimate_salary", "format_output")
    builder.add_edge("format_output", END)

    return builder.compile()
