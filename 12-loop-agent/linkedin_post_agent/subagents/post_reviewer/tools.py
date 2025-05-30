"""
Tools for LinkedIn Post Reviewer Agent

This module provides tools for analyzing and validating LinkedIn posts  
"""

from typing import Any, Dict
from google.adk.tools.tool_context import ToolContext


def count_characters(text: str, tool_context: ToolContext) -> Dict[str, Any]:
    """
    Count the number of characters in the given text and provide the count.
    Updates the tool context with the character count.

    Args:
        text (str): The text to analyze and count characters for.
        tool_context (ToolContext): The context for accessing and updating tool state.

    Returns:
        Dict[str, Any]: A dictionary containing:
            - result: 'pass' or 'fail' 
            - character_count: The number of characters in the text.
            - message: A message indicating the character count.

    """

    character_count = len(text)
    MIN_LENGTH = 1000
    MAX_LENGTH = 3000

    print("\n------------- TOOL DEBUG -------------")
    print(f"Text Length: {character_count} characters")
    print("--------------------------------------\n")

    if character_count < MIN_LENGTH:
        chars_needed = MIN_LENGTH - character_count
        tool_context.state["review_status"] = "fail"
        return {
            "result": "fail",
            "character_count": character_count,
            "chars_needed": chars_needed,
            "message": f"Post is too short. Needs at least {MIN_LENGTH} characters, but has only {character_count} characters.",
        }
    
    elif character_count > MAX_LENGTH:
        chars_to_remove = character_count - MAX_LENGTH
        tool_context.state["review_status"] = "fail"
        return {
            "result": "fail",
            "character_count": character_count,
            "chars_to_remove": chars_to_remove,
            "message": f"Post is too long. Needs at most {MAX_LENGTH} characters, but has {character_count} characters.",
        }
    
    else:
        tool_context.state["review_status"] = "pass"
        return {
            "result": "pass",
            "character_count": character_count,
            "message": f"Post is valid with {character_count} characters.",
        }
    

def exit_loop(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Call this function ONLY when the post meets all requirements and signals the end of the review loop.

    Args:
        tool_context (ToolContext): The context for tool execution and state management.
    
    Returns:
        Empty dictionary to signal the end of the loop.
    """

    print("\n------------- EXIT LOOP TRIGGERED -------------")
    print("Exiting the review loop as the post meets all requirements.")
    print("-----------------------------------------------\n")

    tool_context.actions.escalate = True
    return {}