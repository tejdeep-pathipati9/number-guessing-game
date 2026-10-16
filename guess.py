"""
A CLI based Number Guessing Game

Players guess a randomly chosen number.
They can choose a difficulty level and game mode.
Each diffuclty level has its own attempt limit and number range.
"""

import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")
# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

diffculty_levels = {1: "Easy", 2: "Medium", 3:"Hard"}
range_attempts_map = {"Easy": [50, 10], "Medium": [100, 8], "Hard": [500,10]}

n = len(diffculty_levels)

print("\nThe game levels are:\n")
for index, choice in diffculty_levels.items():
    print(f"  {index}.{choice}")

selected_choice = input("\nTo get started please pick a difficulty level from the options above: ").strip()

while not selected_choice.isdigit() or not int(selected_choice) in diffculty_levels:
    selected_choice = input(f"Invalid option! Choose a number between 1 to {n}: ").strip()
        
selected_choice = int(selected_choice)
        
diffculty = diffculty_levels[selected_choice]
end_range = range_attempts_map[diffculty][0]
attempt_limit = range_attempts_map[diffculty][1]

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
print("\nThe game modes are:\n")
game_modes = {1: "Classic", 2: "Time Challenge"}

m = len(game_modes)

for index, mode in game_modes.items():
    print(f"  {index}.{mode}")

mode = input("\nChoose a mode from above options:").strip()

while not mode.isdigit() or not int(mode) in game_modes:
    mode = input(f"Invalid game mode! Choose a number between 1 to {m}: ").strip()

mode = int(mode)
selected_mode = game_modes[mode]

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

if DEBUG_SECRET is None:
    secret_number = random.randint(1, end_range)
else:
    secret_number = DEBUG_SECRET
# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
attempts_used = 0
won = False

if selected_mode == "Classic":
    while attempts_used < attempt_limit:
        number = input("Guess the number: ").strip()

        while not number.isdigit() or int(number) not in range(1, end_range + 1):
            number = input(f"Invalid input! Please enter a number between 1 and {end_range}: ").strip()

        number = int(number)
        attempts_used += 1


        if number > secret_number:
            print("You guessed too high!")

        elif number < secret_number:
            print("You guessed too low!") 

        else:
            print(f"You guessed the number correctly in {attempts_used} attempts!")
            break

        print(f"Attempts remaining: {attempt_limit - attempts_used}")

else:
    start_time = time.monotonic()

    while attempts_used < attempt_limit:
        elapsed = time.monotonic() - start_time
        remaining = max(0, TIME_LIMIT - elapsed)
        print(f"Time remaining: {round(remaining)} seconds")

        number = input("Guess the number: ").strip()
    
        while not number.isdigit() or int(number) not in range(1, end_range + 1):
            number = input(f"Invalid input! Please enter a number between 1 and {end_range}: ").strip()
    
        number = int(number)

        if time.monotonic() - start_time >= TIME_LIMIT:
                print(f"Time's up! The secret number was {secret_number}.")
                break
        
        attempts_used += 1
    
        if number > secret_number:
            print("You guessed too high!")
    
        elif number < secret_number:
            print("You guessed too low!") 
    
        else:
            print(f"You guessed the number correctly in {attempts_used} attempts!")
            won = True
            break
    
        print(f"Attempts remaining: {attempt_limit - attempts_used}")



# ---------- End of round ----------
# Goal: show the result that matches how the round ended.




