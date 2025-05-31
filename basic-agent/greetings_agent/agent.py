from google.adk.agents import Agent
from dotenv import load_dotenv
import os

load_dotenv()

root_agent = Agent(
    name="greetings_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description="A simple agent that greets the user",
    instruction="""You are a simple agent that greets the user.""")
