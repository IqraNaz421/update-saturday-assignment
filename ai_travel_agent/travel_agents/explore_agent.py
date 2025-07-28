class ExploreAgent:
    def explore(self, destination: str) -> str:
        guides = {
            "queenstown, new zealand": (
                "- 🪂 **Skydive Queenstown** – Jump from 15,000ft with stunning mountain views\n"
                "- 🥾 **Ben Lomond Track** – Full-day scenic alpine hike\n"
                "- 🍔 **Fergburger** – World-famous gourmet burgers\n"
                "- 🚠 **Skyline Gondola** – Ride to the top for breathtaking views"
            ),
            "bali, indonesia": (
                "- 🛕 **Uluwatu Temple** – Cliffside temple with ocean sunset views\n"
                "- 🧘 **Yoga Barn in Ubud** – Peaceful yoga sessions in jungle surroundings\n"
                "- 🏖️ **Seminyak Beach** – Ideal for sunbathing and surfing\n"
                "- 🦞 **Seafood at Jimbaran Bay** – Beachfront dining with grilled seafood"
            ),
            "kyoto, japan": (
                "- ⛩️ **Fushimi Inari Shrine** – Famous red torii gate path\n"
                "- 👘 **Gion District** – Spot geishas and explore traditional tea houses\n"
                "- 🏯 **Kinkaku-ji (Golden Pavilion)** – Zen temple covered in gold leaf\n"
                "- 🍱 **Kaiseki Dinner** – Multi-course traditional Japanese cuisine"
            ),
            "paris, france": (
                "- 🗼 **Eiffel Tower** – Climb or ride up for panoramic city views\n"
                "- 🖼️ **Louvre Museum** – See Mona Lisa and 30,000+ artworks\n"
                "- 🛍️ **Champs-Élysées** – High-end shopping and Arc de Triomphe\n"
                "- ☕ **Cafe de Flore** – Iconic Parisian café for people-watching"
            ),
            "barcelona, spain": (
                "- ⛪ **Sagrada Familia** – Antoni Gaudí’s stunning basilica\n"
                "- 🏰 **Gothic Quarter** – Historic streets and Roman ruins\n"
                "- 🍽️ **Tapas Tour** – Try patatas bravas, croquettes, and sangria\n"
                "- 🏖️ **Barceloneta Beach** – Relax or bike along the seafront"
            )
        }
        key = destination.lower().strip()
        return guides.get(
            key,
            f"Explore museums, local food markets, and take a city tour in {destination}."
        )

# For backward compatibility with tools.py

def explore_place(input: dict) -> dict:
    destination = input.get("destination", "the destination")
    return {"things_to_do": ExploreAgent().explore(destination)}
