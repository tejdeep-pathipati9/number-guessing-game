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


# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.




