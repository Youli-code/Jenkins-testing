# Dark_rpg/utils/input_helpers.py

from Dark_rpg.game_state import game_state

def get_player_choice(prompt, valid_options, retry_function):
    if game_state.get("auto") and game_state["auto_choices"]:
        choice = game_state["auto_choices"].pop(0)
        print(f"[AUTO CHOICE] {prompt.strip()} → {choice}")
        if choice in valid_options:
            return choice
        else:
            print(f"[AUTO ERROR] Invalid choice: {choice}")
            return retry_function()

    choice = input(prompt)
    if choice in valid_options:
        return choice
    print("Invalid choice.")
    return retry_function()

def get_player_answer(prompt, allowed_responses, retry_func):
    if game_state.get("auto") and game_state["auto_choices"]:
        ans = game_state["auto_choices"].pop(0).upper()
        print(f"[AUTO ANSWER] {prompt.strip()} → {ans}")
        if ans in allowed_responses:
            return ans
        else:
            print(f"[AUTO ERROR] Invalid answer: {ans}")
            return retry_func()

    ans = input(prompt)
    if ans.upper() in allowed_responses:
        return ans.upper()
    print("Invalid choice. Please try again.")
    return get_player_answer(prompt, allowed_responses, retry_func)

def wait_for_enter(message="Press ENTER to continue..."):
    if game_state.get("auto"):
        print(f"[AUTO] {message}")
        return
    input(message)