from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

import os
import random

# https://docs.litellm.ai/docs/providers/openrouter

model = LiteLlm(
    model="openrouter/openai/gpt-4.1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def get_dad_joke():
    jokes = [
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? A waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]
    return random.choice(jokes)


root_agent = Agent(
    name="dad_joke_agent",
    description="An agent that tells dad jokes.",
    model=model,
    instruction="""
    You are a dad joke agent. Your job is to tell dad jokes. 
    If the user asks for a dad joke, tell them one only using the tool 'get_dad_joke'.
    If they ask for something else, tell them you only know dad jokes.
    """,
    tools=[get_dad_joke],
)
    