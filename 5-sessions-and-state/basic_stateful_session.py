import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent.agent import question_answering_agent

load_dotenv()

# Create a session service to manage the state
session_service = InMemorySessionService()

initial_state = {
    "user_name": "John Doe",
    "user_age": 30,
    "user_location": "New York",
    "user_interests": ["reading", "traveling", "coding"],
    "user_preferences": {
        "language": "English",
        "food": "pizza",
        "music": "rock",
        "tv shows": ["Breaking Bad", "Game of Thrones"],
        "movies": ["Inception", "The Matrix"],
    }
}

# Create a new session
APP_NAME = "John Doe's Assistant"
USER_ID = "John_Doe"
SESSION_ID = str(uuid.uuid4())

stateful_session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
print("===== CREATED A NEW SESSION: =====")
print(f"Session ID: {SESSION_ID}")

# Create a new agent runner
runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service,
)

# Send a message to the agent
new_message = types.Content(
    role="user",
    parts=[types.Part(text="What are John Doe's favorite movies?")],
)

# Send the message to the agent and get the response
for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"===== FINAL RESPONSE: =====")
            print(event.content.parts[0].text)

print("===== Session Events: =====")
session = session_service.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
)

print("===== Final Session State: =====")
for key, value in session.state.items():
    print(f"{key}: {value}")