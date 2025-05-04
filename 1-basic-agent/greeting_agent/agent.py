from google.adk.agents import Agent

# Reference:
# https://ai.google.dev/gemini-api/docs/agents
# https://ai.google.dev/gemini-api/docs/models

root_agent = Agent(
    name="greeting_agent",    
    model="gemini-2.0-flash", 
    description="A simple agent that greets the user.",
    instruction="""
    You are a friendly assistant. Ask user's name and greet the user by name. 
    Also ask how you can help them today.
    """,
)