import player
import room 
import save_load

def handle_combat(player, enemies):
    """Handles a combat encounter between the player and a list of enemies."""
    while enemies and player.health > 0: 
        # Player's turn
        print("\nYour turn:")
        player.display_status()
        action = input("Choose an action (attack / use {item}): ").lower()

        if action == "attack":
            # Basic attack for now, you'll expand this later
            target_enemy = enemies[0]  # Target the first enemy for now
            player.attack(target_enemy) 
            if target_enemy.health <= 0:
                print(f"You defeated the {target_enemy.name}!")
                enemies.remove(target_enemy)

        # Enemies' turn
        for enemy in enemies:
            enemy.attack(player)
            if player.health <= 0:
                print("You have been defeated!")
                return  # End combat if the player is defeated

        # Check for victory
        if not enemies:
            print("You have defeated all enemies!")
    # End of combat

def main():
    """Main game loop."""

    # 1. Initialize the game
    current_room = room.get_starting_room()  # Get the initial room (e.g., closet)
    player_character = player.create_player()  # Create the player character

    input_history = []

    # 2. Main game loop
    while True: 
        # 2.1 Display the current room and player status
        current_room.describe()
        player_character.display_status()

        # 2.2 Get player input
        try:
            action = input("> ").lower()
        except KeyboardInterrupt:  # Handle Ctrl+C to exit gracefully
            break
        input_history.append(action)

        # 2.3 Handle player actions
        if action.startswith("cd"):
            # Handle movement to a different room
            parts = action.split()  # Split the input into parts (e.g., ["cd", "bedroom"])
            if len(parts) == 2:
                direction = parts[1]
                if direction in current_room.exits:
                    current_room = room.get_room_by_name(current_room.exits[direction])  # Implement get_room_by_name in room.py
                else:
                    print("You can't go that way.")
            else:
                print("Invalid 'cd' command. Usage: cd <direction>")
                # Check for combat after movement
            if current_room.enemies:
                handle_combat(player_character, current_room.enemies)
                
        elif action.startswith("ls"):
            # List contents of the current room
            current_room.describe()  # This already prints items and enemies if present

        elif action.startswith("search"):
            # Search for items in the room (basic implementation for now)
            if current_room.items:
                found_item = current_room.items.pop(0)  # Remove and get the first item
                player_character.inventory.append(found_item)
                print(f"You found a {found_item.name}! {found_item.description}")
            else:
                print("You couldn't find anything.")
           
            # Help Command       
        elif action == "help":
            # List all avaliable commands
            print("\nAvaliable Commands:")
            print(" - go <direction>: Move to another room.")
            print(" - look: Look around the current room.")
            print(" - pick up <item>: Pick up an item from the current room.")
            print(" - attack: Attack an enemy during combat.")
            print(" - use <item>: Use an item from your inventory.")
            print(" - inventory: Check your inventory.")
            print(" - save: Save your current progress.")
            print(" - load: Load a previously saved game.")
            print(" - quit: Quit the game.")

        elif action.startswith("use"):
            parts = action.split()
            if len(parts) == 2:
                item_name = parts[1]
                for item in player_character.inventory:
                    if item.name.lower() == item_name.lower():
                        # Use the item and display its effect
                        message = item.use()
                        print(message)
                        if item.heal > 0:
                            player_character.health += item.heal
                            player_character.inventory.remove(item)
                        elif item.key_for:
                            if current_room.name == item.key_for: 
                                print(f"You used the {item.name} to unlock the door!")
                        # Add logic to unlock the door or reveal a passage
                            else:
                                print(f"The {item.name} doesn’t seem to work here.")
                                # Handle other item effects if needed
                        break
                else:
                    print(f"You don't have a {item_name} in your inventory.")
            else:
                print("Invalid 'use' command. Usage: use <item_name>")


        elif action.startswith("pick up"):
            parts = action.split("pick up ")
            if len(parts) < 2 or not parts[1].strip():
                print("Please specify the item you want to pick up. Usage: pick up <item name>")
            else:
                item_name = parts[1].strip()
                found_item = None
                for item in current_room.items:
                    if item.name.lower() == item_name.lower():
                        found_item = item
                        break
                if found_item:
                    player_character.inventory.append(found_item)
                    current_room.items.remove(found_item)
                    print(f"You picked up {found_item.name}!")
                else:
                    print(f"There is no {item.name} here.")
    
        elif action == "look":
            # Describe current room
            current_room.describe()

        elif action == "save":
            # Save current game
            save_load.save_game(player_character, current_room)

        elif action == "load":
            # Load current game
            player_character, current_room = save_load.load_game()

        elif action == "quit":
            break  # Exit the game loop
        else:
            print("Invalid action. Try again.")
        
if __name__ == "__main__":
    main()
