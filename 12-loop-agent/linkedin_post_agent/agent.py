"""
LinkedIn Post Generator Root Agent

This module defines the root agent for the LinkedIn post generation application.
It uses a sequential agent with an initial post generator followed by a refinement loop.
"""

from google.adk.agents import LoopAgent, SequentialAgent

from .subagents.post_generator import post_generator_agent
from .subagents.post_reviewer import post_reviewer_agent
from .subagents.post_refiner import post_refiner_agent


# Create the refinement loop agent

refinement_loop_agent = LoopAgent(
    name="refinement_loop_agent",
    max_iterations=5,
    sub_agents=[
        post_reviewer_agent,
        post_refiner_agent,
    ],
    description="Refines LinkedIn posts through review and refinement until they meet quality standards.",
)


# Create the root agent that orchestrates the post generation and refinement

root_agent = SequentialAgent(
    name="root_agent",
    description="Generates and refines LinkedIn posts through a review and refinement loop.",
    sub_agents=[
        post_generator_agent,
        refinement_loop_agent,
    ],
)