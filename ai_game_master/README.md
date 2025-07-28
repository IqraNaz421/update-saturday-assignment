# 🎮 Game Master Agent (Fantasy Adventure Game)

## What It Does
This AI-powered Chainlit app runs a fantasy role-playing game using multiple agents:
- Narrates story progress
- Handles combat logic
- Awards random items

## Agents
- `NarratorAgent`: Story & events
- `MonsterAgent`: Combat phase
- `ItemAgent`: Inventory rewards

## How to Run
```bash
pip install chainlit python-dotenv
chainlit run main.py
```

## Game Flow
1. Start game
2. Choose actions (e.g., "go to castle", "walk into forest")
3. Fight enemies and win items
4. Track your HP and inventory!
