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
            target_enemy = enemies[0]  
            player.attack(target_enemy) 
            if target_enemy.health <= 0:
                print(f"You defeated the {target_enemy.name}!")
                enemies.remove(target_enemy)

        # Enemies' turn
        for enemy in enemies:
            enemy.attack(player)
            if player.health <= 0:
                print("You have been defeated!")
                return

        # Check for victory
        if not enemies:
            print("You have defeated all enemies!")
    # End of combat

def main():
    """Main game loop."""

    # 1. Initialize the game
    current_room = room.get_starting_room()  
    player_character = player.create_player()  

    input_history = []

    # 2. Main game loop
    while True: 
        # 2.1 Display the current room and player status
        current_room.describe()
        player_character.display_status()

        # 2.2 Get player input
        try:
            action = input("> ").lower()
        except KeyboardInterrupt:
            break
        input_history.append(action)

        # 2.3 Handle player actions
        if action.startswith("cd"):
            parts = action.split()  
            if len(parts) == 2:
                direction = parts[1]
                if direction in current_room.exits:
                    current_room = room.get_room_by_name(current_room.exits[direction])  
                else:
                    print("You can't go that way.")
            else:
                print("Invalid 'cd' command. Usage: cd <direction>")
                
            if current_room.enemies:
                handle_combat(player_character, current_room.enemies)
                
        elif action.startswith("ls"):
            current_room.describe()
        elif action.startswith("search"):
            
            if current_room.items:
                found_item = current_room.items.pop(0)  
                player_character.inventory.append(found_item)
                print(f"You found a {found_item.name}! {found_item.description}")
            else:
                print("You couldn't find anything.")
           
        elif action == "help":
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
                        message = item.use()
                        print(message)
                        if item.heal > 0:
                            player_character.health += item.heal
                            player_character.inventory.remove(item)
                        elif item.key_for:
                            if current_room.name == item.key_for: 
                                print(f"You used the {item.name} to unlock the door!")
                            else:
                                print(f"The {item.name} doesn’t seem to work here.")
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
                    
        elif action.startswith("talk to "):
            npc_name = action.split("talk to ")[1].strip()
            found_npc = None
            for npc in current_room.npcs:
                if npc.name.lower() == npc_name.lower():
                    found_npc = npc
                    break
            if found_npc:
                found_npc.talk()
                quest = found_npc.give_quest()
                if quest:
                    player_character.active_quests.append(quest)
            else:
                print(f"There is no one neame {npc_name} here.")

        elif action == "look":
            current_room.describe()

        elif action == "save":
            save_load.save_game(player_character, current_room)

        elif action == "load":
            player_character, current_room = save_load.load_game()

        elif action == "quit":
            break
        else:
            print("Invalid action. Try again.")
        
if __name__ == "__main__":
    main()