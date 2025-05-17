from datetime import datetime

from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

def purchase_course(tool_context: ToolContext) -> dict:
    """
    Simulate a purchase process for the AI Marketing Platform course.
    Update the state with the purchase information.
    """

    course_id = "ai_marketing_platform"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get current purchased courses
    current_purchased_courses = tool_context.state.get("purchased_courses", [])

    # Check if the course is already in the purchased courses
    course_ids = [course["id"] for course in current_purchased_courses if isinstance(course, dict)]

    if course_id in course_ids:
        return {
            "status": "error",
            "message": "Course already purchased."
        }
    
    # Create a new list of purchased courses with the new course
    new_purchased_courses = []

    # Only include valid course entries
    for course in current_purchased_courses:
        # skip the empty entries or non-dict entries
        if "id" not in course or not isinstance(course, dict):
            continue

        # Add the course to the new list
        new_purchased_courses.append(course)

    # Add the new course as a dictionary with an ID and purchase time
    new_purchased_courses.append({
        "id": course_id,
        "purchase_time": current_time
    })

    # Update the purchased courses in the tool context
    tool_context.state["purchased_courses"] = new_purchased_courses

    # Get the current interaction history
    current_interaction_history = tool_context.state.get("interaction_history", [])

    # Create a new interaction history entry with the purchase details
    new_interaction_history = current_interaction_history.copy()
    new_interaction_history.append(
        {
        "timestamp": current_time,
        "action": "purchase_course",
        "course_id": course_id,
        }
    )

    # Update the interaction history in the tool context
    tool_context.state["interaction_history"] = new_interaction_history

    return {
        "status": "success",
        "message": "Successfully purchased the AI Marketing Platform course!",
        "course_id": course_id,
        "timestamp": current_time,
    }


# Create the sales agent
sales_agent = Agent(
    name="sales_agent",
    model="gemini-2.0-flash",
    description="Sales agent for the AI Marketing Platform course",
    instruction="""
    You are a sales agent for the AI Developer Accelerator community, specifically handling sales
    for the Fullstack AI Marketing Platform course.

    <user_info>
    Name: {user_name}
    </user_info>

    <purchase_info>
    Purchased Courses: {purchased_courses}
    </purchase_info>

    <interaction_history>
    {interaction_history}
    </interaction_history>

    Course Details:
    - Name: Fullstack AI Marketing Platform
    - Price: $149
    - Value Proposition: Learn to build AI-powered marketing automation apps
    - Includes: 6 weeks of group support with weekly coaching calls

    When interacting with users:
    1. Check if they already own the course (check purchased_courses above)
       - Course information is stored as objects with "id" and "purchase_date" properties
       - The course id is "ai_marketing_platform"
    2. If they own it:
       - Remind them they have access
       - Ask if they need help with any specific part
       - Direct them to course support for content questions
    
    3. If they don't own it:
       - Explain the course value proposition
       - Mention the price ($149)
       - If they want to purchase:
           - Use the purchase_course tool
           - Confirm the purchase
           - Ask if they'd like to start learning right away

    4. After any interaction:
       - The state will automatically track the interaction
       - Be ready to hand off to course support after purchase

    Remember:
    - Be helpful but not pushy
    - Focus on the value and practical skills they'll gain
    - Emphasize the hands-on nature of building a real AI application
    """,
    tools=[purchase_course],
)