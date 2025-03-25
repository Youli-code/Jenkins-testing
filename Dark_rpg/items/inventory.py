# Dark_rpg/items/inventory.py

from Dark_rpg.game_state import game_state

def show_inventory():
    inv = game_state["inventory"]
    if not inv:
        print("\nYour inventory is currently empty.")
    else:
        print("\nYour Inventory contains:")
        for item in inv:
            print(f" - {item}")

def open_inventory_menu(current_menu_func):
    show_inventory()
    current_menu_func()