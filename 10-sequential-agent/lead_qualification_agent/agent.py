"""
Sequential Agent with a Minimal Callback

This example demonstrates a lead qualification pipeline with a minimal
before_agent_callback that only initializes state once at the beginning.
"""

from google.adk.agents import SequentialAgent

from .subagents.recommender import action_recommender_agent
from .subagents.scorer import lead_scorer_agent
from .subagents.validator import lead_validator_agent

# Create a sequential agent with a minimal callback

root_agent = SequentialAgent(
    name="lead_qualification_pipeline",
    description="A lead qualification pipeline that validates, scores, and recommends actions for sales leads.",
    sub_agents=[
        lead_validator_agent,
        lead_scorer_agent,
        action_recommender_agent,
    ],
)