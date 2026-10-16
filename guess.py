"""
A CLI based Number Guessing Game.

Players guess a randomly chosen number.
The game supports difficulty levels, attempt limits, and different game modes.
"""

import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Difficulty selection
difficulty_levels = {
    1: "Easy", 
    2: "Medium", 
    3:"Hard",
}

range_attempts_map = {
    "Easy": [50, 10], 
    "Medium": [100, 8], 
    "Hard": [500,10],
}

num_difficulty_levels = len(difficulty_levels)

print("\nThe game levels are:\n")
for index, choice in difficulty_levels.items():
    print(f"  {index}.{choice}")

selected_choice = input(
    "\nTo get started please pick a difficulty level from the options above: "
).strip()

# Keep asking until a valid difficulty level is chosen
while not selected_choice.isdigit() or int(selected_choice) not in difficulty_levels:
    selected_choice = input(
        f"Invalid option! Choose a number between 1 to {num_difficulty_levels}: "
    ).strip()
        
selected_choice = int(selected_choice)
        
difficulty = difficulty_levels[selected_choice]
end_range = range_attempts_map[difficulty][0]
attempt_limit = range_attempts_map[difficulty][1]

# ---------- Choose a mode ----------
# Game Mode selection
game_modes = {
    1: "Classic", 
    2: "Time Challenge",
}

num_game_modes = len(game_modes)

print("\nThe game modes are:\n")
for index, mode in game_modes.items():
    print(f"  {index}.{mode}")

mode = input("\nChoose a mode from above options:").strip()

# Keep asking until a valid game mode is selected
while not mode.isdigit() or int(mode) not in game_modes:
    mode = input(
        f"Invalid game mode! Choose a number between 1 to {num_game_modes}: "
    ).strip()

mode = int(mode)
selected_mode = game_modes[mode]

# ---------- Set up the round ----------
# Generate a random number unless a fixed secret is set for testing
if DEBUG_SECRET is None:
    secret_number = random.randint(1, end_range)
else:
    secret_number = DEBUG_SECRET

# ---------- Guess loop ----------
# Classic Mode
attempts_used = 0
won = False

if selected_mode == "Classic":
    while attempts_used < attempt_limit:
        guess = input("Guess the number: ").strip()

        # Keep asking for a valid guess without using an attempt
        while not guess.isdigit() or int(guess) not in range(1, end_range + 1):
            guess = input(
                f"Invalid input! Please enter a number between 1 and {end_range}: "
            ).strip()

        guess = int(guess)
        attempts_used += 1

        if guess > secret_number:
            print("You guessed too high!")

        elif guess < secret_number:
            print("You guessed too low!") 

        else:
            attempt_word = "attempt" if attempts_used == 1 else "attempts"
            print(f"You guessed the number correctly in {attempts_used} {attempt_word}!")
            won = True
            break

        print(f"Attempts remaining: {attempt_limit - attempts_used}")

# Time Challenge Mode
else:
    # Start the timer once so it doesn't reset after each guess
    start_time = time.monotonic()

    while attempts_used < attempt_limit:
        elapsed = time.monotonic() - start_time
        remaining = max(0, TIME_LIMIT - elapsed)
        print(f"Time remaining: {remaining:.1f} seconds")

        if remaining <= 0:
            print(f"Time's up! The secret number was {secret_number}.")
            break

        guess = input("Guess the number: ").strip()

        # Keep asking for a valid guess without using an attempt
        while not guess.isdigit() or int(guess) not in range(1, end_range + 1):
            guess = input(
                f"Invalid input! Please enter a number between 1 and {end_range}: "
            ).strip()
    
        guess = int(guess)

        if time.monotonic() - start_time >= TIME_LIMIT:
            print(f"Time's up! The secret number was {secret_number}.")
            break
        
        attempts_used += 1
    
        if guess > secret_number:
            print("You guessed too high!")
    
        elif guess < secret_number:
            print("You guessed too low!") 
    
        else:
            attempt_word = "attempt" if attempts_used == 1 else "attempts"
            print(f"You guessed the number correctly in {attempts_used} {attempt_word}!")
            won = True
            break
    
        print(f"Attempts remaining: {attempt_limit - attempts_used}")

# Reveal the secret number if the player runs out of attempts
if not won and attempts_used >= attempt_limit:
    print(f"You ran out of attempts! The secret number was {secret_number}.")