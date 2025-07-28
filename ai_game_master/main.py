# main.py
import chainlit as cl
from dotenv import load_dotenv
import asyncio
from agent import GameMasterRunner

load_dotenv()

# Runner ka instance banayein
game_runner = GameMasterRunner()

@cl.on_chat_start
async def start_chat():
    """Initialize the chat session with an immersive game intro."""
    await cl.Message(
        content="""⚔️ **Greetings, Adventurer!**

You find yourself at the edge of the **Whispering Woods**, a place of ancient magic and forgotten secrets. Local legends speak of a lost artifact, the 'Sunstone', hidden deep within. It is said to have the power to heal the blighted lands.

Before you lies a fork in the path. 
- To your **left**, a narrow trail disappears into the dark, gnarled trees. 
- To your **right**, the path follows a murmuring stream.

**What do you do?** (e.g., "Go left into the trees" or "Follow the stream to the right")
"""
    ).send()

@cl.on_message
async def main(message: cl.Message):
    """Main message handler that uses the GameMasterRunner."""
    try:
        # Poora workflow Runner se chalayein
        workflow_results = await game_runner.run_workflow(message.content)
        
        # Har agent ka result dikhayein
        for i, result in enumerate(workflow_results):
            await cl.Message(
                author=result["agent"],
                content=f"*{result['description']}*\n\n{result['response']}"
            ).send()
            
            # Agents ke darmiyan thora delay
            if i < len(workflow_results) - 1:
                await cl.Message(content="**🔄 Handing off to next phase...**").send()
                await asyncio.sleep(1)
        
        await cl.Message(content="\n---\n✅ **Turn Complete!** Type your next action to continue the adventure.").send()
        
    except Exception as e:
        await cl.Message(content=f"❌ An error occurred: {e}").send()