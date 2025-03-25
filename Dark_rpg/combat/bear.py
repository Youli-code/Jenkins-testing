# bear.py

from Dark_rpg.game_state import game_state
from Dark_rpg.combat.battle_system import calculate_damage_dealt_for_player
from Dark_rpg.core.game_loop import game_over

def fight_grizzly_bear(fight_mode):
    game_state["in_combat"] = True
    bear_health, bear_ac, bear_attack_power = 50, 13, 15
    player_skip_turn = bear_skip_turn = False

    while game_state["player_health"] > 0 and bear_health > 0:
        if player_skip_turn:
            player_skip_turn = False
        else:
            if fight_mode == "M":
                input("Roll!")
            damage, skip = calculate_damage_dealt_for_player(game_state["attack_power"], bear_ac)
            bear_health -= damage
            if skip: player_skip_turn = True
            if bear_health <= 0:
                print("You defeated the Grizzly Bear!")
                break

        if bear_skip_turn:
            bear_skip_turn = False
        else:
            damage, skip = calculate_damage_dealt_for_player(bear_attack_power, game_state["armor_class"])
            game_state["player_health"] -= damage
            if skip: bear_skip_turn = True
            if game_state["player_health"] <= 0:
                print("The Bear defeats you.")
                game_over()
                return

    game_state["in_combat"] = False
