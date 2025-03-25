import random

def calculate_damage_dealt_for_player(attacker_power, defender_ac):
    dice_roll = random.randint(1, 20)
    print(f"Dice Roll: {dice_roll}")

    if dice_roll == 20:
        print("Natural 20! Critical Hit! (Double Damage)")
        return attacker_power * 2, False
    elif dice_roll == 1:
        print("Natural 1! Critical Miss! You skip your next turn.")
        return 0, True
    elif dice_roll >= defender_ac:
        print("Hit!")
        return attacker_power, False
    else:
        print("Missed the attack!")
        return 0, False
