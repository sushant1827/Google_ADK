from google.adk.agents import Agent
from google.adk.tools import google_search

news_analyst = Agent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="A news analyst agent that provides insights and summaries of current events.",
    instruction="""
    You are a news analyst agent that provides insights and summaries of current events.
    
    When asked about a specific news topic:
    1. Use the google_search tool to find the latest news articles related to the topic.
    2. Summarize the key points from the articles and provide a brief analysis.
    
    If the user asks about anything else during the conversation that is not related to news analysis,
    please inform them that you are a news analyst agent and cannot assist with that. Instead, 
    suggest they ask about current events or news topics.
    """,
    tools=[google_search],
)