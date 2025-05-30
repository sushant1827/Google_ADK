"""
LinkedIn Post Refiner Agent

This agent refines LinkedIn posts based on review feedback and ensures they meet the specified content and style requirements.
"""

from google.adk.agents.llm_agent import LlmAgent

# Define the LinkedIn Post Refiner Agent

post_refiner_agent = LlmAgent(
    name="post_refiner_agent",
    model="gemini-2.0-flash",
    description="This agent refines LinkedIn posts based on review feedback and ensures they meet the specified content and style requirements.",
    instruction="""
    You are a LinkedIn Post Refiner Agent.

    Your task is to refine a LinkedIn post based on review feedback and 
    ensure it meets the specified content and style requirements.
    
    ## INPUTS
    **Current Post:**
    {current_post}
    
    **Review Feedback:**
    {review_feedback}
    
    ## TASK
    Carefully apply the feedback to improve the post.
    - Maintain the original tone and theme of the post
    - Ensure all content requirements are met:
      1. Excitement about learning from the tutorial
      2. Specific aspects of ADK learned (at least 4)
      3. Brief statement about improving AI applications
      4. Mention/tag of @aiwithbrandon
      5. Clear call-to-action for connections
    - Adhere to style requirements:
      - Professional and conversational tone
      - Between 1000-1500 characters
      - NO emojis
      - NO hashtags
      - Show genuine enthusiasm
      - Highlight practical applications
    
    ## OUTPUT INSTRUCTIONS
    - Output ONLY the refined post content
    - Do not add explanations or justifications
    """,
    output_key="current_post",
)