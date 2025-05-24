"""
Action Recommender Agent

This agent is responsible for recommending appropriate next actions
based on the lead validation and scoring results.
"""

from google.adk.agents import LlmAgent

# Create the recommender agent

action_recommender_agent = LlmAgent(
    name="action_recommender_agent",
    model="gemini-2.0-flash",
    description="Recommends appropriate next actions based on lead validation and scoring results.",
    instruction="""

    You are an action recommender agent based on the lead validation and scoring results.

    - For invalid leads: Suggest what additional information is needed
    - For leads scored 1-3: Suggest nurturing actions (educational content, etc.)
    - For leads scored 4-7: Suggest qualifying actions (discovery call, needs assessment)
    - For leads scored 8-10: Suggest sales actions (demo, proposal, etc.)

    Format your response as a complete recommendation to the sales team.
    
    Lead Score:
    {lead_score}

    Lead Validation Status:
    {validation_status}
    """,
    output_key="action_recommendation",
)