from item import admin_key, mana_crystal

class NPC:
    def __init__(self, name, description, dialogue, quest=None, reward=None):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.quest = quest
        self.reward = reward

        def talk(self):
            for line in self.dialogue:
                print(line)

        def give_quest(self):
            if self.quest:
                print(f"{self.name} offers you a quest: {self.quest['description']}")
                return self.quest
            else:
                print(f"{self.name} has nothing more for you.")
                return None
        def give_reward(self):
            if self.reward:
                print(f"{self.name} rewards you with: {self.reward.name}")
                return self.reward
            else:
                print(f"{self.name} has nothing more for you.")
                return None

# Define NPC Marcus
marcus_dialogue = [
    "You... you're not corrupted. There may still be hope.",
    "The Daemon Overlord twisted the Filesystem, and only by collecting the Corrupted Stones can we hope to stabilize it.",
    "Head towards the Corrupted Sector and find the Corruption Stones. Only then can we proceed."
]

marcus = NPC(
    name="Marcus",
    description="A spectral figure with a fading digital aura. Marcus looks lost, but his eyes convey a sense of urgency.",
    dialogue=[marcus_dialogue],
    quest={"description": "Collect the Corrupted Stones to stabilize the sector."},
    reward=admin_key
)

# Define NPC Evelyn
evelyn_dialogue = [
    "We, the Echoes of Resistance, have hidden in the Twisted Passage for too long.",
    "To fight back, you will need the Admin Keys scattered throughout the system. They will help you unlock critical directories and access the tools needed to push back against the Daemon Overlord."
]

evelyn = NPC(
    name="Evelyn",
    description="A flickering form who seems determined. Evelyn is the leader of the Echoes of Resistance, and she has a plan.",
    dialogue=evelyn_dialogue,
    quest={"description": "Find the scattered Admin Key to gain access to the Server Room."}
)

lost_user_lila = NPC(
    name="Lila",
    description="A flickering form, her data seems incomplete. She looks at you with pleading eyes.",
    dialogue=[
        "I was disconnected when everything went wrong. If only someone could restore my data..."
    ],
    quest=None,
    reward=mana_crystal 
)
