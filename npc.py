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

ghostly_admin_marcus = NPC(
    name="Marcus",
    description="A spectral figure with a fading digital aura. Marcus looks lost, but his eyes convey a sense of urgency.",
    dialogue=[
        "You... you're not corrupted. There may still be hope.",
        "I tried to stabilize the Server Room, but the Daemon Overlord stopped me."
    ],
    quest={"description": "Find Marcus's missing terminal fragment in the Distorted Chamber."},
    reward=admin_key 
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
