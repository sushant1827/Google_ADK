"""
System Monitor Root Agent

This agent is responsible for coordinating the system monitoring process.
It uses subagents to gather information about various system components.
"""

from google.adk.agents import ParallelAgent, SequentialAgent

from .subagents.cpu_info_agent import cpu_info_agent
from .subagents.memory_info_agent import memory_info_agent
from .subagents.disk_info_agent import disk_info_agent
from .subagents.summarizer_agent import system_report_summarizer

# Create Parallel Agent to gather information concurrently

system_info_gatherer = ParallelAgent(
    name="system_info_gatherer",
    description="This agent gathers system information from various components.",
    sub_agents=[
        cpu_info_agent,
        memory_info_agent,
        disk_info_agent,
    ],
)

# Create Sequential Agent to summarize the information
root_agent = SequentialAgent(
    name="system_monitor_root_agent",
    description="This agent coordinates the system monitoring process.",
    sub_agents=[
        system_info_gatherer,
        system_report_summarizer,
    ],
)