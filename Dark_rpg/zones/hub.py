from Dark_rpg.utils.input_helpers import get_player_choice
from Dark_rpg.items.inventory import open_inventory_menu
from Dark_rpg.game_state import game_state
from Dark_rpg.zones.forest import forest_options
from Dark_rpg.zones.village import village_options

def choose_location():
    if game_state["in_combat"]:
        print("You are in a fight! Leaving now would make you easy prey!")
        return

    print("\nWhere would you like to travel?")
    print("1. The dark and eerie Forest")
    print("2. The distant lights of the Village")
    print("3. Stay put (do nothing for now)")
    print("4. Open your Inventory")

    choice = get_player_choice("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"], choose_location)
    if not choice:
        return

    if choice == "1":
        print("You make your way into the dense, twisted trees of the Forest...")
        forest_options()
    elif choice == "2":
        print("You head toward the Village, hoping to find safety or answers to your predicament...")
        village_options()
    elif choice == "3":
        print("You decide to stay and gather your thoughts for a moment...")
    elif choice == "4":
        open_inventory_menu(choose_location)
