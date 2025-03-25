# setup.py

from Dark_rpg.game_state import game_state

def setup_player(auto=False):
    if auto:
        print("\n[Auto Mode] Using default player stats...")
        game_state["attack_power"] = 10
        game_state["armor_class"] = 15
        print(f"Attack Power: {game_state['attack_power']}")
        print(f"Armor Class: {game_state['armor_class']}")
    else:
        game_state["attack_power"] = int(input("Enter Attack Power: "))
        ac_input = int(input("Enter Armor Class (Max 20): "))
        game_state["armor_class"] = min(ac_input, 20)

    print("\nDespite feeling a wave of nausea, you finally stumble out of the cave.")
    print("Outside, you spot small animal corpses and a few broken logs scattered about.")
    print("It's clear something—or someone—must have carried them here...")