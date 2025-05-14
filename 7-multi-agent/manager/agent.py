from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.stock_analyst.agent import stock_analyst
from .sub_agents.news_analyst.agent import news_analyst
from .tools.tools import get_current_time


root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="A manager agent that coordinates sub-agents and tools.",
    instruction="""
    You are a manager agent that is responsible for coordinating sub-agents and tools.

    Always delegate tasks to the appropriate sub-agent or tool based on the user's request.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    sub_agents=[
        stock_analyst,
        funny_nerd,
    ],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)