"""
Lead Validator Agent

This agent is responsible for validating if a lead has all the necessary information
for qualification.
"""

from google.adk.agents import LlmAgent


# Create the validator agent

lead_validator_agent = LlmAgent(
    name="lead_validator_agent",
    model="gemini-2.0-flash",
    description="Validates if a lead has all the necessary information for qualification.",
    instruction="""
    You are a lead validation agent.

    Examine the lead information provided by the user and determine if it's complete enough for qualification.
    A complete lead should include:
    - Contact information (name, email or phone)
    - Some indication of interest or need
    - Company or context information if applicable
    
    Output ONLY 'valid' or 'invalid' with a single reason if invalid.
    
    Example valid output: 'valid'
    Example invalid output: 'invalid: missing contact information'
    """,
    output_key="validation_status",
)