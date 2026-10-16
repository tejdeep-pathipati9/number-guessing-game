# Number Guessing Game

A Python command-line game where players guess a randomly generated number using high and low hints.

## Features

- Classic and Time Challenge modes
- Three difficulty levels
- Limited guessing attempts

## Difficulty Levels

| Level | Range | Attempts |
|---|---|---|
| Easy | 1–50 | 10 |
| Medium | 1–100 | 8 |
| Hard | 1–500 | 10 |

## How to Run

1. Clone the repository and navigate to the project folder.

2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate the virtual environment:

   **macOS:**
   ```bash
   source .venv/bin/activate
   ```

4. Run the game:

   ```bash
   python3 guess.py
   ```

Choose a difficulty level and game mode, then guess the number before running out of attempts or time.

## Test Plan

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
| 1 | Invalid difficulty | Entered 4, then 3 | Reject invalid choice | Rejected 4, accepted 3 | Yes |
| 2 | Invalid game mode | Entered 3, then 2 | Reject invalid mode | Rejected 3, accepted 2 | Yes |
| 3 | Low guess | Guessed 3 when secret was 17 | Display too low hint | Displayed too-low hint | Yes |
| 4 | High guess | Guessed 42 when secret was 17 | Display too-high hint | Displayed too-high hint | Yes |
| 5 | Correct guess | Guessed 17 on attempt 7 | Display win message | Won in 7 attempts | Yes |
| 6 | Hard difficulty | Selected Hard | Allow 10 attempts | Started with 10 attempts | Yes |
| 7 | Countdown timer | Selected Time Challenge | Display remaining time | Displayed decreasing time | Yes |
| 8 | Timeout | Set timer to 5 seconds and waited | End game and reveal number | Revealed 268 | Yes |
| 9 | Invalid text | Enter `abc` | Reject without losing attempt | Rejected abc | Yes |
| 10 | Out-of-range guess | Select Easy, enter 100 | Reject without losing attempt | Rejected 100 | Yes |
| 11 | Attempts exhausted | Set secret to 35, guess 1 ten times on Easy | End game and reveal 35 | Revealed secret number 35 | Yes |
| 12 | Correct guess after timeout | Set secret to 35, wait 6 seconds with a 5-second timer, then guess 35 | Timeout instead of win | Guessed 35, but game displayed timeout | Yes |