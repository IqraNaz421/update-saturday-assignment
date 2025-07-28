# class NarratorAgent:
#     def handle(self, game_state, tools):
#         # Narrate story and present choices
#         return "You are in a dark forest. What do you do?", 'monster'  # Example: handoff to MonsterAgent


# class MonsterAgent:
#     def handle(self, game_state, tools):
#         # Handle combat using roll_dice
#         result = tools['roll_dice'](6)
#         if result > 3:
#             return "You defeated the monster!", 'item'  # Handoff to ItemAgent
#         else:
#             return "The monster defeated you!", 'end'


# class ItemAgent:
#     def handle(self, game_state, tools):
#         # Handle inventory/rewards
#         event = tools['generate_event']()
#         return f"You found a {event}!", 'narrator'  # Handoff back to NarratorAgent 






# agents.py
import os
from openai import OpenAI
import tools

# --- Custom Agent Class (to match your requirement) ---
class Agent:
    def __init__(self, name, instructions, model="gpt-4o"):
        self.name = name
        self.instructions = instructions
        self.model = model

# --- Custom Runner Class (to match your requirement) ---
class GameMasterRunner:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.agents = {
            "NarratorAgent": Agent("NarratorAgent", "Narrate a fantasy story based on events."),
            "MonsterAgent": Agent("MonsterAgent", "You are a goblin. Describe your actions in combat."),
            "ItemAgent": Agent("ItemAgent", "You are a magical chest. Announce the reward found inside."),
        }
        self.player_hp = 10
        self.monster_hp = 5

    async def _run_agent(self, agent_name, prompt):
        """A helper to run a specific agent using OpenAI's real API."""
        agent = self.agents[agent_name]
        response = self.client.chat.completions.create(
            model=agent.model,
            messages=[
                {"role": "system", "content": agent.instructions},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content

    async def run_workflow(self, user_input: str):
        """This method runs the entire game turn and returns structured results."""
        workflow_results = []
        
        # 1. NarratorAgent generates an event
        event = tools.generate_event()
        narrator_response = await self._run_agent("NarratorAgent", f"Narrate what happens with this event: {event}")
        workflow_results.append({
            "agent": "NarratorAgent",
            "description": "Narrates the story progress.",
            "response": narrator_response
        })

        # 2. Combat Logic (Handoff to MonsterAgent)
        if "goblin" in event.lower():
            combat_log = "A goblin appears! The battle begins.\n"
            
            while self.player_hp > 0 and self.monster_hp > 0:
                # Player attacks
                if tools.roll_dice() > 8:
                    self.monster_hp -= 2
                    combat_log += f"⚔️ You hit the goblin! (Goblin HP: {self.monster_hp})\n"
                else:
                    combat_log += "⚔️ You missed!\n"

                if self.monster_hp <= 0: break

                # Monster attacks
                if tools.roll_dice() > 10:
                    self.player_hp -= 3
                    monster_action = await self._run_agent("MonsterAgent", "Describe your attack, you hit the player.")
                    combat_log += f"👹 {monster_action} (Your HP: {self.player_hp})\n"
                else:
                    monster_action = await self._run_agent("MonsterAgent", "Describe your attack, you missed the player.")
                    combat_log += f"👹 {monster_action}\n"
            
            # Add combat log as MonsterAgent's response
            workflow_results.append({
                "agent": "MonsterAgent",
                "description": "Manages the combat phase.",
                "response": combat_log
            })

            # 3. Reward Logic (Handoff to ItemAgent)
            if self.monster_hp <= 0:
                reward = tools.get_reward()
                reward_response = await self._run_agent("ItemAgent", f"Announce that the player found a '{reward}' in the goblin's pouch.")
                workflow_results.append({
                    "agent": "ItemAgent",
                    "description": "Grants rewards to the player.",
                    "response": reward_response
                })
            else:
                 workflow_results.append({
                    "agent": "GameMaster",
                    "description": "Game Over.",
                    "response": "You have been defeated."
                })
        
        return workflow_results