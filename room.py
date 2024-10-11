# This file contain the Room class and functions to create and manage rooms in the game.
from item import *
from enemy import *

class Room:
    def __init__(self, name, description, exits, items=None, enemies=None):
        self.name = name
        self.description = description
        self.exits = exits  # Dictionary: {"direction": connected_room_name}
        self.items = items or []  # List of items in the room
        self.enemies = enemies or []  # List of enemies in the room

    def describe(self):
        print(f"\n{self.name}")
        print("-" * len(self.name))
        print(self.description)


        if self.exits:
            print("Exits:", ", ".join(self.exits.keys()))

        if self.items:
            print("Items:", ", ".join([item.name for item in self.items])) # Extract item names before joining

        if self.enemies:
            print("Enemies:", ", ".join([enemy.name for enemy in self.enemies]))  # Assuming enemies have a 'name' attribute


# Dictionary to store all rooms for easy access by name
all_rooms = {}

def get_starting_room():
    # Define your starting room (closet)
    closet = Room("Closet", "A dark and cramped closet.", {"out": "Bedroom"}, items=[flashlight])
    all_rooms["Closet"] = closet 
    return closet

def get_room_by_name(name):
    """Retrieves a room object by its name."""
    return all_rooms.get(name)  # Returns the room or None if not found

# Define other rooms here, similar to the closet example
bedroom = Room(
    name="Bedroom", 
    description="A dimly lit bedroom with an unsettling feeling.", 
    exits={"south": "Closet", "east": "Hallway"}, 
    items=[rusty_key],
    enemies=[]
)
all_rooms["Bedroom"] = bedroom

hallway = Room(
    name="Hallway", 
    description="A long, creaky hallway with flickering lights.",
    exits={"west": "Bedroom", "north": "Bathroom", "south": "Kitchen"},
    items=[],
    enemies=[GhostlyFigure()]
    )
all_rooms["Hallway"] = hallway

bathroom = Room(
    name="Bathroom", 
    description="A small bathroom with a broken mirror and a leaky faucet.",
    exits={"south": "Hallway"}, 
    items=[first_aid_kit],
    enemies=[]
)
all_rooms["Bathroom"] = bathroom

kitchen = Room(
    name="Kitchen", 
    description="A dusty kitchen with an old fridge a broken stove, a flickering light and an aweful smell.",
    exits={"north": "Hallway"}, 
    items=[pocket_knife],
    enemies=[]
)
all_rooms["Kitchen"] = kitchen

basement = Room(
    name="Basement", 
    description="A dark and damp basement with a musty smell. Old boxes and cobwebs are around.",
    exits={"up": "Kitchen:Stairs"},
    items=[old_key, ancient_tome],
    enemies=[]
)
all_rooms["Basement"] = basement

server_room = Room(
    name="Server Room", 
    description="A cold room filled with humming servers. The lights flicker, casting long shadows. You can hear a faint whisper comingn from between the rows of equipment.",
    exits={"west": "Hallway", "down": "Basement"},
    items=[computer_manual],
    enemies=[GhostlyFigure()]
)
all_rooms["Server Room"] = server_room

archive_room = Room(
    name="Archive Room", 
    description="Stacks of old, dusty filing cabinets are scattered around. The room feels like it's holding secrets long forgotten. A Single, dim light bulb swings slowly from the ceiling.",
    exits={"east": "Hallway", "north": "Server Room"},
    items=[ancient_map],
    enemies=[]
)
all_rooms["Archive Room"] = archive_room

firewall_chamber = Room(
    name="Firewall Chamber", 
    description="The air in this room is hot and dry. A wall of fire blocks the only exit, and strange runes are etched into the walls. You sense something powerful is keeping you from leaving.",
    exits={"south": "Server Room"},
    items=[firewall_extinguisher],
    enemies=[Wraith()]
)
all_rooms["Firewall Chamber"] = firewall_chamber

recycle_bin = Room(
    name="Recycle Bin", 
    description="A cold and cluttered space filled with old, discarded items. Everthing looks slightly broken or incomplete, as if awaiting permanent deletion. You feel the presence of something lingering here.",
    exits={"north": "Basement"},
    items=[broken_computer_part],
    enemies=[RestlessSpirit()]
)
all_rooms["Recycle Bin"] = recycle_bin

root_directory = Room(
    name="Root Directory",
    description="An expansive, dimly lit room with a large pedestal in the center. Ancient symbols are inscribed on the floor. The pedestal seems to be waiting for something.",
    exits={"west": "Server Room", "east": "Firewall Chamber"},
    items=[admin_key],
    enemies=[GuardianDaemon()]
)
all_rooms["Root Directory"] = root_directory

corrupted_entryway = Room(
    name="Corrupted Entryway",
    description="A dark, glitchy hallway. The air is thick, and occasional bursts of static ripple across the floor. A corrupted presence seems to be watching you.",
    exits= {"north": "Distorted Chamber"},
    items=health_potion,
    enemies=GlitchEntity()
)
all_rooms["Corrupted Entryway"] = corrupted_entryway

# Corrupted Section of Rooms (Level 2)
corrupted_sector = Room(
    name="Corrupted Sector", 
    description="The walls here seem unstable, flickering in and out of existence. You feel disoriented, and the air crackles with static. Strange symbols flash across the surfaces as if corrupted code has taken over.",
    exits={"west": "Archive Room", "south": "Hallway"},
    items=[corruption_stone],
    enemies=[GlitchEntity()]
)
all_rooms["Corrupted Sector"] = corrupted_sector

distorted_chamber = Room(
    name="Distorted_Chamber",
    description="This chamber appears warped, with reality shifting in and out of focus. The walls pulse with eerie light, and something ancient resides here.",
    exits={"south": "Corrupted Entryway", "east": "Twisted Passage"},
    items={ancient_tome},
    enemies=[GuardianDaemon()]
)
all_rooms["Distorted Chamber"] = distorted_chamber

twisted_passage = Room(
    name="Twisted Passage",
    description="A narrow passage that bends in impossible ways. You feel time itself is moving strangely here. Shadows move with a life of their own.",
    exits={"west": "Distorted Chamber", "north": "Anomaly Core"},
    items=[mana_crystal],
    enemies=[RestlessSpirit()]
)
all_rooms["Twisted Passage"] = twisted_passage

anomaly_core = Room(
    name="Anomaly Core",
    description="The center of the corrupted sector. Energy pulses from an unseen source, and you hear whispers in an unknown language.",
    exits={"south": "Twisted Passage"},
    items=[arcane_blade],
    enemies=[GuardianDaemon()]
)
all_rooms["Anomaly Core"] = anomaly_core