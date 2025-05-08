from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# -------------------------------------
# Define the agent's output schema
# -------------------------------------

class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject of the email. Should be concise and relevant."
        )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
        )

# -------------------------------------
# Define Email Generator agent
# -------------------------------------

root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="An agent that generates professional emails with structured subject and body",
    instruction="""
    You are an Email Generation Assistant.
    Your task is to generate a professional email based on the user's request.

    GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

    DO NOT include any explanations or additional text outside the JSON response.
    """,
    output_schema=EmailContent,
    output_key="email",
)
