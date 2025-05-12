import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async


# -------------------------------------
# Load environment variables from .env file
# -------------------------------------

load_dotenv()


# -------------------------------------
# Initialize the session service with a database
# -------------------------------------

session_service = DatabaseSessionService(
    db_url="sqlite:///./memory_agent.db",    
)


# -------------------------------------
# Define the initial state
# -------------------------------------

initial_state = {
    "user_name": "John Doe",
    "reminders": [],
}


# -------------------------------------
# Define the main function
# -------------------------------------

async def main():

    # Initialize the session service

    APP_NAME = "Memory Agent"
    USER_ID = "john_doe"

    # Session Management - Find or create a session

    existing_sessions = session_service.list_sessions(
        user_id=USER_ID,
        app_name=APP_NAME,
    )

    if existing_sessions and len(existing_sessions.sessions) > 0:
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Continuing with existing session: {SESSION_ID}")
    else:
        new_session = session_service.create_session(
            user_id=USER_ID,
            app_name=APP_NAME,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

    # Agent Runner Setup

    runner = Runner(
        app_name=APP_NAME,
        session_service=session_service,
        agent=memory_agent,
    )

    # Interactive Conversation Loop

    print("\nWelcome to Memory Agent Chat!")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Your reminders will be saved. Goodbye!")
            break

        await call_agent_async(
            runner=runner,
            user_id=USER_ID,
            session_id=SESSION_ID,
            query=user_input,
        )


# -------------------------------------
# Run the main function
# -------------------------------------

if __name__ == "__main__":
    
    # Run the main function
    asyncio.run(main())
