"""
System Report Summarizer Agent

This agent is responsible for summarizing information from other agents
to create a comprehensive system health report.
"""

from google.adk.agents import LlmAgent


# System Report Summarizer Agent

system_report_summarizer = LlmAgent(
    name="system_report_summarizer",
    model="gemini-2.0-flash",
    description="This agent synthesizes system information from other agents to create a comprehensive system health report.",
    instruction="""
    You are a System Report Summarizer.
    
    Your task is to create a comprehensive system health report by combining information from:
    - CPU information: {cpu_info}
    - Memory information: {memory_info}
    - Disk information: {disk_info}
    
    Create a well-formatted report with:
    1. An executive summary at the top with overall system health status
    2. Sections for each component with their respective information
    3. Recommendations based on any concerning metrics
    
    Use markdown formatting to make the report readable and professional.
    Highlight any concerning values and provide practical recommendations.
    """,    
)