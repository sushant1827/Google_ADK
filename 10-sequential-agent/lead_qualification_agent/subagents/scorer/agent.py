"""
Lead Scorer Agent

This agent is responsible for scoring a lead's qualification level
based on various criteria.
"""

from google.adk.agents import LlmAgent


# Create the scorer agent

lead_scorer_agent = LlmAgent(
    name="lead_scorer_agent",
    model="gemini-2.0-flash",
    description="Scores qualified leads on a scale of 1-10.",
    instruction="""
    You are a lead scoring agent.
    
    Analyze the lead information and assign a score from 1 to 10 based on the following criteria:
    - Expressed need (urgency/clarity of problem)
    - Decision-making authority
    - Budget indicators
    - Timeline indicators

    Output ONLY a numeric score and ONE sentence justification.
    
    Example output: '8: Decision maker with clear budget and immediate need'
    Example output: '3: Vague interest with no timeline or budget mentioned'
    """,
    output_key="lead_score",
)