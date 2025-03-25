# wolf.py

from Dark_rpg.game_state import game_state
from Dark_rpg.combat.battle_system import calculate_damage_dealt_for_player

def fight_dire_wolf(fight_mode):
    game_state["in_combat"] = True
    wolf_health, wolf_ac, wolf_attack_power = 30, 12, 8
    player_skip_turn = wolf_skip_turn = False

    while game_state["player_health"] > 0 and wolf_health > 0:
        if player_skip_turn:
            print("You skip your turn.")
            player_skip_turn = False
        else:
            if fight_mode == "M":
                input("Roll the dice!")
            damage, skip = calculate_damage_dealt_for_player(game_state["attack_power"], wolf_ac)
            wolf_health -= damage
            if skip: player_skip_turn = True
            if wolf_health <= 0:
                print("You slayed the Dire Wolf!")
                game_state["dire_wolf_defeated_count"] += 1
                if game_state["dire_wolf_defeated_count"] == 3 and not game_state["magical_sword_found"]:
                    print("You found the Magical Sword!")
                    game_state["magical_sword_found"] = True
                break

        if wolf_skip_turn:
            wolf_skip_turn = False
        else:
            damage, skip = calculate_damage_dealt_for_player(wolf_attack_power, game_state["armor_class"])
            game_state["player_health"] -= damage
            if skip: wolf_skip_turn = True
            if game_state["player_health"] <= 0:
                print("You were defeated by the Dire Wolf.")
                break

    game_state["in_combat"] = False
