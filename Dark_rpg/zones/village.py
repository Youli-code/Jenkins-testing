# Dark_rpg/zones/village.py

from Dark_rpg.utils.input_helpers import get_player_choice, get_player_answer
from Dark_rpg.items.inventory import open_inventory_menu
from Dark_rpg.game_state import game_state

def village_options():
    print("\nYou enter the god-forsaken village. The streets are empty, and an eerie silence fills the air.")
    print("1. Speak with the Village Elder")
    print("2. Look around the village")
    print("3. Return to the main location menu")
    print("4. Open your Inventory")

    choice = get_player_choice("Enter 1, 2, 3, or 4: ", ["1","2","3","4"], village_options)
    if not choice:
        return

    if choice == "1":
        print("You approach the Elder... (placeholder)")
        # Eventually: from Dark_rpg.zones.elder import speak_with_elder()
        # speak_with_elder()
    elif choice == "2":
        print("You wander through the village...")
        village_options()
    elif choice == "3":
        from Dark_rpg.zones.forest import choose_location
        choose_location()
    elif choice == "4":
        open_inventory_menu(village_options)

        
# ---------------------------
# Elder & Sword Logic
# ---------------------------
def speak_with_elder():
    print("\nYou approach the Village Elder, a frail man with eyes that have seen many winters.")

    if not game_state["magical_sword_found"]:
        print('"I once possessed a Magical Sword," he says gravely, "but I lost it two moons ago')
        print('when a pack of ravenous wolves chased me from the forest. If you truly seek')
        print('adventure—and that blade—you must face them. But I won’t force you to do so."')

        ans = get_player_answer("\nWill you accept the quest to recover the Magical Sword? (Y/N): ", ["Y","N"], speak_with_elder)
        if ans == "Y":
            game_state["elder_quest_accepted"] = True
            print("\nElder: \"I thank you, brave one. Return if you learn anything of the sword’s whereabouts.\"")
            print("(QUEST: Find the Magical Sword!)")
        else:
            print("\nElder: \"I understand—these are dark times, and not all are suited for such dangers.\"")
            print("(You declined the quest...)")

    else:
        # We have found the sword by killing 3 wolves, let's see if the player wants to keep it
        if game_state["has_magical_sword"]:
            print('"I see you carry the Magical Sword. You are truly a hero among these humble folk."')
            print("\nElder: \"With that blade in hand, you might just push through the darkest paths of the forest.")
            print("You may well be able to make your way out of here entirely.\"")
        else:
            print('"You have found my Magical Sword!" the Elder exclaims. "My fighting days are long behind me,')
            print('and I have no need for it now. Will you keep it?"')
            ans = get_player_answer("\nKeep the sword? (Y/N): ", ["Y","N"], speak_with_elder)
            if ans == "Y":
                game_state["has_magical_sword"] = True
                game_state["inventory"].append("Magical Sword")
                game_state["attack_power"] += 6
                print("\nElder: \"Then may it serve you well, hero.\"")
                print("You place the gleaming blade at your side, feeling its power course through your veins.")
                print("\nElder: \"With the sword in your hands, you can finally venture deeper into the forest.")
                print("Perhaps you will find a path leading beyond these cursed woods.\"")
            else:
                print("\nElder: \"Very well, I shall keep it safe. Fare thee well on your travels.\"")

    village_options()