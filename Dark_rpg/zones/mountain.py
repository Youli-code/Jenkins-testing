# mountain.py

from Dark_rpg.utils.input_helpers import get_player_choice, wait_for_enter
from Dark_rpg.items.inventory import open_inventory_menu
from Dark_rpg.game_state import game_state
from Dark_rpg.combat.dragon import fight_dragon
from Dark_rpg.zones.navigation import register_zone, go_to

def mountain_path():
    print("\nYou begin a hazardous climb up the mountain trail. Loose rocks tumble beneath your feet.")
    print("Eventually, you reach a plateau with abandoned houses and a warning scrawled on a wall...")

    print("\n1. Sleep within the houses")
    print("2. Continue further up the mountain")
    print("3. Climb down to the crossroads")
    print("4. Open your Inventory")

    choice = get_player_choice("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"], mountain_path)
    if not choice:
        return

    if choice == "1":
        game_state["player_health"] = game_state["player_max_health"]
        print(f"Health restored to {game_state['player_health']} HP!")
        mountain_path()
    elif choice == "2":
        check_ark()
    elif choice == "3":
        go_to("forest_crossroads")
    elif choice == "4":
        open_inventory_menu(mountain_path)

def check_ark():
    print("\nYou find a massive ark with a stone slot in the center...")

    if not game_state["magic_stone_obtained"]:
        print("Something is missing. You must return later.")
        mountain_path()
    else:
        print("The stone fits! The ark opens...")
        final_mountain_ascent()

def final_mountain_ascent():
    print("\nYou climb through the mountain and reach a stormy plateau. A Dragon descends.")

    wait_for_enter("\nPress ENTER to brace for battle...")

    fight_mode = get_player_choice(
        "\nFight the Dragon in Auto or Manual mode? (A/M): ", ["A", "M"], final_mountain_ascent
    )
    fight_dragon(fight_mode)

register_zone("mountain_path", mountain_path)
