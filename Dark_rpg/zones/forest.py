# forest.py

from Dark_rpg.utils.input_helpers import get_player_choice, get_player_answer
from Dark_rpg.items.inventory import open_inventory_menu
from Dark_rpg.game_state import game_state
from Dark_rpg.zones.navigation import register_zone, go_to
from Dark_rpg.combat.wolf import fight_dire_wolf


def forest_options():
    print("\nYou stand among towering trees and creeping shadows.")
    print("1. Look around the forest")
    print("2. Confront the Dire Wolf")
    print("3. Return to the main location menu")
    print("4. Open your Inventory")

    choice = get_player_choice("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"], forest_options)
    if not choice:
        return

    if choice == "1":
        if game_state["has_magical_sword"]:
            go_to("forest_crossroads")
        else:
            print("You explore the forest, discovering broken swords and footprints leading deeper into the woods...")
            forest_options()
    elif choice == "2":
        print("The Dire Wolf emerges!")
        fight_mode = get_player_answer("\nAuto or Manual fight? (A/M): ", ["A", "M"], forest_options)
        fight_dire_wolf(fight_mode)
        if game_state["player_health"] > 0:
            forest_options()
    elif choice == "3":
        go_to("hub")
    elif choice == "4":
        open_inventory_menu(forest_options)

def deeper_forest_path():
    print("\nYou move deeper into the gloom. A Grizzly Bear appears!")
    fight_mode = get_player_answer(
        "\nAuto or Manual fight? (A/M): ", ["A", "M"], deeper_forest_path
    )
    from Dark_rpg.combat.bear import fight_grizzly_bear
    fight_grizzly_bear(fight_mode)

    # Handle outcome logic and new AC if skinned...
    # Then end at:
    go_to("forest_crossroads")

register_zone("deeper_forest_path", deeper_forest_path)

def forest_crossroads():
    print("\nAs you move beyond the forest edge, you come upon a crossroads...")
    print("1. Climb up the mountain trail")
    print("2. Press deeper into the dark woods")
    print("3. Head toward the stream")
    print("4. Open your Inventory")

    choice = get_player_choice("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"], forest_crossroads)
    if not choice:
        return

    if choice == "1":
        go_to("mountain_path")
    elif choice == "2":
        go_to("deeper_forest_path")
    elif choice == "3":
        go_to("stream_path")
    elif choice == "4":
        open_inventory_menu(forest_crossroads)



register_zone("forest_options", forest_options)
register_zone("forest_crossroads", forest_crossroads)
