# dragon.py

from Dark_rpg.game_state import game_state
from Dark_rpg.combat.battle_system import calculate_damage_dealt_for_player
from Dark_rpg.core.game_loop import game_over

def fight_dragon(fight_mode):
    game_state["in_combat"] = True
    dragon_health, dragon_ac, dragon_attack_power = 100, 15, 18
    player_skip_turn = dragon_skip_turn = False

    while game_state["player_health"] > 0 and dragon_health > 0:
        if player_skip_turn:
            player_skip_turn = False
        else:
            if fight_mode == "M":
                input("Roll!")
            damage, skip = calculate_damage_dealt_for_player(game_state["attack_power"], dragon_ac)
            dragon_health -= damage
            if skip: player_skip_turn = True
            if dragon_health <= 0:
                print("The Dragon has been defeated!")
                game_state["dragon_defeated"] = True
                break

        if dragon_skip_turn:
            dragon_skip_turn = False
        else:
            damage, skip = calculate_damage_dealt_for_player(dragon_attack_power, game_state["armor_class"])
            game_state["player_health"] -= damage
            if skip: dragon_skip_turn = True
            if game_state["player_health"] <= 0:
                print("You are slain by the Dragon.")
                game_over()
                return

    game_state["in_combat"] = False
