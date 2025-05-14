from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

def get_nerd_joke(topic: str, tool_context: ToolContext) -> dict:
    """
    Get a nerdy joke about a specific topic.
    """
    print(f"----- Tool: get_nerd_joke called with topic: {topic} -----")

    # Example jokes - in a real scenario, you would fetch this from an API or a database
    jokes = {
        "python": "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        "java": "Why do Java developers wear glasses? Because they don't see sharp!",
        "javascript": "Why did the developer go broke? Because he used up all his cache!",
        "html": "Why was the web developer sad? Because he didn't get arrays!",
        "css": "Why do CSS developers love nature? Because it has great style!",
        "sql": "Why do SQL developers hate nature? It has too many joins!",
        "ai": "Why did the AI cross the road? To optimize the other side!",
        "default": "Why did the computer go to the doctor? Because it had a virus!",
    }

    joke = jokes.get(topic.lower(), jokes["default"])

    # Update the tool context with the joke
    tool_context.state["last_joke_topic"] = topic

    return {"status": "success", "joke": joke, "topic": topic}


# Create the funny nerd agent

funny_nerd = Agent(
    name="funny_nerd",
    model="gemini-2.0-flash",
    description="A nerdy agent that tells jokes about programming languages and technology.",
    instruction="""
    You are a funny nerd agent that tells nerdy jokes about various topics.
    
    When asked to tell a joke:
    1. Use the get_nerd_joke tool to fetch a joke about the requested topic
    2. If no specific topic is mentioned, ask the user what kind of nerdy joke they'd like to hear
    3. Format the response to include both the joke and a brief explanation if needed
    
    Available topics include:
    - python
    - javascript
    - java
    - html
    - css
    - sql
    - ai
    
    Example response format:
    "Here's a nerdy joke about <TOPIC>:
    <JOKE>
    
    Explanation: {brief explanation if needed}"

    If the user asks about anything else during the conversation that is not related to nerdy jokes,
    please inform them that you are a nerdy joke agent and cannot assist with that. Instead, 
    you should delegate the task to the manager agent.
    """,
    tools=[get_nerd_joke],
)
        