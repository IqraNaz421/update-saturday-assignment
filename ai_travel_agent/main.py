import chainlit as cl
import os
from openai import OpenAI
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel
from tools import destination_tool, booking_tool, explore_tool

# Load API key
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# llm object is created correctly
llm = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gpt-3.5-turbo"
)

# Define the single, powerful agent
class TravelDesignerAgent(Agent):
    def __init__(self):
        # FIX: Agent's instructions are made very specific so it knows what to do.
        # The custom `run` method has been REMOVED.
        super().__init__(
            name="TravelDesignerAgent",
            instructions=(
                "You are an expert travel planner. Your goal is to create a complete travel itinerary based on the user's mood. "
                "You must follow these steps in order:\n"
                "1. Use the `destination_tool` to find a suitable destination based on the user's input.\n"
                "2. Use the `booking_tool` to find flight and hotel options for that destination.\n"
                "3. Use the `explore_tool` to find activities and things to do at the destination.\n"
                "Finally, combine all the information into a single, well-formatted, and friendly response for the user. Present the final plan clearly with headings for each section (Destination, Flights & Hotels, Things to Do)."
            ),
            # Give all tools to this one agent
            tools=[destination_tool, booking_tool, explore_tool]
        )

# Instantiate the single agent
travel_agent = TravelDesignerAgent()

@cl.on_chat_start
async def start():
    await cl.Message(
        content=(
            "🌍 **Welcome to the AI Travel Designer Agent!**\n\n"
            "I'm here to plan your perfect trip from destination ideas to flights, hotels, food, and attractions. 😎\n\n"
            "✈️ Just tell me your **travel mood or interest** to begin:\n"
            "- `adventure` (e.g. skydiving, hiking)\n"
            "- `relaxation` (e.g. beaches, spa)\n"
            "- `culture` (e.g. history, temples, art)\n"
            "- `romance` (e.g. candlelight dinners, city of love)"
        )
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # FIX: Use the Runner to let the agent decide how to use tools.
    # We will await the final result and send it in one go.
    # This is the correct way to use the agent.
    msg = cl.Message(content="")
    await msg.send()

    result = await Runner.run(travel_agent, message.content.strip())
    
    await cl.Message(content=result.final_output).send()
