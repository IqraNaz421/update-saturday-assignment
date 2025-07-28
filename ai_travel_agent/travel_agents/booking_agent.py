class BookingAgent:
    def get_flights(self, destination: str) -> str:
        return (
            "- Flight 1: Non-stop, $500\n"
            "- Flight 2: 1 stop, $450\n"
            "- Flight 3: Budget Airline, $350 (hand carry only)"
        )

    def suggest_hotels(self, destination: str) -> str:
        return (
            "- Hotel Lux ⭐⭐⭐⭐: $120/night – Sea view and spa included\n"
            "- Comfort Inn ⭐⭐⭐: $80/night – Breakfast and pool access\n"
            "- Budget Stay ⭐⭐: $50/night – Simple and clean rooms"
        )

# For backward compatibility with tools.py

def get_booking_options(input: dict) -> dict:
    destination = input.get("destination", "your location")
    agent = BookingAgent()
    return {
        "flights": agent.get_flights(destination),
        "hotels": agent.suggest_hotels(destination)
    }
