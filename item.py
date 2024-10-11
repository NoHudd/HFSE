class Item:
    def __init__(self, name, description, usable_in_combat=False, damage=0, heal=0, key_for=None, 
                 strength_boost=0, mana_boost=0, quest_item=False, consumable=False, other_effect=None):
        self.name = name
        self.description = description
        self.usable_in_combat = usable_in_combat
        self.damage = damage
        self.heal = heal
        self.key_for = key_for
        self.strength_boost = strength_boost
        self.mana_boost = mana_boost
        self.quest_item = quest_item
        self.consumable = consumable  # Add the consumable parameter here
        self.other_effect = other_effect
     
    def use(self):
        if self.name == "Computer Manual":
            return "This manual shows a section titled 'Bypassing Security Protocol.' It mentions something about the aligning the server nodes in the correct sequence to disable the firewall. I think this has to do with the 'Server Room'."
        elif self.name == "Ancient Map":
            return """
            Level 1 Map:
            - Closet -> Bedroom -> Hallway -> Bathroom
            - Hallway -> Kitchen
            - Hallway -> Basement -> Server Room
            """
        return f"You used the {self.name}, but nothing significant happened."
    
pocket_knife = Item(
    name="Pocket Knife", 
    description="A small knife used in combat, deals 5 damage", 
    damage=5, 
    heal=0
)
flashlight = Item(
    name="Flashlight", 
    description="A bright flashlight to illuminate dark areas.", 
    usable_in_combat=False
)
rusty_key = Item(
    name="Rusty Key", 
    description="An old, rusty key that might unlock something.", 
    usable_in_combat=False
)
first_aid_kit = Item(
    name="First Aid Kit", 
    description="A basic first aid kit for healing minor wounds.", 
    usable_in_combat=True, 
    heal=20, 
    consumable=True
)
old_key = Item(
    name="Old Key", 
    description="Another old key, perhaps for a different lock.", 
    usable_in_combat=False
)
banana = Item(
    name="Banana", 
    description="A bruised banana.", 
    heal=5
)
bread = Item(
    name="Bread", 
    description="A stale loaf of bread.", 
    heal=3
)
computer_manual = Item(
    name="Computer Manual", 
    description="An old, worn-out manual titled \"Administrator's Guide\". The pages are filled with cryptic notes and diagrams. One section stands out, mentioning 'bypassing security protocols by adjusting the server nodes.' This might be a clue to solve something deeper in the haunted system.", 
    usable_in_combat=False
)
health_potion = Item(
    name="Health Potion",
    description="A potion that restores 30 health points. Use it to heal in the midst of battle or after taking damage.",
    heal=30,
    consumable=True
)
firewall_extinguisher = Item(
    name="Firewall Extingusher",
    description="A mystical extinguisher capable of putting out magical flames. Deals extra damage to fiery enemies.",
    usable_in_combat=True,
    damage=15
)
ancient_tome = Item(
    name="Ancient Tome",
    description="A spellbook filled with powerful incantations. It can be used to attack enemies or unlock hidden areas.",
    usable_in_combat=True,
    damage=20
)
ancient_map = Item(
    name="Ancient Map",
    description="A worn-out parchment that reveals a map of Level 1 of the haunted filesystem. It marks key areas and paths.",
    quest_item=True
)
corruption_stone = Item(
    name="Corruption Stone",
    description="A mysterious stone used to stabilize corrupted areas in the filesystem. It seems to resonate with the corrupted walls.",
    key_for="Corrupted Sector"
)
mana_crystal = Item(
    name="Mana Crystal",
    description="A crystal filled with an ethreal glow. Restores 20 mana when used.",
    mana_boost=20,
    consumable=True
)
arcane_blade = Item(
    name="Arcane Blade",
    description="A sword that glows with an unnatural light. Its magic-infused strikes can cleave through even the toughest enemy.",
    damage=25,
    usable_in_combat=True
)
admin_key = Item(
    name="Admin Key",
    description="A master key with administrative privileges. It can be used to unlock restricted rooms and bypass security protocols.",
    key_for="Root Directory"  # Example: Unlocks a room named "Root Directory"
)
broken_computer_part = Item(
    name="Broken Computer Part",
    description="A damaged piece of hardware. It might be possible to repair or use it as a part of something larger.",
    quest_item=True  # Used as part of a quest or puzzle
)
