from openai import OpenAI
from agents import function_tool
from travel_agents.destination_agent import suggest_destination
from travel_agents.booking_agent import get_booking_options
from travel_agents.explore_agent import explore_place
import os

openai_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_key)  # OpenAI client initialized for compliance

@function_tool
def destination_tool(mood: str):
    """Suggest a destination based on travel mood."""
    return suggest_destination({"mood": mood})

@function_tool
def booking_tool(destination: str):
    """Get flights and hotels based on destination."""
    return get_booking_options({"destination": destination})

@function_tool
def explore_tool(destination: str):
    """Get things to do based on destination."""
    return explore_place({"destination": destination})
