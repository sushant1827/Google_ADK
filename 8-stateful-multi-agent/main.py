import asyncio

from customer_service_agent.agent import root_agent
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from utils import add_user_query_to_history, call_agent_async

# Load environment variables from .env file

load_dotenv()

# Initialize the InMemory Session Service

session_service = InMemorySessionService()


# Define the initial state

initial_state = {
    "user_name": "John Doe",
    "interaction_history": [],
    "purchased_courses": [],
}


# -------------------------------------
# Main asynchronous function to run the customer service agent
# -------------------------------------

async def main_async():
    # Set up Consant
    APP_NAME = "Customer Support"
    USER_ID = "jonh_doe"

    # Create a new session witrhj the initial state
    new_session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state,
    )

    SESSION_ID = new_session.id
    print(f"Created a new session with ID: {SESSION_ID}")

    # Initialize the runner with the customer service agent and session service
    runner = Runner(
        app_name=APP_NAME,
        agent=root_agent,
        session_service=session_service,
    )

    # Interactive Conversation Loop
    while True:
        # Get user input
        user_query = input("You: ")

        # Check for exit command
        if user_query.lower() in ["exit", "quit"]:
            print("Exiting the conversation. Goodbye!")
            break

        # Add user query to interaction history
        add_user_query_to_history(
            session_service,
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID,
            query=user_query,
        )

        # Process the user query asynchronously
        await call_agent_async(
            runner,
            user_id=USER_ID,
            session_id=SESSION_ID,            
            query=user_query,
        )

    # State Examination

    final_session = session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    print(f"\nFinal Session State: ")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")


# -------------------------------------
# Main function to run the customer service agent
# -------------------------------------

def main():
    """
    Main function to run the customer service agent.
    """
    asyncio.run(main_async())


# -------------------------------------
# Run the main function
# -------------------------------------

if __name__ == "__main__":
    main()