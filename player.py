class Player:
    def __init__(self, name, starting_health=100, starting_mana=50, starting_strength=10):
        self.name = name
        self.health = starting_health
        self.mana = starting_mana
        self.strength = starting_strength
        self.inventory = []  # Start with an empty inventory

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print(f"Strength: {self.strength}")
        print("Inventory:", ", ".join([item.name for item in self.inventory]) or "Empty")   

    def attack(self, target):
        damage = self.strength  # Basic attack using strength for now
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage! HP: {target.health}") # Display the attack and target's Health

def create_player():
    name = input("Enter your character's name: ")
    return Player(name)

def display_inventory(self):
    if self.inventory:
        print("\nYour Inventory:")
        for item in self.inventory:
            print(f" - {item.name}: {item.description}")
    else:
        print("\nYour inventory is empty.")