# ---------------------------
# Global game state
# ---------------------------
game_state = {
    "player_health": 100,          # Always 100
    "player_max_health": 100,      # Also 100
    "attack_power": 0,             # User can still choose
    "armor_class": 0,              # User can still choose
    "in_combat": False,

    "dire_wolf_defeated_count": 0,
    "magical_sword_found": False,
    "has_magical_sword": False,
    "elder_quest_accepted": False,

    "inventory": [],

    "bear_defeated": False,

    "chest_key_found": False,
    "chest_opened": False,
    "magic_stone_obtained": False,

    "dragon_defeated": False
}

def reset_game_state():
    """
    Resets our dictionary to original defaults for a fresh restart.
    """
    global game_state
    game_state = {
        "player_health": 100,
        "player_max_health": 100,
        "attack_power": 0,
        "armor_class": 0,
        "in_combat": False,

        "dire_wolf_defeated_count": 0,
        "magical_sword_found": False,
        "has_magical_sword": False,
        "elder_quest_accepted": False,

        "inventory": [],

        "bear_defeated": False,

        "chest_key_found": False,
        "chest_opened": False,
        "magic_stone_obtained": False,

        "dragon_defeated": False
    }
