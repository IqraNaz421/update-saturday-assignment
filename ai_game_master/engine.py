# engine.py (Updated to use OpenAI Agent SDK)
import json
import time
import chainlit as cl
import os
from openai import OpenAI
from agent import NarratorAgent, MonsterAgent, ItemAgent
from tools import roll_dice, generate_event

# tool_map ko yahan define karein
tool_map = {
    "roll_dice": roll_dice,
    "generate_event": generate_event,
}

class GameEngine:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.agents = {
            'narrator': NarratorAgent(),
            'monster': MonsterAgent(),
            'item': ItemAgent(),
        }
        self.tools = {
            'roll_dice': roll_dice,
            'generate_event': generate_event,
        }
        self.state = {}
        self.current_agent = 'narrator'

    def ask_openai(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def run(self):
        print("Welcome to the Fantasy Adventure Game!")
        while self.current_agent != 'end':
            agent = self.agents.get(self.current_agent)
            if not agent:
                print(f"Unknown agent: {self.current_agent}")
                break
            if self.current_agent == 'narrator':
                # Use OpenAI to generate narration
                prompt = "You are the narrator of a fantasy adventure game. Continue the story based on the player's previous actions."
                ai_response = self.ask_openai(prompt)
                print(ai_response)
                output, next_agent = agent.handle(self.state, self.tools)
            else:
                output, next_agent = agent.handle(self.state, self.tools)
                print(output)
            self.current_agent = next_agent
        print("Game Over!")