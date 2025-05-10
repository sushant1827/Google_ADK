from google.adk.agents import Agent

# create a root agent
question_answering_agent = Agent(
    name="question_answering_agent",
    model="gemini-2.0-flash",
    description="An agent that answers questions.",
    instruction="""
    You are a helpful assistant that answers questions about the user's information.

    Here is some information about the user:
    Name: 
    {user_name}
    Age: 
    {user_age}
    Location:
    {user_location}
    Interests:
    {user_interests}
    Preferences: 
    {user_preferences}
    """,
)