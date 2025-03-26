# game_loop.py

from Dark_rpg.utils.input_helpers import wait_for_enter
from Dark_rpg.game_state import reset_game_state
import Dark_rpg.main as game_main

def game_over():
    """
    Called when player's health <= 0. Instead of closing,
    restarts the entire game from scratch.
    """
    print("\nYour vision fades as you succumb to your wounds...")
    print("The world slips away into darkness.")

    wait_for_enter("\nPress ENTER to restart the game.")
    reset_game_state()  # Reset everything
    game_main.main()    # Restart the entire flow