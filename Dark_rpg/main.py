# Dark_rpg/main.py

import sys
import argparse

from Dark_rpg.game_state import game_state
from Dark_rpg.story.storyline import game_introduction
from Dark_rpg.story.setup import setup_player
from Dark_rpg.zones.hub import choose_location  # moved from forest.py

def parse_args():
    parser = argparse.ArgumentParser(description="Dark RPG CLI Mode")
    parser.add_argument("--auto", action="store_true", help="Run the game in non-interactive auto mode")
    parser.add_argument("--script", type=str, help="Path to a file containing pre-defined input choices")
    return parser.parse_args()

def main():
    args = parse_args()

    # Apply auto mode & script
    game_state["auto"] = args.auto
    game_state["auto_choices"] = []

    if args.script:
        try:
            with open(args.script, 'r') as f:
                game_state["auto_choices"] = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"[ERROR] Script file not found: {args.script}")
            sys.exit(1)

    # Start the game loop
    game_introduction()
    setup_player(auto=args.auto)
    choose_location()

if __name__ == "__main__":
    main()
