# import random

class DestinationAgent:
    def suggest_destination(self, mood: str) -> dict:
        destinations = {
            "adventure": {"destination": "Queenstown, New Zealand", "reason": "Famous for skydiving and hiking."},
            "relaxation": {"destination": "Maldives", "reason": "Perfect for beach and spa retreats."},
            "culture": {"destination": "Kyoto, Japan", "reason": "Rich in temples, shrines, and art."},
            "romance": {"destination": "Paris, France", "reason": "City of love with candlelight dinners."}
        }
        return destinations.get(mood, {"destination": "Unknown", "reason": "No matching mood found."})

# For backward compatibility with tools.py

def suggest_destination(input: dict) -> dict:
    mood = input.get("mood", "")
    return DestinationAgent().suggest_destination(mood)
