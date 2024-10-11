import json 
from player import Player

def save_game(player, current_room):
    """Saves the game state to a file."""
    data = {
        "player": {
            "name": player.name,
            "health": player.health,
            "mana": player.mana,
            "strength": player.strength,
            "inventory": player.inventory
        },
        "current_room": current_room.name 
    }

    try:
        with open("save_game.json", "w") as save_file:
            json.dump(data, save_file, indent=4)  
        print("Game saved successfully!")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game():
    """Loads the game state from a file."""
    try:
        with open("save_game.json", "r") as save_file:
            data = json.load(save_file)

      
        player = Player(
            data["player"]["name"],
            data["player"]["health"],
            data["player"]["mana"],
            data["player"]["strength"]
        )
        player.inventory = data["player"]["inventory"]

       
        current_room = get_room_by_name(data["current_room"])  

        print("Game loaded successfully!")
        return player, current_room

    except FileNotFoundError:
        print("No saved game found.")
        return None, None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None

def get_room_by_name(room_name):
    
    global all_rooms
    return all_rooms.get(room_name, None)