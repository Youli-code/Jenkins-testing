# stream.py

from Dark_rpg.utils.input_helpers import get_player_choice
from Dark_rpg.items.inventory import open_inventory_menu
from Dark_rpg.game_state import game_state
from Dark_rpg.zones.navigation import register_zone, go_to

def stream_path():
    print("\nYou reach a foggy lake with a small island in the center.")

    print("\n1. Swim to the island")
    print("2. Return to the crossroads")
    print("3. Open your Inventory")

    choice = get_player_choice("Enter 1, 2, or 3: ", ["1", "2", "3"], stream_path)
    if not choice:
        return

    if choice == "1":
        swim_to_island()
    elif choice == "2":
        go_to("forest_crossroads")
    elif choice == "3":
        open_inventory_menu(stream_path)

def swim_to_island():
    print("\nYou swim across the cold lake and arrive at a haunted island.")
    island_encounter()

def island_encounter():
    print("\nTwo skeletons lie beside a buried chest...")

    print("\n1. Inspect the bodies")
    print("2. Investigate the chest")
    print("3. Return to shore")
    print("4. Open Inventory")

    choice = get_player_choice("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"], island_encounter)
    if not choice:
        return

    if choice == "1":
        inspect_bodies()
    elif choice == "2":
        investigate_chest()
    elif choice == "3":
        go_to("stream_path")
    elif choice == "4":
        open_inventory_menu(island_encounter)

def inspect_bodies():
    if not game_state["chest_key_found"]:
        print("You find a rusted key and pocket it.")
        game_state["chest_key_found"] = True
        game_state["inventory"].append("Rusted Key")
    else:
        print("Nothing else of value remains.")
    island_encounter()

def investigate_chest():
    if game_state["chest_opened"]:
        print("The chest is already open.")
    elif not game_state["chest_key_found"]:
        print("It's locked. You need a key.")
    else:
        print("The chest opens! Inside is a Mysterious Stone.")
        game_state["chest_opened"] = True
        game_state["magic_stone_obtained"] = True
        game_state["inventory"].append("Mysterious Stone")
    island_encounter()

register_zone("stream_path", stream_path)
