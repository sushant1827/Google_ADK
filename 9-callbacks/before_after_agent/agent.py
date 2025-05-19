"""
Before and After Agent Callbacks Example

This example demonstrates how to use both before_agent_callback and after_agent_callback 
for logging purposes.
"""

from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types

from datetime import datetime
from typing import Optional


# Before Agent Callback
def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Simple callback that logs when the agent starts processing a request.

    Args:
        callback_context: Contains state and context information

    Returns:
        None to continue with normal agent processing
    """

    # Get the session state
    state = callback_context.state

    # Log the start time
    timestamp = datetime.now()

    # Set the agent name if not already set
    if "agent_name" not in state:
        state["agent_name"] = "SimpleChatBot" 

    # Initialize request counter
    if "request_counter" not in state:
        state["request_counter"] = 1
    else:
        state["request_counter"] += 1

    # Store start time for duration calculation
    state["request_start_time"] = timestamp

    # Log the request
    print("===== AGENT REQUEST STARTED =====")
    print(f"Request #: {state['request_counter']}")
    print(f"Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')}")

    # Print to console
    print(f"\n[BEFORE AGENT CALLBACK] Agent processing request #{state['request_counter']}...")

    return None


# After Agent Callback
def after_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Simple callback that logs when the agent finishes processing a request.

    Args:
        callback_context: Contains state and context information

    Returns:
        None to continue with normal agent processing
    """

    # Get the session state
    state = callback_context.state

    # Log the end time
    timestamp = datetime.now()
    duration = None

    if "request_start_time" in state:
        duration = (timestamp - state["request_start_time"]).total_seconds()

    # Log the completion
    print("===== AGENT EXECUTION COMPLETED =====")
    print(f"Request #: {state.get('request_counter', 'Unknown')}")

    if duration is not None:
        print(f"Duration: {duration:.2f} seconds")

    # Print to console
    print(f"\n[AFTER AGENT CALLBACK] Request #{state.get('request_counter', 'Unknown')} completed.")

    if duration is not None:
        print(f"\n[AFTER AGENT CALLBACK] Duration: {duration:.2f} seconds")

    return None


# Create the agent

root_agent  = LlmAgent(    
    name="before_after_agent",
    model="gemini-2.0-flash",
    description="A simple agent that demonstrates before and after agent callbacks.",
    instruction="""
    You are a friendly greeting agent. Your name is {agent_name}.
    
    Your job is to:
    - Greet users politely
    - Respond to basic questions
    - Keep your responses friendly and concise
    """,
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback,
)

    